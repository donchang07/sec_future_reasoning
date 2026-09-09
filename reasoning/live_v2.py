"""Frozen-contract forward orchestration. No coefficient or legacy source edits."""
import argparse
import calendar
import hashlib
import importlib.metadata
import json
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Literal
from pydantic import model_validator
from .act_sources import DOCUMENTS, Document, assess, collect_document
from .live import ROOT, RawSnapshot, collect_snapshot, prepare, write_immutable
from .market_data import parse_yahoo
from .engines import EngineRunner, uid
from .technical import technical_evidence
from .decision import decide
from .journal import Execution
from .schemas.contracts import Contract, VersionBundle, EngineVersion, ENGINE_IDS
from .schemas.artifacts import EngineResult, Warning
from .refinement.types import SourceObservation, Candidate, CONTRACT_VERSION, MAPPING_VERSION
from .refinement.mapping import map_observations
from .refinement.assessment import assess_contract, publish_candidate
from .refinement.audit import source_from_fact, verify_manifest
from .refinement.registry import MATRIX, scope_for

UTC=timezone.utc
HORIZONS=('1w','1m','1y')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def seal(value):return {'snapshot':value,'sha256':digest(value)}


def verify_seal(value):
    if digest(value['snapshot'])!=value['sha256']:raise ValueError('journal seal mismatch')
    return value['snapshot']


def file_hashes(root=ROOT):
    files=[]
    for directory in ('reasoning','config','ontology','tests','packages'):
        files.extend(p for p in (root/directory).rglob('*') if p.suffix in ('.py','.json','.yaml','.yml') and '__pycache__' not in p.parts)
    files.extend(p for p in (root/'requirements.lock',root/'pyproject.toml') if p.exists())
    return {p.relative_to(root).as_posix():hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest() for p in sorted(files)}


def runtime():
    return {'python':platform.python_version(),'packages':{p:importlib.metadata.version(p) for p in ('pydantic','pydantic-core','pypdf','tzdata')}}


def verify_lock(lock,root=ROOT,environment=True):
    if file_hashes(root)!=lock['files']:raise ValueError('frozen executable drift')
    if environment and runtime()!=lock['runtime']:raise ValueError('frozen runtime drift')
    if environment:
        verify_manifest(root/'config/contracts/real-world-contract-v2.0.0.json')
        for name,sha in lock.get('historical_journals',{}).items():
            if hashlib.sha256((root/name).read_bytes()).hexdigest()!=sha:raise ValueError('historical journal drift')


def make_lock():
    verify_manifest(ROOT/'config/contracts/real-world-contract-v2.0.0.json')
    scope=['reasoning','config','ontology','tests','packages','requirements.lock','pyproject.toml']
    if subprocess.check_output(['git','status','--porcelain','--',*scope],cwd=ROOT,text=True).strip():
        raise ValueError('commit executable files before freeze')
    old={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
         for p in sorted((ROOT/'artifacts/local/live').glob('*/prediction-journal.json'))}
    return {'feature':'live-forward-v2','frozen_at':datetime.now(UTC).isoformat(),
        'code_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'contract_version':CONTRACT_VERSION,'mapping_version':MAPPING_VERSION,
        'requirement_matrix_version':'economic-bucket-quorum-v1','ontology_version':'ontology-design-v2',
        'engine_adapter_version':'live-v2-adapter-v1','entry':.80,'sell':.70,
        'files':file_hashes(),'runtime':runtime(),'historical_journals':old}


class InputBundle(Contract):
    schema_version: Literal['live-v2-raw-1']='live-v2-raw-1'
    market: RawSnapshot
    documents: tuple[Document,...]
    lock: dict

    @model_validator(mode='after')
    def boundary(self):
        if self.documents and self.market.data_mode!='live_forward':raise ValueError('mixed documentary mode')
        if len({d.source_id for d in self.documents})!=len(self.documents):raise ValueError('duplicate document source')
        if any(d.collected_at>self.market.data_cutoff for d in self.documents):raise ValueError('document after cutoff')
        if 'frozen_at' in self.lock:
            frozen=datetime.fromisoformat(self.lock['frozen_at'])
            if any(r.requested_at<frozen for r in (*self.market.sources,*self.documents)):
                raise ValueError('collection preceded freeze')
        return self


