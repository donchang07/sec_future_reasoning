"""Offline operational and shadow gates; no test data is published as live."""
from datetime import datetime,timedelta,timezone
from pathlib import Path
import json
import pytest
from forward_ops.models import Position,Event,position_diagnostics,event_diagnostic
from forward_ops.evaluation import label,score,metrics,shadow_comparison,review_gate,select_close
from forward_ops.store import Store,seal,read_seal

NOW=datetime(2026,9,9,8,tzinfo=timezone.utc)


def position(**changes):
    data=dict(venue='kospi_spot',instrument='KOSPI',investor='foreign',measure='net_buy_value',unit='krw_million',value=100.,
        trade_date='2026-09-09',effective_at='2026-09-09T06:30:00Z',released_at='2026-09-09T07:00:00Z',source_ref='https://example.invalid/official',submitter='test')
    return Position.model_validate({**data,**changes})


def event(**changes):
    data=dict(event_id='fomc-test',event_type='FOMC',field='policy_rate',unit='percent',actual=5.25,
        released_at=NOW-timedelta(hours=1),source_ref='https://example.invalid/release',consensus=[5.,5.5],
        consensus_at=NOW-timedelta(hours=2),consensus_ref='https://example.invalid/consensus',
        pre_move=-.03,expected_price_move=-.04,pre_start=NOW-timedelta(days=1),pre_end=NOW-timedelta(hours=2))
    return Event.model_validate({**data,**changes})


def horizon(p=None,action='WAIT',confidence=.7):
    return {'horizon':'1w','final':None if p is None else {'probabilities':dict(zip(('up','down','flat'),p)),'confidence':confidence},'decision':{'action':action}}


@pytest.mark.parametrize('changes',[{'venue':'index_futures'},{'unit':'contracts'},{'effective_at':'2026-09-10T06:30:00Z'},{'value':float('nan')}])
def test_position_dimensions(changes):
    with pytest.raises(ValueError):position(**changes)


def test_shadow_never_sums_spot_and_futures():
    rows=[position().model_dump(mode='json'),position(venue='index_futures',instrument='KOSPI200',measure='net_buy_contracts',unit='contracts',expiry='2026-09',value=-20.).model_dump(mode='json')]
    result=position_diagnostics(rows,NOW)
    assert result['model_influence'] is False
    assert result['interactions'][0]['relationship']=='opposing_positioning_possible_hedge'
    assert 'aggregate_net_buy' not in result


def test_position_unknown_expiry_and_net_position_distinct():
    a=position(venue='usd_futures',instrument='USD',measure='net_position_contracts',unit='contracts',expiry='2026-12')
    assert a.measure=='net_position_contracts'
    assert position_diagnostics([a.model_dump(mode='json')],NOW)['rows'][0]['equity_direction']=='unknown'


def test_event_no_rate_hike_direction_hardcode():
    result=event_diagnostic(event(),NOW)
    assert result['surprise']==0.
    assert result['equity_direction']=='unknown' and result['model_influence'] is False
    assert result['priced_in_fraction']==pytest.approx(.75)


def test_event_missing_consensus_and_wrong_sign_pricing():
    assert event_diagnostic(event(consensus=[],consensus_at=None,consensus_ref=None),NOW)['surprise'] is None
    assert event_diagnostic(event(pre_move=.03),NOW)['priced_in_fraction']==0.


def test_event_lookahead_consensus_rejected():
    with pytest.raises(ValueError):event(consensus_at=NOW)


def test_event_unreleased_rejected():
    with pytest.raises(ValueError):event_diagnostic(event(),NOW-timedelta(hours=3))


def test_immutable_and_revision_conflict(tmp_path):
    store=Store(tmp_path)
    a=store.add_position(position(),NOW)
    store.add_position(position(value=200.),NOW)
    result=store.shadow(NOW)
    assert len(result['positioning']['conflicts'])==1 and not result['positioning']['rows']
    with pytest.raises(FileExistsError):store.write('same.json',{'x':1});store.write('same.json',{'x':2})
    assert read_seal(tmp_path/'positioning'/f"{a}.json")['provenance']=='human_supplied_market_close'


def test_shadow_cutoff_and_human_isolation(tmp_path):
    store=Store(tmp_path);store.add_position(position(),NOW)
    assert not store.shadow(NOW-timedelta(seconds=1))['positioning']['rows']
    assert 'human' not in store.shadow(NOW)


