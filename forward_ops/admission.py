"""Versioned operational row admission; never adjusts frozen model semantics."""
import hashlib
import json
from datetime import date,datetime,time,timedelta,timezone
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

UTC=timezone.utc
KST=ZoneInfo('Asia/Seoul')
NY=ZoneInfo('America/New_York')
POLICY='daily-preopen-v1.0.0'
VERSION='forward-ops-v1.1.0'
# https://www.nyse.com/trade/hours-calendars — retrieved 2026-09-10.
HOLIDAYS={
    2026:'01-01 01-19 02-16 04-03 05-25 06-19 07-03 09-07 11-26 12-25',
    2027:'01-01 01-18 02-15 03-26 05-31 06-18 07-05 09-06 11-25 12-24',
    2028:'01-17 02-21 04-14 05-29 06-19 07-04 09-04 11-23 12-25'}
EARLY={2026:'11-27 12-24',2027:'11-26',2028:'07-03 11-24'}
KOREAN={'preferred_30m','preferred_daily','common_daily','kospi','foreign_net_buy','institution_net_buy','program_net_buy'}
US={'treasury_10y','usdkrw','dxy'}


def eligible(now,exception_date=None,reason=None):
    local=now.astimezone(KST)
    if exception_date or reason:
        if exception_date!=local.date().isoformat() or not reason or not reason.strip():
            raise ValueError('Exception needs current KST date and explicit reason')
        return True
    return time(7)<=local.time().replace(tzinfo=None)<time(9)


def previous_us_close(now):
    day=now.astimezone(NY).date()
    for _ in range(15):
        if day.year not in HOLIDAYS:raise ValueError('US calendar unavailable for year')
        md=day.strftime('%m-%d')
        if day.weekday()<5 and md not in HOLIDAYS[day.year].split():
            close=datetime.combine(day,time(13 if md in EARLY[day.year].split() else 16),NY).astimezone(UTC)
            if close<=now:return close
        day-=timedelta(days=1)
    raise ValueError('No completed US session')


def row_end(stamp,tz,interval):
    start=datetime.fromtimestamp(stamp,UTC).astimezone(tz)
    if interval=='30m':end=start+timedelta(minutes=30)
    else:end=datetime.combine(start.date(),time(15,30) if tz.key=='Asia/Seoul' else time(23,59,59),tz)
    return end.astimezone(UTC)


def filter_raw(raw,cap,knowledge):
    if raw.collected_at>knowledge:raise ValueError('Raw collection after knowledge cutoff')
    audit={'source_id':raw.source.source_id,'original_sha256':raw.sha256,'admitted_sha256':raw.sha256,
        'market_effective_ceiling':cap.isoformat(),'collected_at':raw.collected_at.isoformat(),
        'released_at':None,'excluded_by_market_cutoff':0,'latest_admitted_effective_at':None,
        'timestamp_policy':'unchanged frozen provider-local close/end-of-day; no relabeling'}
    if raw.status!='available':return raw,{**audit,'status':'unavailable','reason':raw.error}
    try:
        ends=[]
        if raw.source.source_id=='treasury_10y':
            root=ET.fromstring(raw.body)
            for parent in root.iter():
                for child in list(parent):
                    if child.tag.split('}')[-1]!='entry':continue
                    dates=[e.text for e in child.iter() if e.tag.split('}')[-1]=='NEW_DATE']
                    if not dates:continue
                    end=datetime.combine(datetime.fromisoformat(dates[0]).date(),time(23,59,59),NY).astimezone(UTC)
                    if end>cap:parent.remove(child);audit['excluded_by_market_cutoff']+=1
                    else:ends.append(end)
            body=ET.tostring(root,encoding='unicode')
        else:
            data=json.loads(raw.body);result=data['chart']['result'][0]
            tz=ZoneInfo(result['meta']['exchangeTimezoneName'])
            all_ends=[row_end(s,tz,raw.source.interval) for s in result.get('timestamp',[])]
            keep=[i for i,end in enumerate(all_ends) if end<=cap]
            ends=[all_ends[i] for i in keep]
            audit['excluded_by_market_cutoff']=len(all_ends)-len(keep)
            result['timestamp']=[result['timestamp'][i] for i in keep]
            for series in result['indicators'].values():
                for fields in series:
                    for name,values in fields.items():
                        if len(values)!=len(all_ends):raise ValueError('Misaligned source indicator arrays')
                        fields[name]=[values[i] for i in keep]
            body=json.dumps(data,sort_keys=True,separators=(',',':'))
        derived=type(raw).model_validate({**raw.model_dump(),'body':body,'sha256':hashlib.sha256(body.encode()).hexdigest()})
        return derived,{**audit,'admitted_sha256':derived.sha256,'status':'projected',
            'latest_admitted_effective_at':max(ends).isoformat() if ends else None}
    except (ValueError,TypeError,KeyError,IndexError,ET.ParseError) as exc:
        derived=type(raw).model_validate({**raw.model_dump(),'status':'unavailable','error':'admission: '+str(exc)})
        return derived,{**audit,'status':'unavailable','reason':str(exc)}


def project_bundle(bundle,session):
    from reasoning.market_data import parse_yahoo
    from reasoning.live_v2 import digest
    cutoff=bundle.market.data_cutoff
    raw=next((r for r in bundle.market.sources if r.source.source_id=='preferred_daily'),None)
    if raw is None:raise ValueError('Prior Korean close unavailable')
    bars,_=parse_yahoo(raw,cutoff)
    prior=[b.closed_at for b in bars if b.closed_at.astimezone(KST).date()<date.fromisoformat(session)]
    if not prior:raise ValueError('Prior Korean close unavailable')
    korea=max(prior);us=previous_us_close(cutoff)
    projected=[];audit=[]
    for r in bundle.market.sources:
        if r.source.source_id in KOREAN:cap=korea
        elif r.source.source_id in US:cap=us
        elif r.status=='available':raise ValueError('Unclassified available market source')
        else:cap=cutoff
        value,entry=filter_raw(r,cap,cutoff);projected.append(value);audit.append(entry)
    market=type(bundle.market).model_validate({**bundle.market.model_dump(),'sources':tuple(projected)})
    admitted=type(bundle).model_validate({**bundle.model_dump(),'market':market})
    metadata={'policy_version':POLICY,'korean_price_flow_cutoff':korea.isoformat(),'us_market_cutoff':us.isoformat(),
        'korean_cutoff_basis':'latest observed valid prior preferred daily close; calendar not independently verified',
        'us_cutoff_basis':'NYSE core cash calendar 2026-2028; ceiling, not FX/Treasury close-time relabeling',
        'knowledge_cutoff':cutoff.isoformat(),'sources':audit,'original_raw_bundle_hash':digest(bundle.model_dump(mode='json')),
        'admitted_bundle_hash':digest(admitted.model_dump(mode='json'))}
    return admitted,metadata
