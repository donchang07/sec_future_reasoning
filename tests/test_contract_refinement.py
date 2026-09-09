"""Ex-ante contract Golden cases. Synthetic observations; no live predictions."""
from datetime import datetime, timedelta, timezone
import pytest
from reasoning.refinement import (
    CONTRACT_VERSION, MappingPolicy, SourceObservation, Candidate, map_observations,
    assess_contract, publish_candidate, infer_memory, select_vintages, export_signals,
    evaluate_e11, Requirement, MATRIX, CompanyFinancials, MemoryBusiness, IndustrySupply,
)
from reasoning.schemas.contracts import ProbabilityVector

NOW = datetime(2026, 9, 9, tzinfo=timezone.utc)


def obs(field, value=1., unit='percent', scope='macro', **kwargs):
    if scope=='company_consolidated':kwargs.setdefault('reporting_period','2026-H1')
    return SourceObservation(source_id='authored_test', source_field=field, source_unit=unit, value=float(value),
        economic_scope=scope, series_id=field, observed_at=NOW-timedelta(days=1),
        effective_at=NOW-timedelta(days=1), released_at=NOW-timedelta(hours=1), collected_at=NOW,
        raw_ref='test:'+field, data_mode='synthetic_fixture', **kwargs)


def short_sources():
    return [obs('us_10y_yield', 4.), obs('usdkrw', 1350., 'krw_per_usd'),
        obs('samsung_preferred_price', 100., 'krw_per_share', 'market'),
        obs('preferred_trend_alignment', .5, 'score', 'market')]


def assessment(sources=None, horizon='1w', policy=None):
    mapped = map_observations(short_sources() if sources is None else sources, NOW, horizon, 'unknown', policy or MappingPolicy())
    return assess_contract(mapped, NOW, horizon, 'synthetic_fixture')


def candidate(horizon='1w'):
    return Candidate(probabilities=ProbabilityVector(up=.5, down=.3, flat=.2), confidence=.8,
        horizon=horizon, data_cutoff=NOW, data_mode='synthetic_fixture', contract_version=CONTRACT_VERSION)


def memory(field, current, prior):
    scopes = {'dram_contract_asp':'memory_contract','dram_spot_price':'memory_spot'}
    return obs(field, current, 'index' if field == 'dram_contract_asp' else 'usd_per_chip', scopes[field], prior_value=float(prior))


def export(month='2026-08', stage='nowcast_v2', value=200., yoy=20., **kwargs):
    from calendar import monthrange
    y,m=map(int,month.split('-'));days={'nowcast_v1':10,'nowcast_v2':20}.get(stage,monthrange(y,m)[1])
    effective=datetime(y,m,days,tzinfo=timezone.utc)
    return SourceObservation(source_id='authored_test',source_field='semiconductor_export_demand',source_unit='usd_million',
        value=value,economic_scope='semiconductor_exports',series_id='kcs_exports',raw_ref='test:'+month+stage,
        observed_at=effective,effective_at=effective,released_at=effective+timedelta(days=1),collected_at=NOW,
        data_mode='synthetic_fixture',month=month,coverage_days=days,vintage_stage=stage,reported_yoy=yoy,**kwargs)


def test_g01_contract_missing_spot_available_short_can_qualify():
    a=assessment(short_sources()+[memory('dram_spot_price',12,10)])
    assert a.eligible and 'dram_contract_asp' not in a.hard_missing


def test_g02_spot_rising_never_becomes_contract():
    m=map_observations([memory('dram_spot_price',12,10)],NOW,'1w','unknown')
    state=infer_memory(m.evidence)
    assert state.score > 0 and state.positive_families == ('dram_spot_price',)
    assert 'dram_contract_asp' in state.unknown_families