def test_brier_and_unique_accuracy():
    row=score(horizon((.7,.2,.1)),.10)
    assert row['brier']==pytest.approx(.14)
    assert row['correct'] is True
    assert label(.01,'1w')=='flat'


def test_ties_and_withheld_not_zero():
    assert score(horizon(),.1) is None
    assert score(horizon((.5,.5,0.)),.1)['correct'] is None


@pytest.mark.parametrize('action,ret,held,key',[('ENTRY',-.1,False,'false_entry'),('WAIT',.1,False,'missed_entry'),('SELL',.1,True,'false_sell'),('HOLD',-.1,True,'missed_sell')])
def test_action_opportunity_metrics(action,ret,held,key):
    row=score(horizon((.6,.3,.1),action),ret,held)
    assert row[key] is True


def test_calibration_counts_and_confidence():
    rows=[score(horizon((.7,.2,.1)),.1),score(horizon((.7,.2,.1)),-.1)]
    m=metrics(rows)
    assert m['n']==2 and m['directional_accuracy']==.5
    assert sum(b['n'] for b in m['confidence_bins'])==2
    assert sum(b['n'] for b in m['reliability']['up'])==2


def test_select_earliest_mature_close():
    bars=[{'closed_at':(NOW+timedelta(days=d)).isoformat(),'close':100.+d} for d in (0,1,2)]
    assert select_close(bars,NOW+timedelta(hours=1),NOW+timedelta(days=2))['close']==101.
    assert select_close(bars,NOW+timedelta(days=3),NOW+timedelta(days=2)) is None


def test_twenty_guard_deduplicates_and_never_unfreezes():
    records=[{'case_key':str(i),'eligible_case':True} for i in range(19)]*2
    assert review_gate(records)['distinct_cases']==19
    assert not review_gate(records)['review_minimum_met']
    assert not review_gate(records+[{'case_key':'20','eligible_case':True}])['automatic_tuning_allowed']


def test_shadow_comparison_is_descriptive_only():
    row=score(horizon((.7,.2,.1)), -.1)
    rows=[{**row,'run_id':'a','return':-.1,'shadow':{'positioning':{'rows':[{'venue':'index_futures','investor':'foreign','measure':'net_buy_contracts','instrument':'KOSPI200','value':-20.}]},'event':None}}]
    result=shadow_comparison(rows)
    assert result['causal_claim'] is False and result['groups'][0]['baseline_errors']==1


def test_store_path_traversal_rejected(tmp_path):
    with pytest.raises(ValueError):Store(tmp_path).write('../outside.json',{})


def stored_run(store):
    from forward_ops.store import digest
    j={'run_id':'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa','data_cutoff':NOW.isoformat(),'held':False,
        'outcome_due':{h:(NOW+timedelta(days=d)).isoformat() for h,d in [('1d',1),('1w',7),('1m',30),('1y',365)]},
        'p0':{'value':100.},'horizons':[horizon((.7,.2,.1))]}
    r={'system':j,'baseline_journal_sha256':digest(j),'case_key':'daily:2026-09-09','kind':'daily','eligible_case':True,'shadow':{'positioning':{'rows':[]},'event':None}}
    store.write('runs/'+j['run_id']+'.json',r)
    return j


def test_outcome_links_immutable_prediction_and_late_human(tmp_path):
    s=Store(tmp_path);j=stored_run(s);rid=j['run_id'];original=s.path('runs/'+rid+'.json').read_bytes()
    human={'run_id':rid,'horizon':'1w','probabilities':{'up':.2,'down':.7,'flat':.1},'confidence':.6,'human_id':'test','rationale':'independent'}
    s.add_human(human,NOW+timedelta(hours=1));s.add_human({**human,'human_id':'late'},NOW+timedelta(days=8))
    s.add_outcome(rid,'1w',{'closed_at':j['outcome_due']['1w'],'close':110.},NOW+timedelta(days=8),'synthetic:test',NOW+timedelta(days=9))
    e=s.evaluation()
    assert e['system']['1w']['n']==1 and e['human']['1w']['n']==1
    assert e['system']['1w']['directional_accuracy']==1. and e['human']['1w']['directional_accuracy']==0.
    assert s.path('runs/'+rid+'.json').read_bytes()==original
    with pytest.raises(FileExistsError):s.add_outcome(rid,'1w',{'closed_at':j['outcome_due']['1w'],'close':120.},NOW+timedelta(days=8),'synthetic:test',NOW+timedelta(days=9))


