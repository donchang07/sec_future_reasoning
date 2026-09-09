"""Immutable aggregate journal: one sealed document for the entire execution."""
from pathlib import Path
from typing import Literal
from uuid import UUID
from pydantic import AwareDatetime, model_validator
from .schemas.contracts import Contract, VersionBundle, Forecast, Observation, canonical_hash, canonical_json, ENGINE_IDS, DataMode
from .schemas.artifacts import EngineResult, CausalPath
from .technical import TechnicalEvidence
from .decision import Decision
from .fixture import Fixture


class Execution(Contract):
    horizon: Literal['1w','1m','1y']
    generation: Literal[0,1]
    engine_id: str
    result: EngineResult


class HorizonOutput(Contract):
    horizon: Literal['1w','1m','1y']
    initial: Forecast | None
    final: Forecast | None
    positive_paths: tuple[CausalPath,...]
    negative_paths: tuple[CausalPath,...]
    technical: TechnicalEvidence
    decision: Decision
    explanation: str


class RunJournal(Contract):
    schema_version: Literal['1.0.0','1.1.0'] = '1.1.0'
    data_mode: DataMode = 'synthetic_fixture'
    run_id: UUID
    data_cutoff: AwareDatetime
    versions: VersionBundle
    fixture_hash: str
    source_hash: str
    input_fixture: Fixture
    observations: tuple[Observation,...]
    horizons: tuple[HorizonOutput,...]
    executions: tuple[Execution,...]

    @model_validator(mode='after')
    def verify_structure(self):
        if self.schema_version=='1.0.0':
            if self.data_mode!='synthetic_fixture' or self.input_fixture.data_mode!='synthetic_fixture':
                raise ValueError('legacy journal cannot acquire a real data mode')
            for o in self.observations+self.input_fixture.observations:
                if o.collected_at is not None or o.released_at is not None or o.effective_at is not None or o.source_ref is not None:
                    raise ValueError('legacy journal cannot acquire unsealed provenance')
        fixture_hash=legacy_hash(self.input_fixture) if self.schema_version=='1.0.0' else canonical_hash(self.input_fixture)
        if fixture_hash!=self.fixture_hash or self.input_fixture.data_cutoff!=self.data_cutoff:
            raise ValueError('fixture identity mismatch')
        if self.input_fixture.data_mode!=self.data_mode or any(o.data_mode!=self.data_mode for o in self.observations):
            raise ValueError('mixed data mode in journal')
        expected={(h,g,e) for h in ('1w','1m','1y') for g in (0,1) for e in ENGINE_IDS}
        actual=[(r.horizon,r.generation,r.engine_id) for r in self.executions]
        if len(actual)!=114 or set(actual)!=expected: raise ValueError('execution matrix incomplete')
        if len(self.horizons)!=3 or {h.horizon for h in self.horizons}!={'1w','1m','1y'}:raise ValueError('horizon set')
        seen=set();versions={e.engine_id:e.version for e in self.versions.engines}
        for r in self.executions:
            a=r.result.output_artifact
            if a is None:continue
            if a.run_id!=self.run_id or a.data_cutoff!=self.data_cutoff or a.engine_id!=r.engine_id:
                raise ValueError('artifact identity mismatch')
            if a.engine_version!=versions[a.engine_id]:raise ValueError('engine version mismatch')
            if a.artifact_id in seen or not set(a.input_artifact_ids)<=seen:raise ValueError('artifact reference order')
            seen.add(a.artifact_id)
        for h in self.horizons:
            for generation,f in ((0,h.initial),(1,h.final)):
                r=next(r for r in self.executions if (r.horizon,r.generation,r.engine_id)==(h.horizon,generation,'E18'))
                actual_forecast=r.result.output_artifact.payload.forecast if r.result.output_artifact else None
                if f!=actual_forecast:raise ValueError('forecast does not match engine artifact')
                if f and (f.versions!=self.versions or f.run_id!=self.run_id or f.horizon!=h.horizon):raise ValueError('forecast versions/identity')
            from .decision import decide
            f=h.final;t=h.technical;w=t.wave
            meta=next(r.result.output_artifact.payload for r in self.executions if (r.horizon,r.generation,r.engine_id)==(h.horizon,1,'E19'))
            decision=decide(up=f.probabilities.up if f else None,down=f.probabilities.down if f else None,
                no_history_up=f.without_history_probabilities.up if f else None,no_history_down=f.without_history_probabilities.down if f else None,
                confidence=f.confidence if f else None,bottom=w.bottom_score,top=w.top_score,bottom_confirmed=w.bottom_confirmed,
                top_confirmed=w.top_confirmed,bullish_alignment=t.bullish_alignment,bearish_alignment=t.bearish_alignment,
                buy_liquidity=t.buy_liquidity,sell_liquidity=t.sell_liquidity,fatal=not meta.publishable,held=self.input_fixture.held)
            if h.decision!=decision:raise ValueError('decision does not match independent policy gates')
        if any(o.available_at>self.data_cutoff for o in self.observations):raise ValueError('future observation')
        return self


class SealedRun(Contract):
    snapshot: RunJournal
    sha256: str

    @model_validator(mode='after')
    def verify(self):
        expected=legacy_hash(self.snapshot) if self.snapshot.schema_version=='1.0.0' else canonical_hash(self.snapshot)
        if self.sha256!=expected:raise ValueError('journal hash mismatch')
        return self

    @classmethod
    def seal(cls,snapshot):return cls(snapshot=snapshot,sha256=canonical_hash(snapshot))


def write_journal(path: Path,journal: SealedRun):
    # Validate before exclusive creation; never truncate an existing snapshot.
    checked=SealedRun.model_validate_json(journal.model_dump_json())
    content=(canonical_json(checked)+'\n').encode('utf-8')
    path.parent.mkdir(parents=True,exist_ok=True)
    try:
        with path.open('xb') as stream:stream.write(content)
    except FileExistsError:
        if path.read_bytes()!=content:raise ValueError('immutable journal already exists with different content')


def read_journal(path: Path):return SealedRun.model_validate_json(path.read_text(encoding='utf-8'))


def legacy_hash(model):
    """Verify original 1.0 bytes without rewriting or resealing the old snapshot."""
    import hashlib,json
    new_fields={'data_mode','released_at','collected_at','effective_at','source_ref','market_timezone','time_precision'}
    def strip(value):
        if isinstance(value,dict):return {k:strip(v) for k,v in value.items() if k not in new_fields}
        if isinstance(value,list):return [strip(v) for v in value]
        return value
    raw=strip(json.loads(canonical_json(model)))
    return hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