@pytest.mark.parametrize('contract_now,export_yoy,positive,negative',[
    (80.,50.,'semiconductor_export_momentum','dram_contract_asp'),
    (120.,-50.,'dram_contract_asp','semiconductor_export_momentum'),
])
def test_g03_g04_export_price_conflict_preserved(contract_now,export_yoy,positive,negative):
    m=map_observations([memory('dram_contract_asp',contract_now,100),export(yoy=export_yoy)],NOW,'1m','unknown')
    state=infer_memory(m.evidence)
    assert positive in state.positive_families and negative in state.negative_families
    assert state.conflict > 0


def test_g05_short_sufficient_long_insufficient():
    assert assessment().eligible
    assert not assessment(horizon='1y').eligible


def test_g06_company_financial_constraint_applicable():
    result=evaluate_e11(CompanyFinancials(period='2026-H1',assets=300.,liabilities=100.,equity=200.),None,None)
    check=next(x for x in result.company.checks if x.name=='balance_sheet')
    assert check.status=='passed' and check.residual==0.


def test_g07_memory_business_non_applicable():
    result=evaluate_e11(CompanyFinancials(period='2026-H1',revenue=500.),None,None)
    assert result.memory.status=='non_applicable' and not result.fatal


def test_g08_industry_supply_missing_non_applicable():
    r=evaluate_e11(None,None,None)
    assert r.industry.status=='non_applicable' and 'capacity' in r.industry.missing


def test_g09_strong_missing_reduces_confidence_not_direction():
    a=assessment();b=assessment(short_sources()+[obs('foreign_net_buy',100.,'krw_million','flow'),obs('institution_net_buy',100.,'krw_million','flow')])
    pa,pb=publish_candidate(candidate(),a),publish_candidate(candidate(),b)
    assert pa.probabilities == pb.probabilities == candidate().probabilities
    assert pa.confidence < pb.confidence <= candidate().confidence


def test_g10_hard_missing_withholds():
    a=assessment([s for s in short_sources() if s.source_field!='samsung_preferred_price'])
    p=publish_candidate(candidate(),a)
    assert not a.eligible and p.probabilities is None and 'samsung_preferred_price' in a.hard_missing


def test_g11_23_unmapped_raw_observations_have_no_probability_effect():
    junk=[obs('unknown_'+str(i),float(i)) for i in range(23)]
    a,b=assessment(),assessment(short_sources()+junk)
    assert len(b.unmapped)==23
    assert publish_candidate(candidate(),a).probabilities==publish_candidate(candidate(),b).probabilities
    assert a.confidence_multiplier==b.confidence_multiplier


def test_g12_semantic_unit_mismatch():
    m=map_observations([obs('dram_spot_price',100.,'krw_million','memory_spot')],NOW,'1w','unknown')
    assert not m.evidence and m.unmapped[0].reason=='unit_mismatch'


def test_g13_same_month_revision_not_double_counted():
    a,b,c,d=[export(stage=s,value=v) for s,v in [('nowcast_v1',100.),('nowcast_v2',200.),('nowcast_v3',300.),('final',310.)]]
    # Both full-month releases are as-of eligible; final dominates, regardless of input order.
    mapped=map_observations([c,a,d,b],NOW,'1m','unknown')
    assert len(mapped.evidence)==1 and mapped.evidence[0].value==20.
    assert mapped.evidence[0].source_refs==(d.raw_ref,)


def test_g14_mapping_version_changes_identity_not_raw():
    s=short_sources();a=map_observations(s,NOW,'1w','unknown')
    b=map_observations(s,NOW,'1w','unknown',MappingPolicy(version='semantic-mapping-test-v2'))
    assert a.evidence[0].evidence_id!=b.evidence[0].evidence_id
    assert a.evidence[0].source_refs==b.evidence[0].source_refs
    assert a.evidence[0].value==b.evidence[0].value