def market_semantics(fixture):
    groups={};sources=[];priors=[]
    for o in fixture.observations:
        if o.available_at<=fixture.data_cutoff:groups.setdefault((o.factor_id,o.source_id),[]).append(o)
    for (fid,sid),rows in sorted(groups.items()):
        rows=sorted(rows,key=lambda o:(o.observed_at,o.available_at,str(o.observation_id)))
        for o in rows:
            previous=[p for p in rows if p.observed_at<o.observed_at]
            prior=previous[-1] if previous else None
            scope=scope_for(fid) if fid in MATRIX else 'unknown'
            # Every row has a unique point reference into an immutable raw series.
            ref=(o.source_ref or 'synthetic:'+str(o.observation_id))+'#'+fid+'@'+o.observed_at.isoformat()
            sources.append(SourceObservation(source_id=sid,source_field=fid,source_unit=o.unit,value=o.value,
                economic_scope=scope,series_id=fid,observed_at=o.observed_at,effective_at=o.effective_at or o.observed_at,
                released_at=o.released_at,collected_at=o.collected_at or o.available_at,data_mode=o.data_mode,
                raw_ref=ref,prior_value=prior.value if prior else None))
            if prior:priors.append({'source_ref':ref,'effective_at':o.observed_at.isoformat(),'prior_value':prior.value,
                'prior_effective_at':prior.observed_at.isoformat(),'prior_observation_id':str(prior.observation_id)})
    return tuple(sources),priors


def admitted_fixture(fixture,sources,batch):
    # Historical rows need their own semantic validation; a valid latest row must
    # never admit an older conflicting/unit-invalid row by association.
    valid=set()
    for source in sources:
        single=map_observations((source,),fixture.data_cutoff,batch.horizon,'unknown')
        if single.evidence:valid.add((source.source_field,source.source_id,source.effective_at,source.value))
    present={e.factor_id for e in batch.evidence}
    observations=tuple(o for o in fixture.observations if o.factor_id in present and
        (o.factor_id,o.source_id,o.effective_at or o.observed_at,o.value) in valid)
    return fixture.model_copy(update={'observations':observations,'events':(),'history':(),'accounting':None})


class V2Runner(EngineRunner):
    """Only semantic eligibility and contract boundaries differ from v1."""
    @property
    def specs(self):
        return {s.factor_id:s.model_copy(update={'critical':False}) for s in self.fixture.factors}

    def E01(self):
        values=super().E01()
        directional={e.factor_id for e in self.batch.evidence if e.signal is not None}
        for row in values['items']:
            if row['factor_id'] not in directional:row['normalized']=None
        return values

    def factor_effects(self):
        return {fid:s.normalized*self.specs[fid].sign for fid,s in self.signals.items() if s.normalized is not None}

    def E11(self):
        items=[]
        for domain in ('company','memory','industry'):
            for check in getattr(self.assessment.constraints,domain).checks:
                if check.status=='non_applicable':continue
                items.append(dict(target_id='samsung',constraint_id=domain+'_'+check.name,lhs=check.lhs,rhs=check.rhs,
                    tolerance=.01,valid=check.status=='passed',evidence_refs=check.source_refs or (domain+':'+check.name,)))
        return dict(items=items)

    def E18(self):
        values=super().E18();forecast=values['forecast']
        publication=publish_candidate(Candidate(probabilities=forecast.probabilities,confidence=forecast.confidence,
            horizon=self.horizon,data_cutoff=self.fixture.data_cutoff,data_mode=self.fixture.data_mode),self.assessment)
        values['forecast']=forecast.model_copy(update={'confidence':publication.confidence})
        return values

    def execute(self,engine):
        if engine=='E18' and not self.assessment.eligible:
            return EngineResult(status='insufficient_evidence',trace_id=self.ident(engine+'/trace'),
                warnings=(Warning(code='v2_coverage_withheld',message='; '.join(self.assessment.reasons),
                    evidence_refs=self.assessment.hard_missing or self.assessment.reasons),))
        result=super().execute(engine)
        if engine=='E01':
            warnings=result.warnings+(Warning(code='v2_coverage',message='Coverage assessed before probability; confidence penalty applied at publication',
                evidence_refs=self.assessment.strong_missing or ('v2:coverage_complete',)),)
            result=result.model_copy(update={'warnings':warnings})
        return result


