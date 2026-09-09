"""Data-boundary tests precede adapters; synthetic test responses never become live evidence."""
import hashlib
import json
from datetime import datetime,timedelta,timezone
from pathlib import Path
import pytest
from reasoning.market_data import SOURCES, RawResponse, parse_yahoo, aggregate, choose_revision, freshness, collect_one
from reasoning.schemas.contracts import Observation
from reasoning.live import write_immutable, attach_outcome

UTC=timezone.utc
NOW=datetime(2026,9,9,7,tzinfo=UTC)


def response(points,interval='1d',collected=NOW):
    body=json.dumps({'chart':{'error':None,'result':[{'meta':{'exchangeTimezoneName':'Asia/Seoul','currency':'KRW'},
        'timestamp':[int(t.timestamp()) for t in points], 'indicators':{'quote':[{'open':[50000.]*len(points),
        'high':[51000.]*len(points),'low':[49000.]*len(points),'close':[50500.]*len(points),'volume':[1000.]*len(points)}]}}]}})
    return RawResponse(source=SOURCES['preferred_30m' if interval=='30m' else 'preferred_daily'],
        requested_at=collected-timedelta(seconds=1),collected_at=collected,status='available',http_status=200,
        body=body,sha256=hashlib.sha256(body.encode()).hexdigest(),error=None,data_mode='synthetic_fixture')


def observation(value=4.,collected=NOW,mode='live_forward',revision='r1'):
    from uuid import uuid5,NAMESPACE_URL
    return Observation(observation_id=uuid5(NAMESPACE_URL,revision),factor_id='us_10y_yield',source_id='treasury',revision_id=revision,
        unit='percent',value=value,observed_at=NOW-timedelta(days=1),published_at=collected,available_at=collected,
        data_mode=mode,released_at=None,collected_at=collected,effective_at=NOW-timedelta(days=1),
        source_ref='raw:hash',market_timezone='America/New_York',time_precision='date')


def test_source_unavailable():
    def unavailable(request,timeout):raise OSError('offline')
    result=collect_one(SOURCES['preferred_daily'],opener=unavailable)
    assert result.status=='unavailable' and not result.body


def test_source_stale():
    assert freshness(NOW-timedelta(days=9),NOW,7.)=='stale'


def test_source_conflict():
    with pytest.raises(ValueError,match='conflict'):
        choose_revision((observation(),observation(5.,revision='r2')),NOW)


def test_market_timezone():
    # 00:00 UTC is the Korean session start, not its daily closing time.
    bars,excluded=parse_yahoo(response([datetime(2026,9,8,tzinfo=UTC)]),NOW)
    assert bars[0].closed_at==datetime(2026,9,8,6,30,tzinfo=UTC)


def test_data_cutoff():
    raw=response([datetime(2026,9,8,tzinfo=UTC)],collected=NOW+timedelta(seconds=1))
    with pytest.raises(ValueError,match='cutoff'):parse_yahoo(raw,NOW)


def test_revision():
    first=observation();second=observation(4.2,NOW+timedelta(days=1),revision='r2')
    assert choose_revision((first,second),NOW).value==4.
    assert choose_revision((first,second),NOW+timedelta(days=1)).value==4.2


def test_lookahead_prevention_unknown_release():
    assert observation().released_at is None
    assert choose_revision((observation(),),NOW-timedelta(seconds=1)) is None


def test_missing_30m():
    bars,excluded=parse_yahoo(response([],interval='30m'),NOW)
    from reasoning.technical import analyze_wave
    assert not analyze_wave(bars).available


def test_intraday_is_not_daily_close():
    cutoff=datetime(2026,9,9,5,tzinfo=UTC)
    bars,excluded=parse_yahoo(response([datetime(2026,9,9,tzinfo=UTC)],collected=cutoff),cutoff)
    assert bars==() and excluded['incomplete'] == 1


def test_live_journal_immutability(tmp_path):
    p=tmp_path/'sealed.json';write_immutable(p,{'a':1});write_immutable(p,{'a':1})
    with pytest.raises(ValueError,match='immutable'):write_immutable(p,{'a':2})


def test_same_raw_replay_reproducibility():
    r=response([datetime(2026,9,8,tzinfo=UTC)])
    assert parse_yahoo(r,NOW)==parse_yahoo(RawResponse.model_validate_json(r.model_dump_json()),NOW)