def test_g15_horizon_criticality_diverges():
    assert MATRIX['dram_contract_asp'].levels['1w']==Requirement.SUPPORTING
    assert MATRIX['dram_contract_asp'].levels['1y']==Requirement.STRONG
    assert MATRIX['dram_spot_price'].levels['1y']==Requirement.UNAVAILABLE_ALLOWED
    assert MATRIX['samsung_total_assets'].levels['1y']==Requirement.HARD


def test_technical_only_cannot_qualify():
    assert not assessment(short_sources()[2:]).eligible


def test_export_workdays_and_comparable_acceleration():
    older=export('2026-07','nowcast_v2',yoy=10.)
    newer=export(yoy=20.,current_workdays=10.,prior_workdays=12.)
    signals=export_signals(newer,older)
    assert signals['yoy']==20. and signals['workday_adjusted_yoy']==pytest.approx(44.)
    assert signals['acceleration_pp']==10.
    assert export_signals(newer,export('2026-07','nowcast_v1'))['acceleration_pp'] is None
    assert export_signals(export())['workday_adjusted_yoy'] is None


def test_conflicting_export_vintage_rejected():
    with pytest.raises(ValueError,match='conflict'):
        select_vintages([export(value=100.),export(value=200.)],NOW)


def test_cutoff_and_mixed_modes():
    future=short_sources()[0].model_copy(update={'collected_at':NOW+timedelta(seconds=1)})
    assert not map_observations([future],NOW,'1w','unknown').evidence
    live=short_sources()[0].model_copy(update={'data_mode':'live_forward'})
    with pytest.raises(ValueError,match='mixed'):
        map_observations(short_sources()+[live],NOW,'1w','unknown')


def test_company_no_fake_full_capex_or_fcf():
    c=CompanyFinancials(period='2026-H1',operating_cash=100.,capex_ppe_cash=30.)
    assert evaluate_e11(c,None,None).company.metrics['free_cash_flow'] is None
    c=c.model_copy(update={'capex_intangibles':10.})
    assert evaluate_e11(c,None,None).company.metrics['free_cash_flow']==60.


def test_memory_constraint_scope_and_industry_bounds():
    with pytest.raises(ValueError):
        MemoryBusiness(scope='company_consolidated',period='2026-H1',revenue=100.,volume=10.,asp=10.)
    m=MemoryBusiness(period='2026-H1',revenue=100.,volume=10.,asp=10.)
    r=evaluate_e11(None,m,IndustrySupply(period='2026-H1',capacity=10.,production=11.))
    assert r.memory.status=='passed' and r.industry.status=='failed' and r.fatal


def test_candidate_cannot_cross_horizon_or_cutoff():
    with pytest.raises(ValueError,match='identity'):
        publish_candidate(candidate('1m'),assessment())


def test_single_spot_quote_is_not_rising():
    s=obs('dram_spot_price',10.,'usd_per_chip','memory_spot')
    m=map_observations([s],NOW,'1w','unknown')
    assert m.evidence[0].signal is None and infer_memory(m.evidence).score is None


def test_duplicate_skus_do_not_raise_module_coverage():
    s=memory('dram_spot_price',12,10)
    t=s.model_copy(update={'series_id':'another_sku','raw_ref':'test:second_sku'})
    a=assessment(short_sources()+[s]);b=assessment(short_sources()+[s,t])
    assert a.coverage==b.coverage


def test_long_horizon_sufficient_diverse_real_world_contract():
    sources=short_sources()+[memory('dram_contract_asp',120,100),
        obs('hbm_demand',120.,'index','memory_business',prior_value=100.),
        obs('samsung_eps',8000.,'krw_per_share','company_consolidated'),
        obs('samsung_operating_cash',100.,'krw_million','company_consolidated')]
    for field,value in [('samsung_total_assets',300.),('samsung_total_liabilities',100.),('samsung_total_equity',200.)]:
        sources.append(obs(field,value,'krw_million','company_consolidated'))
    a=assessment(sources,'1y')
    assert a.eligible and publish_candidate(candidate('1y'),a).probabilities is not None


