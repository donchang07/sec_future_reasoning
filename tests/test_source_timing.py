"""Source availability changes must not change model rules or invent releases."""
from datetime import datetime,timedelta,timezone
import hashlib,json
import pytest
from forward_ops.source_timing import treasury_rows,assess_yahoo
from reasoning.market_data import RawResponse,SOURCES,yahoo

UTC=timezone.utc
AT7=datetime(2026,9,9,22,tzinfo=UTC)
CAP=datetime(2026,9,9,20,tzinfo=UTC)


def response(body,source,at=AT7):
    return RawResponse(source=source,data_mode='synthetic_fixture',requested_at=at-timedelta(seconds=1),collected_at=at,
        status='available',http_status=200,body=body,sha256=hashlib.sha256(body.encode()).hexdigest(),error=None)


def treasury(days=('2026-09-08','2026-09-09'),at=AT7):
    body='<feed xmlns="urn:test">'+''.join('<entry><properties><NEW_DATE>'+d+'T00:00:00</NEW_DATE><BC_10YEAR>4.2</BC_10YEAR></properties></entry>' for d in days)+'</feed>'
    return response(body,SOURCES['treasury_10y'],at)


def equity(symbol='NVDA',at=AT7,**changes):
    start=int(CAP.replace(hour=13,minute=30).timestamp())
    r={'meta':{'symbol':symbol,'exchangeTimezoneName':'America/New_York','instrumentType':'EQUITY',
        'regularMarketPrice':99999,'currentTradingPeriod':{'regular':{'start':start,'end':int(CAP.timestamp())}}},
        'timestamp':[start],'indicators':{'quote':[{'open':[100],'high':[110],'low':[90],'close':[105],'volume':[1000]}]}}
    r.update(changes)
    return response(json.dumps({'chart':{'result':[r],'error':None}}),yahoo('nvda',symbol,range_='5d',tz='America/New_York',unit='usd_per_share'),at)


def test_treasury_0700_uses_prior_session_not_end_of_day():
    rows,audit=treasury_rows(treasury(),AT7,CAP)
    assert len(rows)==2 and rows[-1][0].isoformat()=='2026-09-09T19:30:00+00:00'
    assert audit['status']=='available' and audit['released_at'] is None
    assert audit['effective_precision']=='approximate_1530_ET_date_observation'


def test_treasury_later_capture_cannot_enter_0700():
    rows,audit=treasury_rows(treasury(at=AT7+timedelta(hours=3)),AT7,CAP)
    assert not rows and audit['reason']=='collected_after_knowledge_cutoff'


def test_missing_target_not_silently_backfilled():
    rows,audit=treasury_rows(treasury(('2026-09-08',)),AT7,CAP)
    assert not rows and audit['status']=='unavailable' and 'target_session' in audit['reason']


def test_treasury_future_rows_excluded():
    rows,_=treasury_rows(treasury(('2026-09-09','2026-09-10')),AT7,CAP)
    assert len(rows)==1 and rows[0][0]<=CAP


def test_early_cash_close_does_not_admit_later_yield():
    rows,audit=treasury_rows(treasury(),AT7,CAP.replace(hour=17))
    assert not rows and audit['reason']=='effective_after_market_ceiling'


def test_conflicting_treasury_duplicate_fails_closed():
    r=treasury(('2026-09-09','2026-09-09'));body=r.body.replace('4.2','4.3',1)
    r=response(body,r.source)
    rows,audit=treasury_rows(r,AT7,CAP)
    assert not rows and 'conflict' in audit['reason']


def test_completed_regular_bar_ignores_post_market_quote():
    a=assess_yahoo(equity(),AT7,CAP)
    assert a['status']=='available_completed_regular_session' and a['bar']['close']==105
    assert a['provider_final'] is None and a['revisable'] and not a['model_influence']


def test_current_incomplete_equity_bar_rejected():
    a=assess_yahoo(equity(at=CAP),CAP,CAP)
    assert a['status']=='unavailable' and a['reason']=='session_not_completed_with_buffer'


def test_missing_or_bad_equity_ohlcv_rejected():
    r=equity();d=json.loads(r.body);d['chart']['result'][0]['indicators']['quote'][0]['close']=[None]
    a=assess_yahoo(response(json.dumps(d),r.source),AT7,CAP)
    assert a['status']=='unavailable' and 'invalid' in a['reason']