def reference_price(fixture):
    for timeframe in ('30m','1d'):
        bars=[b for b in fixture.bars.get(timeframe,()) if b.closed_at<=fixture.data_cutoff]
        if bars:
            b=bars[-1]
            refs=sorted({o.source_ref for o in fixture.observations if o.factor_id=='samsung_preferred_price' and o.source_ref})
            return {'value':b.close,'unit':'krw_per_share','timeframe':timeframe,'effective_at':b.closed_at.isoformat(),
                'definition':'last eligible completed close, not execution quote','source_refs':refs}
    return None


def outcome_due(date):
    month=date.month%12+1;year=date.year+(date.month==12)
    return {'1d':(date+timedelta(days=1)).isoformat(),'1w':(date+timedelta(days=7)).isoformat(),
        '1m':date.replace(year=year,month=month,day=min(date.day,calendar.monthrange(year,month)[1])).isoformat(),
        '1y':date.replace(year=date.year+1,day=min(date.day,calendar.monthrange(date.year+1,date.month)[1])).isoformat()}


def run_mapped(fixture,sources,lock):
    model='slice-v1:'+digest(lock['files'])
    graph_hash=hashlib.sha256(''.join(e.model_dump_json() for e in fixture.edges).encode()).hexdigest()
    versions=VersionBundle(ontology='ontology-design-v2',graph='fixture-dag-v1:'+graph_hash,model=model,
        prompt='event-grammar-v1',calibration='temperature-1.15-unvalidated-v1',policy='entry80-sell70-v1',
        source_registry='live-forward-v2',calendar='closed-market-bars-v1',code_commit=lock['code_commit'],
        engines=tuple(EngineVersion(engine_id=e,version='e11-real-world-v2.0.0' if e=='E11' else model) for e in ENGINE_IDS))
    run_id=uid(digest({'lock':lock,'fixture':fixture.model_dump(mode='json'),'sources':[s.model_dump(mode='json') for s in sources]}))
    executions=[];horizons=[]
    for horizon in HORIZONS:
        batch=map_observations(sources,fixture.data_cutoff,horizon,'unknown')
        assessment=assess_contract(batch,fixture.data_cutoff,horizon,fixture.data_mode)
        admitted=admitted_fixture(fixture,sources,batch)
        runners=[];technical=None
        for generation in (0,1):
            if generation:technical=technical_evidence(admitted,horizon,run_id)
            runner=V2Runner(admitted,versions,run_id,horizon,generation,technical)
            runner.batch=batch;runner.assessment=assessment
            for engine in ENGINE_IDS:
                executions.append(Execution(horizon=horizon,generation=generation,engine_id=engine,result=runner.execute(engine)).model_dump(mode='json'))
            runners.append(runner)
        initial,final=(r.get('E18').forecast if 'E18' in r.artifacts else None for r in runners)
        r=runners[1];p=final.probabilities if final else None;shadow=final.without_history_probabilities if final else None;w=technical.wave
        decision=decide(up=p.up if p else None,down=p.down if p else None,no_history_up=shadow.up if shadow else None,
            no_history_down=shadow.down if shadow else None,confidence=final.confidence if final else None,
            bottom=w.bottom_score,top=w.top_score,bottom_confirmed=w.bottom_confirmed,top_confirmed=w.top_confirmed,
            bullish_alignment=technical.bullish_alignment,bearish_alignment=technical.bearish_alignment,
            buy_liquidity=technical.buy_liquidity,sell_liquidity=technical.sell_liquidity,fatal=not r.get('E19').publishable,held=fixture.held)
        effects={x.path_id:x.effect for x in r.get('E12').items}
        paths=sorted(r.get('E08').items,key=lambda x:-abs(effects[x.path_id]))
        dispositions=[]
        for e in batch.evidence:
            path_ids=[x.path_id for x in paths if x.node_ids[0]==e.factor_id]
            signal=r.signals.get(e.factor_id)
            dispositions.append({'evidence_id':e.evidence_id,'factor_id':e.factor_id,'source_refs':list(e.source_refs),
                'semantic_signal':e.signal,'engine_normalized':signal.normalized if signal else None,'path_ids':path_ids,
                'status':'mapped_value_only' if e.signal is None else 'directional_with_path' if path_ids else 'directional_no_frozen_graph_route'})
        gates={'future_up','without_history_up','confidence','bottom_timing','alignment','liquidity','meta_check'} if not fixture.held else {'future_down','without_history_down','confidence','top_timing','alignment','liquidity','meta_check'}
        horizons.append({'horizon':horizon,'mapping':batch.model_dump(mode='json'),'assessment':assessment.model_dump(mode='json'),
            'dispositions':dispositions,'initial':initial.model_dump(mode='json') if initial else None,'final':final.model_dump(mode='json') if final else None,
            'feedback_passes':1,'feedback_delta_pp':[100*(b-a) for a,b in zip(initial.probabilities.vector(),final.probabilities.vector())] if initial and final else None,
            'feedback_reason':{'regime_effect':technical.regime_effect,'flow_effect':technical.flow_effect,'reflexivity_effect':technical.reflexivity_effect,
                'batch_id':technical.batch_id,'flow_applied':bool(r.get('E06').items[5].top_factors)},
            'positive_paths':[x.model_dump(mode='json') for x in paths if effects[x.path_id]>0][:5],
            'negative_paths':[x.model_dump(mode='json') for x in paths if effects[x.path_id]<0][:5],
            'technical':technical.model_dump(mode='json'),'decision':decision.model_dump(mode='json'),
            'passed_gates':sorted(gates-set(decision.reasons)),
            'what_would_change_my_mind':{'missing_coverage':list(assessment.reasons),'missing_strong':list(assessment.strong_missing),
                'failed_gates':list(decision.reasons),'falsifiers':[f.model_dump(mode='json') for h in r.get('E07').items for f in h.falsifiers]}})
    return {'run_id':str(run_id),'data_mode':fixture.data_mode,'contract_version':CONTRACT_VERSION,'mapping_version':MAPPING_VERSION,
        'versions':versions.model_dump(mode='json'),'prediction_timestamp':fixture.data_cutoff.isoformat(),'data_cutoff':fixture.data_cutoff.isoformat(),
        'held':fixture.held,'held_basis':'No actual holding supplied; unheld policy input','p0':reference_price(fixture),
        'outcome_due':outcome_due(fixture.data_cutoff),'horizons':horizons,'executions':executions}