def test_outcome_early_or_future_rejected(tmp_path):
    s=Store(tmp_path);j=stored_run(s)
    with pytest.raises(ValueError):s.add_outcome(j['run_id'],'1w',{'closed_at':NOW.isoformat(),'close':110.},NOW,'synthetic:test',NOW)
    with pytest.raises(ValueError):s.add_outcome(j['run_id'],'1w',{'closed_at':j['outcome_due']['1w'],'close':110.},NOW+timedelta(days=8),'synthetic:test',NOW)


def test_daily_duplicate_skips_worker_and_clock_boundaries(tmp_path,monkeypatch):
    from forward_ops import runtime
    s=Store(tmp_path);stored_run(s)
    monkeypatch.setattr(runtime,'bootstrap',lambda:pytest.fail('duplicate attempted model collection'))
    assert runtime.run_daily(s,now=NOW)['status']=='already_sealed'
    assert not runtime.eligible_session(NOW.replace(hour=5))
    assert not runtime.eligible_session(NOW+timedelta(days=3))


def test_worker_rejects_shadow_input_before_import(tmp_path):
    import subprocess,sys
    p=tmp_path/'input.json';p.write_text(json.dumps({'shadow':{'rate':5.}}))
    result=subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'forward_ops/worker.py'),str(p)],capture_output=True,text=True)
    assert result.returncode!=0 and 'forbidden' in result.stderr


def test_baseline_files_unchanged():
    import hashlib
    root=Path(__file__).resolve().parents[1]
    lock=json.loads((root/'docs/03-analysis/live-forward-v2.pre-run-lock.json').read_text())['snapshot']
    for name,sha in lock['files'].items():
        assert hashlib.sha256((root/name).read_text(encoding='utf-8').encode()).hexdigest()==sha,name


def test_http_allowlist_and_read_only(tmp_path):
    import threading,urllib.request,urllib.error
    from http.server import ThreadingHTTPServer
    from forward_ops.web import handler
    server=ThreadingHTTPServer(('127.0.0.1',0),handler(Store(tmp_path)))
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    url='http://127.0.0.1:'+str(server.server_port)
    try:
        with urllib.request.urlopen(url+'/api/state') as r:
            assert json.load(r)['shadow_model_influence'] is False
        for route in ('/../.codex/config.toml','/%2e%2e/secret','/api/run/../../secret'):
            with pytest.raises(urllib.error.HTTPError):urllib.request.urlopen(url+route)
        with pytest.raises(urllib.error.HTTPError):urllib.request.urlopen(urllib.request.Request(url+'/api/state',data=b'{}'))
    finally:server.shutdown();server.server_close();thread.join()


def test_ui_source_uses_safe_text_rendering():
    root=Path(__file__).resolve().parents[1]
    js=(root/'forward_ops/static/app.js').read_text(encoding='utf-8')
    assert 'innerHTML' not in js and 'textContent' in js


def test_minimum_sample_guard_counts_one_session_once():
    assert review_gate([{'case_key':'a','review_key':'session:2026-09-09','eligible_case':True},
        {'case_key':'b','review_key':'session:2026-09-09','eligible_case':True}])['distinct_cases']==1


def test_latest_position_conflict_does_not_fall_back(tmp_path):
    s=Store(tmp_path)
    s.add_position(position(trade_date='2026-09-08',effective_at='2026-09-08T06:30:00Z'),NOW)
    s.add_position(position(),NOW);s.add_position(position(value=200.),NOW)
    assert not s.shadow(NOW)['positioning']['rows']


def test_only_latest_position_per_series():
    old=position(trade_date='2026-09-08',effective_at='2026-09-08T06:30:00Z',value=-20.)
    d=position_diagnostics([old.model_dump(mode='json'),position().model_dump(mode='json')],NOW)
    assert len(d['rows'])==1 and len(d['historical_rows'])==2 and d['rows'][0]['value']==100.


def test_browserless_dom_render_and_drilldown():
    import shutil,subprocess
    node=shutil.which('node')
    if node is None:pytest.skip('Node is unavailable for browserless DOM unit test')
    result=subprocess.run([node,'tests/forward_ui_dom.js'],cwd=Path(__file__).resolve().parents[1],capture_output=True,text=True)
    assert result.returncode==0,result.stdout+result.stderr