def test_regular_metadata_must_match_target_session():
    r=equity();d=json.loads(r.body);d['chart']['result'][0]['meta']['currentTradingPeriod']['regular']['end']+=3600
    a=assess_yahoo(response(json.dumps(d),r.source),AT7,CAP)
    assert a['reason']=='regular_session_metadata_mismatch'


@pytest.mark.parametrize('symbol',['DX-Y.NYB','CL=F','KRW=X'])
def test_cash_index_fx_and_continuous_oil_not_equity_closes(symbol):
    a=assess_yahoo(equity(symbol),AT7,CAP)
    assert a['status']=='unavailable' and 'unverified' in a['reason']


def test_midday_capture_does_not_certify_past_0700():
    at=AT7+timedelta(hours=5)
    a=assess_yahoo(equity(at=at),at,CAP)
    assert a['status']=='available_completed_regular_session'
    assert a['availability_at_0700']=='unknown_not_captured_by_0700'


def test_treasury_dst_observation_time():
    at=datetime(2026,1,7,22,tzinfo=UTC);cap=datetime(2026,1,7,21,tzinfo=UTC)
    rows,_=treasury_rows(treasury(('2026-01-07',),at),at,cap)
    assert rows[-1][0].hour==20 and rows[-1][0].minute==30


def test_fixed_preparation_preserves_model_and_admits_treasury():
    from test_preopen import bundle
    from forward_ops.timing_evaluate import project,prepare,evaluate
    from reasoning.live_v2 import digest
    b=bundle();b=b.model_copy(update={'market':b.market.model_copy(update={'sources':b.market.sources+(treasury(),)})})
    original=b.model_dump_json();admitted,audit=project(b,'2026-09-10')
    f,statuses=prepare(admitted,b)
    obs=[o for o in f.observations if o.factor_id=='us_10y_yield']
    assert obs[-1].effective_at==CAP-timedelta(minutes=30) and obs[-1].value==4.2
    assert obs[-1].time_precision=='date' and obs[-1].released_at is None
    assert b.model_dump_json()==original
    result=evaluate(admitted,b)
    assert len(result['executions'])==114 and result['versions']['policy']=='entry80-sell70-v1'
    assert digest(result)==digest(evaluate(admitted,b))
    assert not any(s['source_id'] in ('nvda','sox','nasdaq','wti') for s in result['raw_observations'])
    assert result['data_timing_version']=='source-timing-v1.0.1'


def test_missing_treasury_reaches_e01_as_missing():
    from test_preopen import bundle
    from forward_ops.timing_evaluate import project,prepare
    b=bundle();b=b.model_copy(update={'market':b.market.model_copy(update={'sources':b.market.sources+(treasury(('2026-09-08',)),)})})
    admitted,_=project(b,'2026-09-10');f,statuses=prepare(admitted,b)
    assert not any(o.factor_id=='us_10y_yield' for o in f.observations)
    assert next(s for s in statuses if s.source_id=='treasury_10y').status=='unavailable'


def test_equity_prior_date_is_explicitly_unavailable():
    r=equity();d=json.loads(r.body);d['chart']['result'][0]['timestamp'][0]-=86400
    a=assess_yahoo(response(json.dumps(d),r.source),AT7,CAP)
    assert a['reason']=='target_session_bar_not_available' and a['latest_source_date']=='2026-09-08'


@pytest.mark.parametrize('at,cap,opening',[
    ('2026-01-07T22:00:00+00:00','2026-01-07T21:00:00+00:00','2026-01-07T14:30:00+00:00'),
    ('2026-11-27T22:00:00+00:00','2026-11-27T18:00:00+00:00','2026-11-27T14:30:00+00:00')])
def test_equity_winter_and_early_close(at,cap,opening):
    at=datetime.fromisoformat(at);cap=datetime.fromisoformat(cap);opening=int(datetime.fromisoformat(opening).timestamp())
    r=equity(at=at);d=json.loads(r.body);row=d['chart']['result'][0];row['timestamp']=[opening]
    row['meta']['currentTradingPeriod']['regular']={'start':opening,'end':int(cap.timestamp())}
    assert assess_yahoo(response(json.dumps(d),r.source,at),at,cap)['status']=='available_completed_regular_session'


def test_non_us_preparation_is_unchanged():
    from test_preopen import bundle
    from forward_ops.admission import project_bundle
    from forward_ops.timing_evaluate import project,prepare
    from reasoning.live import prepare as old_prepare
    b=bundle();old,_=project_bundle(b,'2026-09-10');new,_=project(b,'2026-09-10')
    old_fixture=old_prepare(old.market)[0];new_fixture=prepare(new,b)[0]
    assert old_fixture==new_fixture
