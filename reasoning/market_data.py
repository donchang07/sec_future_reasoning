"""Machine-readable source collection and conservative point-in-time normalization."""
import calendar
import hashlib
import json
import math
from datetime import datetime,timedelta,timezone,time
from typing import Literal
from urllib.request import Request,urlopen
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo
from pydantic import AwareDatetime,model_validator
from .schemas.contracts import Contract,DataMode,Observation,select_as_of
from .fixture import Bar
from .engines import uid

UTC=timezone.utc


class Source(Contract):
    source_id: str
    provider: str
    instrument: str
    url: str | None
    interval: str
    market_timezone: str
    unit: str
    authority: Literal['official_original','public_vendor_fallback','unavailable']
    priority: int
    revisable: bool = True
    freshness_days: float = 4.
    release_policy: str = 'unknown_release_use_collection_time'
    missing_policy: str = 'unavailable_no_imputation'


def yahoo(source_id,symbol,interval='1d',range_='20y',tz='Asia/Seoul',unit='krw_per_share'):
    return Source(source_id=source_id,provider='Yahoo Finance',instrument=symbol,interval=interval,
        url=f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range_}&interval={interval}',
        market_timezone=tz,unit=unit,authority='public_vendor_fallback',priority=40)


SOURCES={s.source_id:s for s in (
    yahoo('preferred_30m','005935.KS','30m','1mo'),yahoo('preferred_daily','005935.KS'),yahoo('common_daily','005930.KS'),
    Source(source_id='treasury_10y',provider='US Treasury',instrument='daily_par_yield_10y',interval='1d',
        url='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value={year}',
        market_timezone='America/New_York',unit='percent',authority='official_original',priority=10,freshness_days=7.),
    yahoo('usdkrw','KRW=X',range_='1y',tz='Europe/London',unit='krw_per_usd'),
    yahoo('kospi','%5EKS11',range_='1y',unit='index'),
    yahoo('dxy','DX-Y.NYB',range_='1y',tz='America/New_York',unit='index'),
)}
for source_id in ('foreign_net_buy','institution_net_buy','program_net_buy','dram_contract_asp'):
    SOURCES[source_id]=Source(source_id=source_id,provider='not_connected',instrument=source_id,url=None,interval='1d',
        market_timezone='Asia/Seoul',unit='unconfirmed',authority='unavailable',priority=99)


class RawResponse(Contract):
    source: Source
    data_mode: DataMode = 'live_forward'
    requested_at: AwareDatetime
    collected_at: AwareDatetime
    status: Literal['available','unavailable']
    http_status: int | None
    body: str
    sha256: str
    error: str | None

    @model_validator(mode='after')
    def validate_raw(self):
        if self.sha256!=hashlib.sha256(self.body.encode()).hexdigest():raise ValueError('raw response hash mismatch')
        if self.collected_at<self.requested_at:raise ValueError('collection chronology')
        if self.status=='available' and (self.http_status!=200 or not self.body):raise ValueError('available source needs successful response')
        return self


def collect_one(source: Source,opener=urlopen):
    start=datetime.now(UTC);body='';error=None;status='unavailable';http=None
    try:
        if source.url is None:raise ValueError('No verified source credentials/series; unavailable')
        url=source.url.format(year=start.year)
        with opener(Request(url,headers={'User-Agent':'SEC-Future-Reasoning-Research/1.0'}),timeout=30) as response:
            http=response.status
            body=response.read(8_000_000).decode('utf-8')
        if http!=200:raise ValueError(f'HTTP {http}')
        status='available'
    except (OSError,ValueError) as exc:error=f'{type(exc).__name__}: {exc}'
    return RawResponse(source=source,requested_at=start,collected_at=datetime.now(UTC),status=status,http_status=http,
        body=body,sha256=hashlib.sha256(body.encode()).hexdigest(),error=error)


def freshness(effective_at,cutoff,max_age_days):
    if effective_at>cutoff:return 'future'
    return 'stale' if (cutoff-effective_at).total_seconds()>max_age_days*86400 else 'fresh'


