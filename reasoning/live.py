"""First-forward evidence capture. No synthetic observations or model tuning."""
import argparse
import calendar
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timedelta,timezone
from pathlib import Path
from statistics import mean,pstdev
from uuid import UUID
from typing import Literal
from pydantic import AwareDatetime,model_validator
from .market_data import SOURCES,RawResponse,collect_one,parse_yahoo,aggregate,treasury_observations,make_observation,freshness
from .schemas.contracts import Contract,DataMode,canonical_hash,canonical_json
from .schemas.artifacts import Warning,EngineResult
from .fixture import Fixture,FactorSpec,Edge
from .engines import EngineRunner,uid
from .technical import analyze_wave
from .workflow import run_fixture
from .journal import RunJournal

ROOT=Path(__file__).resolve().parents[1]
UTC=timezone.utc


class ModelProfile(Contract):
    factors: tuple[FactorSpec,...]
    edges: tuple[Edge,...]
    seed: int
    origin: str
    core_sha256: dict[str,str]

    def verify_core(self):
        for name,digest in self.core_sha256.items():
            if name not in ('engines.py','technical.py','decision.py'):raise ValueError('unexpected core file')
            if hashlib.sha256((ROOT/'reasoning'/name).read_text(encoding='utf-8').encode()).hexdigest()!=digest:
                raise ValueError(f'frozen algorithm changed: {name}')


class RawSnapshot(Contract):
    schema_version: Literal['1.0.0']='1.0.0'
    snapshot_id: UUID
    data_mode: DataMode
    prediction_timestamp: AwareDatetime
    data_cutoff: AwareDatetime
    sources: tuple[RawResponse,...]
    profile: ModelProfile

    @model_validator(mode='after')
    def provenance(self):
        if self.data_cutoff>self.prediction_timestamp:raise ValueError('cutoff after prediction')
        for r in self.sources:
            if r.data_mode!=self.data_mode:raise ValueError('mixed source mode')
            if r.collected_at>self.data_cutoff:raise ValueError('raw source after cutoff')
        if len({r.source.source_id for r in self.sources})!=len(self.sources):raise ValueError('duplicate raw source')
        return self


class SourceStatus(Contract):
    source_id: str
    instrument: str
    provider: str
    authority: str
    raw_sha256: str
    status: str
    latest_effective_at: AwareDatetime | None
    collected_at: AwareDatetime
    released_at: AwareDatetime | None=None
    age_hours: float | None
    rows: int
    excluded: dict[str,int]
    used_by_model: bool
    reason: str | None


class Availability(Contract):
    expected_factors: tuple[str,...]
    present_factors: tuple[str,...]
    missing_factors: tuple[str,...]
    conflicting_factors: tuple[str,...]
    e01_coverage: float
    accounting_status: Literal['unavailable']='unavailable'


class LiveJournal(Contract):
    schema_version: Literal['1.0.0']='1.0.0'
    data_mode: DataMode
    prediction_timestamp: AwareDatetime
    data_cutoff: AwareDatetime
    raw_snapshot_hash: str
    raw_snapshot: RawSnapshot
    source_status: tuple[SourceStatus,...]
    availability: Availability
    run: RunJournal
    outcome_due: dict[str,AwareDatetime]
    completion_blockers: tuple[str,...]

    @model_validator(mode='after')
    def verify(self):
        if self.data_mode!=self.run.data_mode or self.data_mode!=self.raw_snapshot.data_mode:raise ValueError('journal mode mismatch')
        if self.raw_snapshot_hash!=canonical_hash(self.raw_snapshot):raise ValueError('raw snapshot hash mismatch')
        if self.data_cutoff!=self.run.data_cutoff or self.data_cutoff!=self.raw_snapshot.data_cutoff:raise ValueError('cutoff mismatch')
        if self.prediction_timestamp!=self.raw_snapshot.prediction_timestamp:raise ValueError('prediction timestamp mismatch')
        return self


class SealedLive(Contract):
    snapshot: LiveJournal
    sha256: str

    @model_validator(mode='after')
    def verify(self):
        if self.sha256!=canonical_hash(self.snapshot):raise ValueError('live journal hash mismatch')
        return self

    @classmethod
    def seal(cls,journal):return cls(snapshot=journal,sha256=canonical_hash(journal))