def test_operating_margin_requires_matching_periods():
    a=obs('samsung_revenue',200.,'krw_million','company_consolidated')
    b=obs('samsung_operating_profit',40.,'krw_million','company_consolidated')
    mapped=map_observations([a,b],NOW,'1m','unknown')
    assert next(e.value for e in mapped.evidence if e.factor_id=='samsung_operating_margin')==20.
    b=b.model_copy(update={'effective_at':NOW-timedelta(days=2),'observed_at':NOW-timedelta(days=2)})
    assert not any(e.factor_id=='samsung_operating_margin' for e in map_observations([a,b],NOW,'1m','unknown').evidence)


def test_nonmatching_scope_and_stale_evidence_not_credited():
    s=short_sources()[0].model_copy(update={'economic_scope':'memory_contract'})
    assert map_observations([s],NOW,'1w','unknown').unmapped[0].reason=='scope_mismatch'
    s=short_sources()[0].model_copy(update={'effective_at':NOW-timedelta(days=20),'observed_at':NOW-timedelta(days=20)})
    assert map_observations([s],NOW,'1w','unknown').unmapped[0].reason=='stale'


def test_zero_coverage_withholds_instead_of_relabeling_prior():
    a=assessment([])
    assert not a.eligible and publish_candidate(candidate(),a).confidence is None


def test_unregistered_live_mapping_version_rejected():
    s=short_sources()[0].model_copy(update={'data_mode':'live_forward'})
    with pytest.raises(ValueError,match='unsupported mapping'):
        map_observations([s],NOW,'1w','unknown',MappingPolicy(version='arbitrary-v99'))


def test_decision_liquidity_gate_remains_independent():
    from reasoning.decision import decide
    d=decide(up=.99,down=.005,no_history_up=.99,no_history_down=.005,confidence=.99,
        bottom=1.,top=0.,bottom_confirmed=True,top_confirmed=False,bullish_alignment=1.,bearish_alignment=0.,
        buy_liquidity=None,sell_liquidity=None,fatal=False,held=False)
    assert d.action=='WAIT' and 'liquidity' in d.reasons


def test_all_legacy_factors_have_three_explicit_requirement_levels():
    import json
    from pathlib import Path
    profile=json.loads(Path('config/live-model-profile.json').read_text(encoding='utf-8'))
    assert {s['factor_id'] for s in profile['factors']} <= set(MATRIX)
    assert all(set(s.levels)=={'1w','1m','1y'} for s in MATRIX.values())


def test_conflicting_macro_value_cannot_increase_coverage():
    sources=short_sources();copy=sources[0].model_copy(update={'value':10.,'raw_ref':'test:conflict'})
    a=assessment(sources+[copy])
    assert a.coverage['macro']==.5
    assert any(u.reason=='conflicting_source_value' for u in a.unmapped)


def test_export_acceleration_keeps_both_source_references():
    a,b=export('2026-07',yoy=10.),export(yoy=20.)
    batch=map_observations([a,b],NOW,'1m','unknown')
    e=next(e for e in batch.evidence if e.root_id=='kcs_exports:2026-08')
    assert e.derived_signals['acceleration_pp']==10.
    assert set(e.source_refs)=={a.raw_ref,b.raw_ref}


def test_unknown_workdays_never_inferred_from_calendar():
    assert export_signals(export())['workday_adjusted_yoy'] is None


def test_bad_company_identity_is_not_non_applicable():
    sources=short_sources()
    for field,value in [('samsung_total_assets',300.),('samsung_total_liabilities',200.),('samsung_total_equity',200.)]:
        sources.append(obs(field,value,'krw_million','company_consolidated'))
    a=assessment(sources)
    assert not a.eligible and 'E11_constraint_failure' in a.reasons