def evaluate(bundle):
    fixture,statuses,availability=prepare(bundle.market)
    sources,priors=market_semantics(fixture)
    evidence=assess(bundle.documents,bundle.market.data_cutoff)
    sources=list(sources)+[source_from_fact(f) for f in evidence.facts]
    for raw in bundle.market.sources:
        if raw.source.source_id not in ('kospi','dxy') or raw.status!='available':continue
        bars,_=parse_yahoo(raw,bundle.market.data_cutoff)
        if bars:
            b=bars[-1]
            sources.append(SourceObservation(source_id=raw.source.source_id,source_field=raw.source.source_id,source_unit=raw.source.unit,
                value=b.close,economic_scope='market',series_id=raw.source.source_id,observed_at=b.closed_at,effective_at=b.closed_at,
                released_at=None,collected_at=raw.collected_at,data_mode=raw.data_mode,raw_ref='raw:'+raw.sha256))
    output=run_mapped(fixture,tuple(sources),bundle.lock)
    if output['p0']:
        sid='preferred_30m' if output['p0']['timeframe']=='30m' else 'preferred_daily'
        output['p0']['source_refs']=['raw:'+r.sha256 for r in bundle.market.sources if r.source.source_id==sid]
    output.update(raw_bundle_hash=digest(bundle.model_dump(mode='json')),lock=bundle.lock,
        sources=[s.model_dump(mode='json') for s in statuses],document_status=evidence.source_status,
        raw_observations=[s.model_dump(mode='json') for s in sources],prior_provenance=priors,
        bar_boundaries={k:{'count':len(v),'last':v[-1].closed_at.isoformat() if v else None} for k,v in fixture.bars.items()},
        findings=['Mapped new families with no frozen graph route do not contribute direction.',
                  'Original level normalization is unchanged; semantic change is an eligibility gate, not its sign.',
                  'Coverage can include value-only evidence; confidence and probability are distinct.',
                  'Calibration is unvalidated; reversal scores are not calibrated probabilities.'])
    return output


