"""Operational admission tests; offline data is never published as live evidence."""
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import pytest
from forward_ops import admission
from forward_ops.store import Store

UTC=timezone.utc
NOW=datetime(2026,9,10,3,5,tzinfo=UTC)


@pytest.mark.parametrize('hour,minute,expected',[(21,59,False),(22,0,True),(23,59,True),(0,0,False),(3,5,False)])
def test_schedule_boundaries(hour,minute,expected):
    assert admission.eligible(NOW.replace(hour=hour,minute=minute)) is expected


def test_exception_is_explicit_and_date_scoped():
    assert admission.eligible(NOW,'2026-09-10','User authorized current-time exception')
    for date,reason in [('2026-09-09','reason'),('2026-09-10',None),(None,'reason')]:
        with pytest.raises(ValueError):admission.eligible(NOW,date,reason)


@pytest.mark.parametrize('stamp,expected',[
    ('2026-09-09T22:00:00+00:00','2026-09-09T20:00:00+00:00'),
    ('2026-01-06T22:00:00+00:00','2026-01-06T21:00:00+00:00'),
    ('2026-09-07T22:00:00+00:00','2026-09-04T20:00:00+00:00'),
    ('2026-11-27T22:00:00+00:00','2026-11-27T18:00:00+00:00'),
    ('2026-12-24T22:00:00+00:00','2026-12-24T18:00:00+00:00')])
def test_us_calendar(stamp,expected):
    assert admission.previous_us_close(datetime.fromisoformat(stamp)).isoformat()==expected


def test_unknown_calendar_fails_closed():
    with pytest.raises(ValueError):admission.previous_us_close(NOW.replace(year=2030))


def raw(source_id,dates,tz='Asia/Seoul'):
    from reasoning.market_data import SOURCES,RawResponse
    body=json.dumps({'chart':{'error':None,'result':[{'meta':{'exchangeTimezoneName':tz},
        'timestamp':[int(datetime.fromisoformat(d).timestamp()) for d in dates],
        'indicators':{'quote':[{k:[100+i for i in range(len(dates))] for k in ('open','high','low','close','volume')}],
                      'adjclose':[{'adjclose':[100+i for i in range(len(dates))]}]}}]}})
    return RawResponse(source=SOURCES[source_id],data_mode='synthetic_fixture',requested_at=NOW-timedelta(minutes=1),collected_at=NOW,
        status='available',http_status=200,body=body,sha256=hashlib.sha256(body.encode()).hexdigest(),error=None)


def test_prior_korean_close_filters_today_without_changing_raw():
    r=raw('preferred_daily',['2026-09-09T00:00:00Z','2026-09-10T00:00:00Z'])
    original=r.model_dump_json();cap=datetime(2026,9,9,6,30,tzinfo=UTC)
    derived,audit=admission.filter_raw(r,cap,NOW)
    assert r.model_dump_json()==original and audit['excluded_by_market_cutoff']==1
    result=json.loads(derived.body)['chart']['result'][0]
    assert len(result['timestamp'])==len(result['indicators']['adjclose'][0]['adjclose'])==1
    assert audit['original_sha256']==r.sha256 and derived.sha256!=r.sha256


def test_us_date_end_is_not_silently_relabelled_as_cash_close():
    r=raw('dxy',['2026-09-08T04:00:00Z','2026-09-09T04:00:00Z'],'America/New_York')
    derived,audit=admission.filter_raw(r,datetime(2026,9,9,20,tzinfo=UTC),NOW)
    assert audit['excluded_by_market_cutoff']==1
    assert audit['latest_admitted_effective_at']=='2026-09-09T03:59:59+00:00'


def test_late_collected_raw_rejected():
    r=raw('preferred_daily',['2026-09-09T00:00:00Z'])
    with pytest.raises(ValueError):admission.filter_raw(r,NOW,NOW-timedelta(seconds=1))


def test_duplicate_official_day_across_policy_versions(tmp_path,monkeypatch):
    from forward_ops import preopen
    s=Store(tmp_path)
    s.write('runs/old.json',{'case_key':'daily:2026-09-10','system':{'run_id':'old'}})
    monkeypatch.setattr(preopen,'bootstrap',lambda:pytest.fail('must not collect twice'))
    assert preopen.run_official(s,'2026-09-10','exception',now=NOW)['run_id']=='old'


def test_new_schedule_preserves_old_outcome_due_and_hash(tmp_path):
    from reasoning.live_v2 import outcome_due
    s=Store(tmp_path)
    old=datetime(2026,9,9,7,16,tzinfo=UTC);morning=datetime(2026,9,8,22,tzinfo=UTC)
    for rid,stamp in [('old',old),('morning',morning)]:
        j={'run_id':rid,'p0':{'value':100},'outcome_due':outcome_due(stamp),'horizons':[],'data_cutoff':stamp.isoformat()}
        s.write('runs/'+rid+'.json',{'system':j,'baseline_journal_sha256':'hash-'+rid})
    before=s.path('runs/old.json').read_bytes()
    close={'closed_at':'2026-09-10T06:30:00+00:00','close':101}
    with pytest.raises(ValueError):s.add_outcome('old','1d',close,NOW+timedelta(days=1),'actual',NOW+timedelta(days=1))
    # 07:00 due selects the later close, while the original 16:16 due does not.
    s.add_outcome('morning','1d',close,NOW+timedelta(days=1),'actual',NOW+timedelta(days=1))
    assert before==s.path('runs/old.json').read_bytes()