def write_immutable(path: Path,value):
    content=(canonical_json(value) if isinstance(value,Contract) else json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')))+'\n'
    encoded=content.encode('utf-8');path.parent.mkdir(parents=True,exist_ok=True)
    try:
        with path.open('xb') as stream:stream.write(encoded)
    except FileExistsError:
        if path.read_bytes()!=encoded:raise ValueError('immutable file already exists with different content')


class LiveRunner(EngineRunner):
    def E11(self):
        if self.fixture.accounting is None:
            return dict(applicable=False,reason='Accounting source unavailable; identities not evaluated',items=())
        return super().E11()

    def execute(self,engine):
        result=super().execute(engine)
        warnings=list(result.warnings)
        if engine=='E01':
            present={s.factor_id for s in self.get('E01').items}
            missing=tuple(s.factor_id for s in self.fixture.factors if s.factor_id not in present)
            if missing:warnings.append(Warning(code='source_missing',message=f'E01 coverage {len(present)}/{len(self.fixture.factors)}; existing E06/E14 confidence penalty and E18 critical gate apply',evidence_refs=missing))
        if engine=='E11' and self.fixture.accounting is None:
            warnings.append(Warning(code='accounting_unavailable',message='No accounting facts supplied; no identity passed',evidence_refs=('source:accounting_unavailable',)))
        values=result.model_dump();values['warnings']=tuple(warnings)
        return EngineResult.model_validate(values)


def prepare(snapshot: RawSnapshot):
    observations=[];bars_by_source={};statuses=[];conflicts=[]
    factor_map={'preferred_daily':'samsung_preferred_price','common_daily':'samsung_common_price','usdkrw':'usdkrw'}
    for raw in snapshot.sources:
        source=raw.source;bars=();obs=();excluded={};reason=raw.error;status=raw.status
        try:
            if status=='available':
                if source.source_id=='treasury_10y':obs=treasury_observations(raw,snapshot.data_cutoff)
                else:
                    bars,excluded=parse_yahoo(raw,snapshot.data_cutoff)
                    if source.source_id in factor_map:
                        obs=tuple(make_observation(raw,factor_map[source.source_id],source.unit,b.close,b.closed_at) for b in bars[-60:])
                latest=max([b.closed_at for b in bars]+[o.observed_at for o in obs],default=None)
                if latest is None:status='unavailable';reason='No completed valid observations'
                else:
                    status=freshness(latest,snapshot.data_cutoff,source.freshness_days)
                    if source.interval=='30m':
                        from zoneinfo import ZoneInfo
                        local=snapshot.data_cutoff.astimezone(ZoneInfo('Asia/Seoul'))
                        if local.weekday()<5 and 10<=local.hour<16 and (snapshot.data_cutoff-latest)>timedelta(hours=2):status='stale'
                    if status=='stale':reason='Freshness SLA exceeded; excluded from reasoning'
            latest=max([b.closed_at for b in bars]+[o.observed_at for o in obs],default=None)
        except (ValueError,KeyError,TypeError) as exc:
            status='conflict' if 'conflict' in str(exc) else 'invalid';reason=str(exc);latest=None;bars=();obs=()
            if status=='conflict':conflicts.append(factor_map.get(source.source_id,source.source_id))
        if status=='fresh':
            observations.extend(obs);bars_by_source[source.source_id]=bars
        statuses.append(SourceStatus(source_id=source.source_id,instrument=source.instrument,provider=source.provider,
            authority=source.authority,raw_sha256=raw.sha256,status=status,latest_effective_at=latest,collected_at=raw.collected_at,
            age_hours=(snapshot.data_cutoff-latest).total_seconds()/3600 if latest else None,rows=len(bars) or len(obs),excluded=excluded,
            used_by_model=status=='fresh' and (bool(obs) or source.source_id=='preferred_30m'),reason=reason))
    daily=bars_by_source.get('preferred_daily',())
    raw=next((r for r in snapshot.sources if r.source.source_id=='preferred_daily'),None)
    if len(daily)>=153 and raw:
        for end in range(len(daily)-3,len(daily)+1):
            window=daily[:end];wave=analyze_wave(window);last=window[-1]
            volumes=[b.volume for b in window[-20:]];std=pstdev(volumes)
            derived={'preferred_rsi_14':wave.rsi,'preferred_trend_alignment':2*sum(last.close>s for s in wave.sma)/3-1,
                     'preferred_volume_z':(last.volume-mean(volumes))/std if std else None}
            units={'preferred_rsi_14':'rsi','preferred_trend_alignment':'score','preferred_volume_z':'z_score'}
            for fid,value in derived.items():
                if value is not None:observations.append(make_observation(raw,fid,units[fid],value,last.closed_at))
    batch=Fixture(data_mode=snapshot.data_mode,fixture_version='real-data-minimum-slice-v1',data_cutoff=snapshot.data_cutoff,
        factors=snapshot.profile.factors,observations=tuple(observations),events=(),edges=snapshot.profile.edges,
        bars={'30m':bars_by_source.get('preferred_30m',()),'1d':daily,'1w':aggregate(daily,'1w',snapshot.data_cutoff),
              '1mo':aggregate(daily,'1mo',snapshot.data_cutoff)},history=(),accounting=None,seed=snapshot.profile.seed)
    present={o.factor_id for o in observations};expected=tuple(s.factor_id for s in snapshot.profile.factors)
    availability=Availability(expected_factors=expected,present_factors=tuple(sorted(present)),missing_factors=tuple(k for k in expected if k not in present),
        conflicting_factors=tuple(conflicts),e01_coverage=len(present)/len(expected))
    return batch,tuple(statuses),availability


def evaluate(snapshot: RawSnapshot):
    snapshot.profile.verify_core()
    batch,statuses,availability=prepare(snapshot);run=run_fixture(batch,LiveRunner)
    date=snapshot.prediction_timestamp;month=date.month%12+1;year=date.year+(date.month==12)
    next_month=date.replace(year=year,month=month,day=min(date.day,calendar.monthrange(year,month)[1]))
    blockers=[]
    if any(h.final is None for h in run.horizons):blockers.append('numeric_forecast_unavailable_critical_inputs_missing')
    if any(not h.technical.wave.available for h in run.horizons):blockers.append('wave_warmup_unavailable')
    blockers.append('accounting_identity_inputs_unavailable')
    return LiveJournal(data_mode=snapshot.data_mode,prediction_timestamp=date,data_cutoff=snapshot.data_cutoff,
        raw_snapshot_hash=canonical_hash(snapshot),raw_snapshot=snapshot,source_status=statuses,availability=availability,run=run,
        outcome_due={'1d':date+timedelta(days=1),'1w':date+timedelta(days=7),'1m':next_month},completion_blockers=tuple(blockers))


def collect_snapshot():
    profile=ModelProfile.model_validate_json((ROOT/'config/live-model-profile.json').read_text(encoding='utf-8'));profile.verify_core()
    with ThreadPoolExecutor(max_workers=4) as pool:raw=tuple(pool.map(collect_one,SOURCES.values()))
    cutoff=datetime.now(UTC)
    identity='/'.join(r.sha256+str(r.collected_at) for r in raw)
    return RawSnapshot(snapshot_id=uid(identity),data_mode='live_forward',prediction_timestamp=cutoff,data_cutoff=cutoff,sources=raw,profile=profile)


def explain(journal: LiveJournal):
    run=journal.run
    lines=['# First live forward evidence',f'Prediction timestamp: {journal.prediction_timestamp.isoformat()}',
        f'Data cutoff: {journal.data_cutoff.isoformat()}',f'Data mode: {journal.data_mode}',f'Run ID: {run.run_id}',
        f'Raw snapshot hash: {journal.raw_snapshot_hash}',f'Core algorithms frozen: {journal.raw_snapshot.profile.core_sha256}',
        '', '## Sources','| Source | Provider/authority | Status | Effective | Collected | Age hours | Rows | Model use |',
        '|---|---|---|---|---|---:|---:|---|']
    for s in journal.source_status:
        lines.append(f'| {s.source_id} | {s.provider}/{s.authority} | {s.status} | {s.latest_effective_at} | {s.collected_at} | {s.age_hours} | {s.rows} | {s.used_by_model} |')
    lines+=['','Released-at is unknown unless supplied explicitly; collection time is the conservative known-at bound.',
        f'Missing factors from E01: {", ".join(journal.availability.missing_factors)}',
        f'Conflicting factors: {journal.availability.conflicting_factors}',f'E01 coverage: {journal.availability.e01_coverage:.1%}. Existing E06/E14 confidence penalties retained.',
        'KOSPI/DXY are captured context feeds; no invented causal edges were added to the frozen model.',
        'Accounting and event/consensus evidence are unavailable, not synthetic. E11 identities are not reported as passed.']
    for h in run.horizons:
        lines+=['',f'## Horizon {h.horizon}',f'Before feedback: {h.initial.probabilities.model_dump() if h.initial else "null / insufficient_evidence"}',
            f'After feedback: {h.final.probabilities.model_dump() if h.final else "null / insufficient_evidence"}',
            f'Confidence: {h.final.confidence if h.final else "null; no publishable forecast"}',
            'Feedback passes: 1; Regime/Flow/Actor interpretation consumes technical evidence.',
            f'Wave primary/context: {h.technical.primary}/{h.technical.higher}',
            f'Bottom/Top reversal score: {h.technical.wave.bottom_score}/{h.technical.wave.top_score}; calibrated probability: unavailable.',
            f'Bottom/Top confirmed: {h.technical.wave.bottom_confirmed}/{h.technical.wave.top_confirmed}',
            f'Bottom features: {h.technical.wave.bottom_features}',f'Top features: {h.technical.wave.top_features}',
            f'Alignment bullish/bearish: {h.technical.bullish_alignment}/{h.technical.bearish_alignment}',
            f'Liquidity buy/sell: {h.technical.buy_liquidity}/{h.technical.sell_liquidity}',
            f'Final decision: {h.decision.action}',f'Failed gates: {", ".join(h.decision.reasons)}']
        gates={'future_up','without_history_up','confidence','bottom_timing','alignment','liquidity','meta_check'}
        lines.append('Passed ENTRY gates: '+', '.join(sorted(gates-set(h.decision.reasons))))
        for title,paths in [('Positive drivers (up to 5)',h.positive_paths),('Negative drivers (up to 5)',h.negative_paths)]:
            lines+=['',title]+[f'- {p.path_id}; sign={p.sign}, strength={p.strength:.6f}, confidence={p.confidence:.6f}, root={p.root_evidence_group}' for p in paths]
            if not paths:lines.append('- None supported; no filler drivers.')
        lines+=['','### Probability contribution ledger']
        if h.final:
            lines+=['| Stage/engine | Before up/down/flat | Delta pp | After |','|---|---|---|---|']
            for c in h.final.ledger:lines.append(f'| {c.stage}/{c.engine_id} | {c.before.vector()} | {c.delta_pp} | {c.after.vector()} |')
            lines.append(f'Feedback probability delta: {tuple(b-a for a,b in zip(h.initial.probabilities.vector(),h.final.probabilities.vector()))}')
        else:lines.append('No numeric final probability or delta exists: critical input is missing. Prior is not relabeled as a forecast. Causal effects remain inspectable below.')
        for engine in ('E09','E12','E13','E19'):
            record=next(r for r in run.executions if r.horizon==h.horizon and r.generation==1 and r.engine_id==engine)
            lines+=['',f'### {engine} structured reasoning', '```json',record.result.output_artifact.payload.model_dump_json(indent=2),'```']
        lines+=['','### What Would Change My Mind','Supply genuine critical DRAM evidence and missing flow/accounting sources, then create a NEW forward prediction. Do not edit this one.']
        hypotheses=next(r.result.output_artifact.payload for r in run.executions if r.horizon==h.horizon and r.generation==1 and r.engine_id=='E07')
        for hyp in hypotheses.items:
            for f in hyp.falsifiers:lines.append(f'- {hyp.direction}: {f.factor_id} {f.operator} {f.threshold} {f.unit}')
    lines+=['','## Outcome links (pending)']+[f'- {k}: {v.isoformat()} — append-only outcome; no future value collected.' for k,v in journal.outcome_due.items()]
    lines+=['','## Completion blockers']+[f'- {b}' for b in journal.completion_blockers]
    return '\n'.join(lines)+'\n'


def attach_outcome(path,*,run_id,journal_sha256,due_at,observed_at,collected_at,price,source_ref):
    if observed_at<due_at:raise ValueError('outcome observed before due time')
    if collected_at<observed_at or collected_at>datetime.now(UTC):raise ValueError('outcome future/collection chronology')
    if price<=0 or not source_ref:raise ValueError('outcome requires real positive price and provenance')
    value=dict(run_id=run_id,journal_sha256=journal_sha256,data_mode='live_forward',due_at=due_at.isoformat(),
        observed_at=observed_at.isoformat(),collected_at=collected_at.isoformat(),price=price,source_ref=source_ref)
    write_immutable(path,value)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=('collect','replay','verify'))
    p.add_argument('--output',type=Path,default=Path('artifacts/local/live'));p.add_argument('--journal',type=Path)
    args=p.parse_args()
    if args.command=='collect':
        snapshot=collect_snapshot();folder=args.output/str(snapshot.snapshot_id)
        write_immutable(folder/'raw-snapshot.json',snapshot)
        journal=evaluate(snapshot);sealed=SealedLive.seal(journal);write_immutable(folder/'prediction-journal.json',sealed)
        report=explain(journal);report_path=folder/'explainability.md'
        with report_path.open('x',encoding='utf-8',newline='\n') as stream:stream.write(report)
        write_immutable(folder/'outcome-schedule.json',{'run_id':str(journal.run.run_id),'journal_sha256':sealed.sha256,
            'pending':{k:v.isoformat() for k,v in journal.outcome_due.items()}})
        print(json.dumps({'journal':str(folder/'prediction-journal.json'),'sha256':sealed.sha256,'run_id':str(journal.run.run_id),
            'blockers':journal.completion_blockers,'sources':[(s.source_id,s.status,s.rows) for s in journal.source_status]},indent=2))
    else:
        if args.journal is None:p.error('--journal is required')
        sealed=SealedLive.model_validate_json(args.journal.read_text(encoding='utf-8'))
        if args.command=='replay' and evaluate(sealed.snapshot.raw_snapshot)!=sealed.snapshot:raise ValueError('raw replay mismatch; inspect versions')
        print(json.dumps({'valid':True,'replayed':args.command=='replay','sha256':sealed.sha256,'run_id':str(sealed.snapshot.run.run_id)}))


if __name__=='__main__':main()