def append_outcome(folder,journal,outcome):
    j=verify_seal(journal);h=outcome['horizon'];due=datetime.fromisoformat(j['outcome_due'][h])
    effective=datetime.fromisoformat(outcome['effective_at']);collected=datetime.fromisoformat(outcome['collected_at'])
    if effective<due or effective>collected or collected>datetime.now(UTC) or outcome['price']<=0 or not outcome['source_ref']:
        raise ValueError('invalid forward outcome chronology/provenance')
    if not j['p0']:raise ValueError('P0 unavailable')
    record={**outcome,'run_id':j['run_id'],'journal_sha256':journal['sha256'],'return':outcome['price']/j['p0']['value']-1}
    write_immutable(folder/(h+'.json'),record)


def report(j):
    lines=['# live-forward-v2 — sealed forward evidence','',f"Run: {j['run_id']}",f"Cutoff / prediction: {j['data_cutoff']}",
        f"Contract: {j['contract_version']}; mapping: {j['mapping_version']}",f"P0: {j['p0']}",'',
        '| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |',
        '|---|---:|---:|---:|---:|---:|---:|---|---|---|']
    pct=lambda x:'—' if x is None else f'{100*x:.4f}%'
    for h in j['horizons']:
        f=h['final'];p=f['probabilities'] if f else {};t=h['technical'];w=t['wave']
        lines.append('| '+' | '.join([h['horizon'],*[pct(p.get(k)) for k in ('up','down','flat')],pct(f['confidence'] if f else None),
            pct(w['bottom_score']),pct(w['top_score']),str(t['bullish_alignment'])+'/'+str(t['bearish_alignment']),
            str(t['buy_liquidity'])+'/'+str(t['sell_liquidity']),h['decision']['action']])+' |')
    lines+=['','## Feedback probability (Up / Down / Flat)','| Horizon | Before | After | Delta pp |','|---|---|---|---|']
    for h in j['horizons']:
        vector=lambda f: 'insufficient_evidence' if f is None else ' / '.join(pct(f['probabilities'][k]) for k in ('up','down','flat'))
        lines.append(f"| {h['horizon']} | {vector(h['initial'])} | {vector(h['final'])} | {h['feedback_delta_pp']} |")
    lines+=['','## Sources / freshness','```json',json.dumps(j.get('sources',[]),indent=2),'```',
        'Document statuses: '+str(j.get('document_status',{})), 'Bar boundaries: '+str(j.get('bar_boundaries',{})),
        'Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.']
    for h in j['horizons']:
        a=h['assessment'];t=h['technical'];w=t['wave']
        lines+=['',f"## {h['horizon']}",f"Eligibility: {a['eligible']}; reasons: {a['reasons']}",
            f"Coverage: {a['coverage']}; confidence multiplier: {a['confidence_multiplier']}",
            f"Confidence-lowering Strong Evidence: {a['strong_missing']}",f"Unmapped/conflicting evidence: {h['mapping']['unmapped']}",
            f"E11: company={a['constraints']['company']['status']}, memory={a['constraints']['memory']['status']}, industry={a['constraints']['industry']['status']}",
            f"Primary/context: {t['primary']}/{t['higher']}",'```json',json.dumps(t,indent=2),'```',
            f"Passed gates: {h['passed_gates']}; failed gates: {h['decision']['reasons']}",
            'Feedback applied once: '+str(h['feedback_reason']),
            'Memory module state (coverage/semantic diagnostic, no invented graph route): '+str(a['memory'])]
        for label in ('positive_paths','negative_paths'):
            lines+=['',label+' (up to five; never padded)','```json',json.dumps(h[label],indent=2),'```']
        lines+=['','### Probability contribution reconstruction']
        if h['final']:
            f=h['final'];lines+=['Prior: '+str(f['prior']),'| Sequence | Engine/stage | Evidence | Before | Delta pp | After |','|---|---|---|---|---|---|']
            for c in f['ledger']:
                lines.append(f"| {c['sequence']} | {c['engine_id']}/{c['stage']} | {c['evidence_refs']} | {c['before']} | {c['delta_pp']} | {c['after']} |")
            lines.append('E09 duplicate-root interaction adjustment precedes these causal steps. E10 reflexivity, E17 scenario, E14 challenger, E13 historical and E18 calibration steps are explicit; no additional hidden adjustment.')
        else:lines.append('Probability withheld. No prior is relabeled as a forecast; no numeric feedback delta exists.')
        lines+=['','### What Would Change My Mind','```json',json.dumps(h['what_would_change_my_mind'],indent=2),'```',
            'Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.']
    lines+=['','## Findings for the next PDCA']+['- '+x for x in j.get('findings',[])]
    return '\n'.join(lines)+'\n'


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=('freeze','collect','replay','verify','outcome'))
    p.add_argument('--lock',type=Path);p.add_argument('--journal',type=Path);p.add_argument('--outcome',type=Path)
    p.add_argument('--output',type=Path,default=ROOT/'artifacts/local/live-v2')
    args=p.parse_args()
    if args.command=='freeze':
        lock=make_lock();write_immutable(args.lock,seal(lock));print('lock_sha256='+digest(lock));return
    if args.command=='collect':
        lock=verify_seal(json.loads(args.lock.read_text(encoding='utf-8')));verify_lock(lock)
        with ThreadPoolExecutor(max_workers=4) as pool:documents=tuple(pool.map(collect_document,DOCUMENTS))
        market=collect_snapshot();bundle=InputBundle(market=market,documents=documents,lock=lock)
        folder=args.output/str(market.snapshot_id);write_immutable(folder/'raw-bundle.json',bundle)
        j=evaluate(bundle);verify_lock(lock);sealed=seal(j)
        write_immutable(folder/'prediction-journal.json',sealed)
        with (folder/'explainability.md').open('x',encoding='utf-8',newline='\n') as f:f.write(report(j))
        write_immutable(folder/'outcome-schedule.json',{'run_id':j['run_id'],'journal_sha256':sealed['sha256'],'p0':j['p0'],'pending':j['outcome_due'],
            'selection_rule':'first completed close on or after due time; separate immutable outcome files'})
        print(json.dumps({'journal':str(folder/'prediction-journal.json'),'run_id':j['run_id'],'sha256':sealed['sha256']}));return
    sealed=json.loads(args.journal.read_text(encoding='utf-8'));j=verify_seal(sealed)
    if args.command=='replay':
        verify_lock(j['lock']);bundle=InputBundle.model_validate_json((args.journal.parent/'raw-bundle.json').read_text(encoding='utf-8'))
        if digest(evaluate(bundle))!=sealed['sha256']:raise ValueError('raw replay mismatch')
        print('replay_equal=true; run_id='+j['run_id'])
    elif args.command=='outcome':append_outcome(args.journal.parent/'outcomes',sealed,json.loads(args.outcome.read_text(encoding='utf-8')))
    else:print('seal_valid=true; run_id='+j['run_id'])


if __name__=='__main__':main()