def test_partial_30m_and_non_grid_quote_excluded():
    cutoff=datetime(2026,9,9,5,45,tzinfo=UTC)
    r=response([datetime(2026,9,9,4,30,tzinfo=UTC),datetime(2026,9,9,5,30,tzinfo=UTC),datetime(2026,9,9,5,44,tzinfo=UTC)],'30m',cutoff)
    bars,excluded=parse_yahoo(r,cutoff)
    assert len(bars)==1 and excluded['incomplete']==1 and excluded['off_grid']==1


def test_unfinished_week_excluded():
    times=[datetime(2026,8,31,tzinfo=UTC)]+[datetime(2026,9,d,tzinfo=UTC) for d in (1,2,3,4,7,8)]
    bars,_=parse_yahoo(response(times),NOW)
    weekly=aggregate(bars,'1w',NOW)
    assert len(weekly)==1 and weekly[0].volume==5000.


def test_first_partial_aggregation_bucket_excluded():
    times=[datetime(2026,9,d,tzinfo=UTC) for d in (2,3,4)]
    bars,_=parse_yahoo(response(times),NOW)
    assert aggregate(bars,'1w',NOW)==()


def test_mode_mixing_rejected():
    from reasoning.fixture import Fixture
    root=Path(__file__).resolve().parents[1]
    raw=json.loads((root/'fixtures/samsung-preferred-v1.json').read_text());raw['data_mode']='live_forward'
    with pytest.raises(ValueError,match='mode'):Fixture.model_validate(raw)


def test_model_core_unchanged():
    root=Path(__file__).resolve().parents[1]
    config=json.loads((root/'config/live-model-profile.json').read_text())
    for name,expected in config['core_sha256'].items():
        assert hashlib.sha256((root/'reasoning'/name).read_text(encoding='utf-8').encode()).hexdigest()==expected


def test_outcome_cannot_arrive_early(tmp_path):
    with pytest.raises(ValueError,match='due'):
        attach_outcome(tmp_path/'outcome.json',run_id='run',journal_sha256='a'*64,due_at=NOW+timedelta(days=1),
                       observed_at=NOW,collected_at=NOW,price=50000.,source_ref='source')


def test_offline_full_snapshot_replay_and_missing_trace():
    from reasoning.live import RawSnapshot,ModelProfile,evaluate,SealedLive
    from reasoning.engines import uid
    root=Path(__file__).resolve().parents[1]
    profile=ModelProfile.model_validate_json((root/'config/live-model-profile.json').read_text())
    r=response([datetime(2026,9,8,tzinfo=UTC)])
    snapshot=RawSnapshot(snapshot_id=uid('offline-source-test'),data_mode='synthetic_fixture',prediction_timestamp=NOW,
        data_cutoff=NOW,sources=(r,),profile=profile)
    first=evaluate(snapshot);sealed=SealedLive.seal(first)
    assert evaluate(SealedLive.model_validate_json(sealed.model_dump_json()).snapshot.raw_snapshot)==first
    assert len(first.run.executions)==114
    assert all(h.final is None and h.decision.action=='WAIT' for h in first.run.horizons)
    e01=next(r for r in first.run.executions if r.engine_id=='E01')
    assert any(w.code=='source_missing' for w in e01.result.warnings)
    assert 'dram_contract_asp' in first.availability.missing_factors


def test_treasury_official_xml_parser():
    from reasoning.market_data import treasury_observations
    body='<feed xmlns:d="urn:dataservices"><d:properties><d:NEW_DATE>2026-09-08T00:00:00</d:NEW_DATE><d:BC_10YEAR>4.2</d:BC_10YEAR></d:properties></feed>'
    raw=RawResponse(source=SOURCES['treasury_10y'],requested_at=NOW,collected_at=NOW,status='available',http_status=200,
        body=body,sha256=hashlib.sha256(body.encode()).hexdigest(),error=None,data_mode='synthetic_fixture')
    obs=treasury_observations(raw,NOW)
    assert len(obs)==1 and obs[0].value==4.2 and obs[0].released_at is None
    assert obs[0].observed_at==datetime(2026,9,9,3,59,59,tzinfo=UTC)


def test_live_source_cannot_claim_release_before_collection():
    values=observation().model_dump();values['published_at']=NOW-timedelta(hours=1)
    with pytest.raises(ValueError,match='backdated'):Observation.model_validate(values)