def test_real_23_fact_classification_contract_without_prediction(tmp_path):
    # Shape matches the 23 captured facts. Values here are authored test data.
    from reasoning.act_sources import Fact
    from reasoning.refinement.audit import classify_facts
    fields=['total_assets','total_liabilities','total_equity','revenue','operating_profit','operating_cash',
        'ppe_acquisition','investing_cash','financing_cash','fx_cash_effect','cash_change','cash_begin','cash_end']
    facts=[]
    for i,name in enumerate(fields):
        facts.append(Fact(factor_id='samsung_'+name,value=-30. if name=='ppe_acquisition' else 100.,unit='krw_million',scope='Consolidated H1',
            source_id='samsung_cf',source_ref='test:'+name,observed_at=NOW-timedelta(days=1),effective_at=NOW-timedelta(days=1),
            released_at=None,collected_at=NOW,market_timezone='Asia/Seoul',authority='official_original',freshness_days=150.,mapping_reason='legacy unmapped'))
    for i in range(7):
        facts.append(facts[0].model_copy(update={'factor_id':'dram_spot_sku_'+str(i),'unit':'usd_per_chip','source_id':'dram_spot','source_ref':'test:spot'+str(i)}))
    for o in [export(stage='nowcast_v1'),export(),export('2026-07',stage='final')]:
        facts.append(facts[0].model_copy(update={'factor_id':'semiconductor_export_demand','unit':'usd_million','source_id':'exports_20',
            'source_ref':o.raw_ref,'effective_at':o.effective_at,'observed_at':o.observed_at,'released_at':o.released_at,
            'month':o.month,'coverage_days':o.coverage_days,'yoy_percent':o.reported_yoy}))
    before=[f.model_dump_json() for f in facts]
    result=classify_facts(facts,NOW)
    assert result['counts']=={'directly mappable':19,'derived evidence mappable':4}
    assert result['new_prediction_created'] is False
    assert before==[f.model_dump_json() for f in facts]
    assert all(f.mapping=='unmapped' for f in facts)


def test_published_contract_manifest_matches_code_and_frozen_model():
    from reasoning.refinement.audit import verify_manifest
    manifest=verify_manifest('config/contracts/real-world-contract-v2.0.0.json')
    assert manifest['live_prediction_enabled'] is False
    assert manifest['entry_threshold']==.8 and manifest['sell_threshold']==.7
    assert manifest['prior']==[.4,.35,.25]


def test_rw01_cross_provider_conflict_is_not_a_revision():
    sources=short_sources()
    other=sources[0].model_copy(update={'source_id':'second_provider','value':7.,'raw_ref':'test:other',
        'collected_at':NOW-timedelta(minutes=1)})
    a=assessment(sources+[other])
    assert a.coverage['macro']==.5
    assert any(u.reason=='conflicting_source_value' for u in a.unmapped)


def test_rw02_same_end_date_different_duration_not_combined():
    a=obs('samsung_revenue',200.,'krw_million','company_consolidated',reporting_period='2026-H1')
    b=obs('samsung_operating_profit',40.,'krw_million','company_consolidated',reporting_period='2026-Q2')
    batch=map_observations([a,b],NOW,'1m','unknown')
    assert not any(e.factor_id=='samsung_operating_margin' for e in batch.evidence)


def test_rw02_missing_reporting_period_unmapped():
    s=obs('samsung_revenue',200.,'krw_million','company_consolidated',reporting_period=None)
    batch=map_observations([s],NOW,'1m','unknown')
    assert not batch.evidence and batch.unmapped[0].reason=='financial_period_missing'


def test_rw02_e11_rejects_cross_period_statement_operands():
    from reasoning.refinement.constraints import company_from_evidence
    sources=[obs('samsung_total_assets',300.,'krw_million','company_consolidated',reporting_period='2026-H1'),
        obs('samsung_total_liabilities',100.,'krw_million','company_consolidated',reporting_period='2026-Q2')]
    batch=map_observations(sources,NOW,'1y','unknown')
    with pytest.raises(ValueError,match='reporting periods'):
        company_from_evidence(batch.evidence)
