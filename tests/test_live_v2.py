"""Pre-forward integration gates; exclusively synthetic/offline inputs."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import pytest
from reasoning.fixture import Fixture
from reasoning.schemas.contracts import canonical_hash
from reasoning.live_v2 import (run_mapped, market_semantics, digest, seal, verify_seal,
    outcome_due, append_outcome, reference_price, file_hashes, verify_lock)

ROOT=Path(__file__).resolve().parents[1]


def inputs():
    f=Fixture.model_validate_json((ROOT/'fixtures/samsung-preferred-v1.json').read_text())
    # No synthetic accounting is migrated into company consolidated financial evidence.
    f=f.model_copy(update={'events':(), 'history':(), 'accounting':None})
    sources,priors=market_semantics(f)
    return f,sources,priors


def run(f=None,sources=None):
    original,obs,_=inputs()
    return run_mapped(f or original,obs if sources is None else sources,{'code_commit':'0'*40,'files':{'offline':'test'}})


def test_114_invocations_one_feedback_and_determinism():
    a=run();b=run()
    assert digest(a)==digest(b)
    assert len(a['executions'])==114
    assert {e['generation'] for e in a['executions']}=={0,1}
    assert all(h['feedback_passes']==1 for h in a['horizons'])


def test_horizon_withholding_no_fabricated_candidate():
    result=run(sources=())
    assert all(h['final'] is None and h['initial'] is None for h in result['horizons'])
    assert all('hard_missing:samsung_preferred_price' in h['assessment']['reasons'] for h in result['horizons'])


def test_value_only_is_not_direction():
    f,sources,_=inputs()
    sources=tuple(s.model_copy(update={'prior_value':None}) for s in sources)
    result=run(f,sources)
    e01=result['executions'][0]['result']['output_artifact']['payload']
    assert e01['items'] and all(x['normalized'] is None for x in e01['items'])
    assert not result['executions'][7]['result']['output_artifact']['payload']['items']


def test_legacy_normalization_unchanged_for_admitted_direction():
    f,sources,_=inputs(); result=run(f,sources)
    specs={s.factor_id:s for s in f.factors}
    rows=result['executions'][0]['result']['output_artifact']['payload']['items']
    for x in rows:
        if x['normalized'] is not None:
            s=specs[x['factor_id']]
            assert x['normalized']==max(-1.,min(1.,(x['level']-s.baseline)/s.scale))


def test_prior_provenance_is_actual_previous_observation():
    f,sources,priors=inputs()
    assert priors
    for row in priors:
        assert row['prior_effective_at'] < row['effective_at']
        assert any(o.value==row['prior_value'] and o.observed_at.isoformat()==row['prior_effective_at'] for o in f.observations)


def test_liquidity_unavailable_blocks_entry():
    f,sources,_=inputs()
    f=f.model_copy(update={'observations':tuple(o for o in f.observations if o.factor_id not in ('foreign_net_buy','institution_net_buy','program_net_buy'))})
    sources=tuple(s for s in sources if s.source_field not in ('foreign_net_buy','institution_net_buy','program_net_buy'))
    for h in run(f,sources)['horizons']:
        assert h['technical']['buy_liquidity'] is None
        assert h['decision']['action']=='WAIT' and 'liquidity' in h['decision']['reasons']


def test_ledger_reconstructs_and_post_coverage_does_not_change_probability():
    result=run(); count=0
    for h in result['horizons']:
        for key in ('initial','final'):
            if h[key]:
                f=h[key]; p=f['prior']; count+=1
                for row in f['ledger']:
                    assert row['before']==p
                    p=row['after']
                assert p==f['probabilities']
    assert count>0


def test_layered_missing_constraints_non_applicable():
    for h in run()['horizons']:
        assert h['assessment']['constraints']['memory']['status']=='non_applicable'
        assert h['assessment']['constraints']['industry']['status']=='non_applicable'


def test_seal_tamper_and_exclusive_write(tmp_path):
    from reasoning.live import write_immutable
    value=seal({'run_id':'offline'})
    verify_seal(value);write_immutable(tmp_path/'journal.json',value)
    with pytest.raises(ValueError):write_immutable(tmp_path/'journal.json',seal({'run_id':'changed'}))
    value['snapshot']['run_id']='changed'
    with pytest.raises(ValueError):verify_seal(value)


def test_lock_detects_drift(tmp_path):
    (tmp_path/'reasoning').mkdir();(tmp_path/'reasoning/a.py').write_text('a=1')
    hashes=file_hashes(tmp_path)
    (tmp_path/'reasoning/a.py').write_text('a=2')
    with pytest.raises(ValueError,match='drift'):verify_lock({'files':hashes},tmp_path,environment=False)


def test_reference_price_uses_closed_latest_bar():
    f,_,_=inputs();p=reference_price(f)
    assert p['value']==f.bars['30m'][-1].close
    assert p['effective_at']==f.bars['30m'][-1].closed_at.isoformat()


def test_annual_outcome_leap_day_and_append_identity(tmp_path):
    t=datetime(2024,2,29,tzinfo=timezone.utc);due=outcome_due(t)
    assert due['1y']==datetime(2025,2,28,tzinfo=timezone.utc).isoformat()
    journal=seal({'run_id':'test','outcome_due':due,'p0':{'value':100.}})
    outcome={'horizon':'1d','price':110.,'effective_at':due['1d'],'collected_at':due['1d'],'source_ref':'raw:actual-test'}
    append_outcome(tmp_path,journal,outcome)
    with pytest.raises(ValueError):append_outcome(tmp_path,journal,{**outcome,'price':120.})
    with pytest.raises(ValueError):append_outcome(tmp_path,journal,{**outcome,'effective_at':t.isoformat()})


def financial_sources(f,wrong=False):
    from reasoning.refinement.types import SourceObservation
    t=f.data_cutoff-timedelta(days=1)
    values={'samsung_total_assets':300.,'samsung_total_liabilities':110. if wrong else 100.,
        'samsung_total_equity':200.,'samsung_revenue':100.,'samsung_operating_profit':10.,'samsung_operating_cash':20.}
    return tuple(SourceObservation(source_id='authored',source_field=k,source_unit='krw_million',value=v,
        economic_scope='company_consolidated',series_id=k,observed_at=t,effective_at=t,released_at=None,
        collected_at=f.data_cutoff,data_mode='synthetic_fixture',raw_ref='synthetic:'+k,reporting_period='2026-H1') for k,v in values.items())


@pytest.mark.parametrize('wrong',[False,True])
def test_e11_company_projection_and_fail_closed(wrong):
    f,sources,_=inputs();j=run(f,sources+financial_sources(f,wrong))
    for h in j['horizons']:
        assert h['assessment']['constraints']['company']['status']==('failed' if wrong else 'passed')
        if wrong:assert h['final'] is None and 'E11_constraint_failure' in h['assessment']['reasons']
    e11=j['executions'][10]['result']['output_artifact']['payload']['items']
    assert len(e11)==1 and e11[0]['constraint_id']=='company_balance_sheet'


def test_unsupported_directional_graph_route_is_not_aliased():
    from reasoning.refinement.types import SourceObservation
    f,sources,_=inputs();t=f.data_cutoff-timedelta(days=1)
    spot=SourceObservation(source_id='authored',source_field='dram_spot_test',source_unit='usd_per_chip',value=12.,
        prior_value=10.,economic_scope='memory_spot',series_id='sku',observed_at=t,effective_at=t,released_at=None,
        collected_at=f.data_cutoff,data_mode='synthetic_fixture',raw_ref='synthetic:spot')
    j=run(f,sources+(spot,))
    row=next(x for x in j['horizons'][0]['dispositions'] if x['factor_id']=='dram_spot_price')
    assert row['status']=='directional_no_frozen_graph_route' and not row['path_ids']


def test_raw_bundle_replay_and_complete_candles():
    from test_real_data import response,NOW
    from reasoning.live import ModelProfile,RawSnapshot
    from reasoning.live_v2 import InputBundle,evaluate
    from reasoning.engines import uid
    points=[NOW-timedelta(days=2),NOW-timedelta(days=1),NOW]
    raw=response(points)
    profile=ModelProfile.model_validate_json((ROOT/'config/live-model-profile.json').read_text())
    market=RawSnapshot(snapshot_id=uid('authored-v2'),data_mode='synthetic_fixture',prediction_timestamp=NOW,
        data_cutoff=NOW,sources=(raw,),profile=profile)
    bundle=InputBundle(market=market,documents=(),lock={'code_commit':'0'*40,'files':{'offline':'test'}})
    a=evaluate(bundle);b=evaluate(InputBundle.model_validate_json(bundle.model_dump_json()))
    assert digest(a)==digest(b)
    assert a['data_mode']=='synthetic_fixture'
    assert a['bar_boundaries']['1d']['count']<=3
    assert a['bar_boundaries']['1mo']['count']==0


def test_future_semantic_observation_does_not_enter_engine():
    f,sources,_=inputs()
    future=tuple(s.model_copy(update={'collected_at':f.data_cutoff+timedelta(days=1)}) for s in sources)
    j=run(f,future)
    assert not j['executions'][0]['result']['output_artifact']['payload']['items']
    assert all(h['final'] is None for h in j['horizons'])