def parse_yahoo(raw: RawResponse,cutoff):
    if raw.collected_at>cutoff:raise ValueError('source collected after cutoff')
    excluded=dict(incomplete=0,off_grid=0,invalid=0)
    if raw.status!='available':return (),excluded
    chart=json.loads(raw.body)['chart']
    if chart.get('error') or not chart.get('result'):raise ValueError('provider chart error')
    result=chart['result'][0];meta=result['meta'];tz=ZoneInfo(meta['exchangeTimezoneName'])
    quote=result['indicators']['quote'][0];bars=[]
    for i,stamp in enumerate(result.get('timestamp',[])):
        start=datetime.fromtimestamp(stamp,UTC).astimezone(tz)
        if raw.source.interval=='30m':
            if start.second or start.minute not in (0,30) or start.weekday()>4 or not time(9)<=start.time().replace(tzinfo=None)<time(15,30):
                excluded['off_grid']+=1;continue
            end=start+timedelta(minutes=30)
        elif meta['exchangeTimezoneName']=='Asia/Seoul':
            end=datetime.combine(start.date(),time(15,30),tz)
        else:
            # FX/index daily timestamps don't establish a release time. Take the
            # conservative end of their provider-local day; current day excluded.
            end=datetime.combine(start.date(),time(23,59,59),tz)
        end=end.astimezone(UTC)
        if end+timedelta(minutes=20)>cutoff:
            excluded['incomplete']+=1;continue
        try:
            values={key:quote[key][i] for key in ('open','high','low','close','volume')}
            if any(v is None or not math.isfinite(v) for v in values.values()):raise ValueError('missing OHLCV')
            bars.append(Bar(closed_at=end,**values))
        except (ValueError,IndexError,KeyError):excluded['invalid']+=1
    unique={}
    for b in bars:
        if b.closed_at in unique and b!=unique[b.closed_at]:raise ValueError('conflicting duplicate bar')
        unique[b.closed_at]=b
    return tuple(unique[k] for k in sorted(unique)),excluded


def aggregate(bars,interval,cutoff):
    tz=ZoneInfo('Asia/Seoul');groups={}
    for b in bars:
        date=b.closed_at.astimezone(tz).date()
        key=date-timedelta(days=date.weekday()) if interval=='1w' else date.replace(day=1)
        groups.setdefault(key,[]).append(b)
    result=[]
    for key,items in sorted(groups.items()):
        if key==min(groups) and items[0].closed_at.astimezone(tz).date()>key:
            continue  # The raw range begins inside this period; completeness unknown.
        end_date=key+timedelta(days=4) if interval=='1w' else key.replace(day=calendar.monthrange(key.year,key.month)[1])
        end=datetime.combine(end_date,time(15,30) if interval=='1w' else time(23,59,59),tz).astimezone(UTC)
        if end+timedelta(minutes=20)>cutoff:continue
        result.append(Bar(closed_at=end,open=items[0].open,high=max(b.high for b in items),low=min(b.low for b in items),
                          close=items[-1].close,volume=sum(b.volume for b in items)))
    return tuple(result)


def choose_revision(observations,cutoff):
    eligible=select_as_of(tuple(o for o in observations if o.collected_at is None or o.collected_at<=cutoff),cutoff)
    if not eligible:return None
    latest=max(o.observed_at for o in eligible);candidates=[o for o in eligible if o.observed_at==latest]
    if len({(o.value,o.unit) for o in candidates})>1:raise ValueError('source conflict')
    return max(candidates,key=lambda o:o.available_at)


def make_observation(raw,factor,unit,value,effective,precision='second'):
    return Observation(data_mode=raw.data_mode,observation_id=uid(f'{raw.sha256}/{factor}/{effective.isoformat()}'),factor_id=factor,
        source_id=raw.source.source_id,revision_id=raw.sha256,unit=unit,value=float(value),observed_at=effective,
        published_at=raw.collected_at,available_at=raw.collected_at,released_at=None,collected_at=raw.collected_at,
        effective_at=effective,source_ref=f'raw:{raw.sha256}',market_timezone=raw.source.market_timezone,time_precision=precision)


def treasury_observations(raw,cutoff):
    if raw.collected_at>cutoff:raise ValueError('source collected after cutoff')
    if raw.status!='available':return ()
    root=ET.fromstring(raw.body);out=[];tz=ZoneInfo('America/New_York')
    for properties in root.iter():
        if not properties.tag.endswith('}properties'):continue
        row={e.tag.split('}')[-1]:e.text for e in properties}
        if not row.get('BC_10YEAR') or not row.get('NEW_DATE'):continue
        date=datetime.fromisoformat(row['NEW_DATE']).date()
        effective=datetime.combine(date,time(23,59,59),tz).astimezone(UTC)
        if effective<=cutoff:out.append(make_observation(raw,'us_10y_yield','percent',float(row['BC_10YEAR']),effective,'date'))
    return tuple(sorted(out,key=lambda o:o.observed_at))