def test_schedule_installer_enforces_kst_and_morning():
    text=(Path(__file__).resolve().parents[1]/'scripts/install-forward-schedule.ps1').read_text()
    assert '07:00' in text and '16:10' not in text and 'Korea Standard Time' in text


def bundle():
    from reasoning.live import RawSnapshot,ModelProfile
    from reasoning.live_v2 import InputBundle
    root=Path(__file__).resolve().parents[1]
    profile=ModelProfile.model_validate_json((root/'config/live-model-profile.json').read_text())
    sources=(raw('preferred_daily',['2026-09-08T00:00:00Z','2026-09-09T00:00:00Z','2026-09-10T00:00:00Z']),
        raw('preferred_30m',['2026-09-09T06:00:00Z','2026-09-10T02:00:00Z']))
    market=RawSnapshot(snapshot_id='00000000-0000-0000-0000-000000000001',data_mode='synthetic_fixture',
        prediction_timestamp=NOW,data_cutoff=NOW,sources=sources,profile=profile)
    return InputBundle(market=market,documents=(),lock={'code_commit':'0'*40,'files':{'test':'offline'}})


def test_projection_and_frozen_reasoning_replay_deterministically():
    from reasoning.live_v2 import evaluate,digest
    original=bundle();before=original.model_dump_json()
    a,meta=admission.project_bundle(original,'2026-09-10')
    b,again=admission.project_bundle(type(original).model_validate_json(before),'2026-09-10')
    assert a==b and meta==again and original.model_dump_json()==before
    x=evaluate(a);y=evaluate(b)
    assert digest(x)==digest(y) and len(x['executions'])==114
    assert x['data_cutoff']==NOW.isoformat()
    assert meta['korean_price_flow_cutoff']=='2026-09-09T06:30:00+00:00'
    assert meta['us_market_cutoff']=='2026-09-09T20:00:00+00:00'
    assert all(h['feedback_passes']==1 for h in x['horizons'])
    # Midday exception must retain the frozen freshness failure, never force a Wave.
    assert next(s for s in x['sources'] if s['source_id']=='preferred_30m')['status']=='stale'
    assert x['bar_boundaries']['30m']['count']==0


def test_missing_korean_close_does_not_guess():
    b=bundle();b=b.model_copy(update={'market':b.market.model_copy(update={'sources':()})})
    with pytest.raises(ValueError,match='Prior Korean close'):admission.project_bundle(b,'2026-09-10')


def test_unavailable_stays_unavailable():
    r=raw('dxy',[]).model_copy(update={'status':'unavailable','error':'source down'})
    derived,audit=admission.filter_raw(r,NOW,NOW)
    assert derived==r and audit['status']=='unavailable' and audit['latest_admitted_effective_at'] is None


def test_treasury_cutoff_does_not_relabel_quote_time():
    r=raw('treasury_10y',[])
    xml='<feed xmlns="urn:test"><entry><properties><NEW_DATE>2026-09-08T00:00:00</NEW_DATE><BC_10YEAR>4</BC_10YEAR></properties></entry><entry><properties><NEW_DATE>2026-09-09T00:00:00</NEW_DATE><BC_10YEAR>5</BC_10YEAR></properties></entry></feed>'
    r=type(r).model_validate({**r.model_dump(),'body':xml,'sha256':hashlib.sha256(xml.encode()).hexdigest()})
    value,audit=admission.filter_raw(r,datetime(2026,9,9,20,tzinfo=UTC),NOW)
    assert '2026-09-09T00:00:00' not in value.body and '2026-09-08T00:00:00' in value.body
    assert audit['excluded_by_market_cutoff']==1


def test_legacy_replay_rejects_changed_manifest(monkeypatch):
    from forward_ops import preopen
    monkeypatch.setattr(preopen.subprocess,'check_output',lambda *a,**kw:b'original worker')
    with pytest.raises(ValueError,match='version mismatch'):
        preopen.legacy_worker({'operations_manifest':{'forward_ops/worker.py':'incorrect'}})


def test_worker_rejects_shadow_before_import(tmp_path):
    import subprocess,sys
    path=tmp_path/'bad.json';path.write_text(json.dumps({'shadow':{}}))
    result=subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'forward_ops/preopen_worker.py'),str(path)],capture_output=True,text=True)
    assert result.returncode!=0 and 'forbidden' in result.stderr
