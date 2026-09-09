"""Baseline engines -> technical evidence -> exactly one feedback pass -> journal."""
import hashlib
import subprocess
from pathlib import Path
from .fixture import Fixture
from .engines import EngineRunner, uid
from .technical import technical_evidence
from .decision import decide
from .journal import RunJournal, Execution, HorizonOutput
from .schemas.contracts import VersionBundle, EngineVersion, ENGINE_IDS, canonical_hash


def source_identity():
    root=Path(__file__).resolve().parents[1]
    digest=hashlib.sha256()
    for p in sorted((root/'reasoning').rglob('*.py')):
        digest.update(p.relative_to(root).as_posix().encode());digest.update(p.read_text(encoding='utf-8').encode())
    commit=subprocess.check_output(['git','log','-1','--format=%H','--','reasoning'],cwd=root,text=True).strip()
    return digest.hexdigest(),commit


def run_fixture(fixture: Fixture, runner_class=EngineRunner) -> RunJournal:
    source_hash,commit=source_identity();fixture_hash=canonical_hash(fixture)
    graph_hash=hashlib.sha256(''.join(e.model_dump_json() for e in fixture.edges).encode()).hexdigest()
    model=f'slice-v1:{source_hash}'
    versions=VersionBundle(ontology='ontology-design-v2',graph=f'fixture-dag-v1:{graph_hash}',model=model,
        prompt='event-grammar-v1',calibration='temperature-1.15-unvalidated-v1',policy='entry80-sell70-v1',
        source_registry=fixture.fixture_version,calendar='synthetic-closed-bars-v1',code_commit=commit,
        engines=tuple(EngineVersion(engine_id=e,version=model) for e in ENGINE_IDS))
    run_id=uid(f'{fixture_hash}/{canonical_hash(versions)}');records=[];horizons=[]
    for horizon in ('1w','1m','1y'):
        baseline=runner_class(fixture,versions,run_id,horizon,0)
        for engine in ENGINE_IDS:records.append(Execution(horizon=horizon,generation=0,engine_id=engine,result=baseline.execute(engine)))
        technical=technical_evidence(fixture,horizon,run_id)
        final=runner_class(fixture,versions,run_id,horizon,1,technical)
        for engine in ENGINE_IDS:records.append(Execution(horizon=horizon,generation=1,engine_id=engine,result=final.execute(engine)))
        initial_forecast=baseline.get('E18').forecast if 'E18' in baseline.artifacts else None
        forecast=final.get('E18').forecast if 'E18' in final.artifacts else None
        meta=final.get('E19');w=technical.wave
        p=forecast.probabilities if forecast else None;shadow=forecast.without_history_probabilities if forecast else None
        decision=decide(up=p.up if p else None,down=p.down if p else None,no_history_up=shadow.up if shadow else None,
            no_history_down=shadow.down if shadow else None,confidence=forecast.confidence if forecast else None,
            bottom=w.bottom_score,top=w.top_score,bottom_confirmed=w.bottom_confirmed,top_confirmed=w.top_confirmed,
            bullish_alignment=technical.bullish_alignment,bearish_alignment=technical.bearish_alignment,
            buy_liquidity=technical.buy_liquidity,sell_liquidity=technical.sell_liquidity,fatal=not meta.publishable,held=fixture.held)
        adjusted={p.path_id:p.adjusted_effect for p in final.get('E09').items}
        paths=sorted(final.get('E08').items,key=lambda p:-abs(adjusted[p.path_id]))
        positive=tuple(p for p in paths if adjusted[p.path_id]>0)[:5];negative=tuple(p for p in paths if adjusted[p.path_id]<0)[:5]
        explanation=(f'{horizon}: up={p.up:.6f}, down={p.down:.6f}, flat={p.flat:.6f}; confidence={forecast.confidence:.6f}. '
            f'{len(forecast.ledger)} ledger steps reconstruct final probability. ' if p else f'{horizon}: insufficient_evidence. ')
        explanation+=f'One technical feedback pass; {decision.action}; gates: {", ".join(decision.reasons)}. Research fixture, unvalidated calibration.'
        horizons.append(HorizonOutput(horizon=horizon,initial=initial_forecast,final=forecast,positive_paths=positive,
            negative_paths=negative,technical=technical,decision=decision,explanation=explanation))
    return RunJournal(data_mode=fixture.data_mode,run_id=run_id,data_cutoff=fixture.data_cutoff,versions=versions,fixture_hash=fixture_hash,source_hash=source_hash,
        input_fixture=fixture,observations=tuple(o for o in fixture.observations if o.available_at<=fixture.data_cutoff),horizons=tuple(horizons),executions=tuple(records))
