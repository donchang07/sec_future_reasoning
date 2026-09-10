"""Instrument-specific completed/available contracts, independent of model rules."""
import json
import math
from datetime import datetime,time,timedelta,timezone
from urllib.parse import unquote
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo
try:
    from .admission import NY,KST,previous_us_close
except ImportError:
    from admission import NY,KST,previous_us_close

TIMING='source-timing-v1.0.1'
POLICY='daily-preopen-v1.0.1'
VERSION='forward-ops-v1.1.1'
UTC=timezone.utc
EQUITIES={'^IXIC','^SOX','NVDA','AMD','MU','AVGO','TSM'}


def base(raw,knowledge,cap):
    nominal=datetime.combine(knowledge.astimezone(KST).date(),time(7),KST)
    return {'source_id':raw.source.source_id,'instrument':raw.source.instrument,'timing_version':TIMING,
        'target_session':cap.astimezone(NY).date().isoformat(),'market_ceiling':cap.isoformat(),
        'knowledge_cutoff':knowledge.isoformat(),'collected_at':raw.collected_at.isoformat(),'released_at':None,
        'raw_sha256':raw.sha256,'source_url':raw.source.url,'authority':raw.source.authority,
        'source_available':raw.status=='available','provider_final':None,'revisable':True,'model_influence':False,
        'status':'unavailable','reason':None,'latest_source_date':None,
        'availability_at_0700':'unknown_not_captured_by_0700' if raw.collected_at>nominal else 'captured_by_0700_pending_validation'}


def unavailable(audit,reason):return {**audit,'status':'unavailable','reason':reason,'stale_reason':reason}


def treasury_rows(raw,knowledge,cap):
    audit=base(raw,knowledge,cap)
    audit['effective_precision']='approximate_1530_ET_date_observation'
    if raw.collected_at>knowledge:return (),unavailable(audit,'collected_after_knowledge_cutoff')
    if raw.status!='available':return (),unavailable(audit,'source_unavailable: '+str(raw.error))
    try:
        rows={}
        for p in ET.fromstring(raw.body).iter():
            if p.tag.split('}')[-1]!='properties':continue
            fields={c.tag.split('}')[-1]:c.text for c in p}
            if not fields.get('NEW_DATE') or not fields.get('BC_10YEAR'):continue
            day=datetime.fromisoformat(fields['NEW_DATE']).date();value=float(fields['BC_10YEAR'])
            if not math.isfinite(value):raise ValueError('invalid_yield')
            if day in rows and rows[day]!=value:raise ValueError('conflicting_source_revision')
            rows[day]=value
        audit['latest_source_date']=max(rows).isoformat() if rows else None
        target=cap.astimezone(NY).date()
        if target not in rows:return (),unavailable(audit,'target_session_not_available_or_source_market_holiday')
        def effective(day):return datetime.combine(day,time(15,30),NY).astimezone(UTC)
        if effective(target)>cap:return (),unavailable(audit,'effective_after_market_ceiling')
        eligible=tuple((effective(day),rows[day]) for day in sorted(rows) if effective(day)<=cap)
        return eligible,{**audit,'status':'available','reason':None,'stale_reason':None,
            'effective_at':effective(target).isoformat(),'value':rows[target],
            'completion_basis':'Official daily XML row actually received; quote approximately 15:30 ET; exact release unknown'}
    except (ValueError,TypeError,ET.ParseError) as exc:return (),unavailable(audit,'invalid_or_conflicting_treasury: '+str(exc))


def assess_yahoo(raw,knowledge,cap):
    audit=base(raw,knowledge,cap);symbol=unquote(raw.source.instrument)
    if raw.collected_at>knowledge:return unavailable(audit,'collected_after_knowledge_cutoff')
    if raw.status!='available':return unavailable(audit,'source_unavailable: '+str(raw.error))
    try:
        chart=json.loads(raw.body)['chart']
        if chart.get('error'):raise ValueError('provider_chart_error')
        result=chart['result'][0];meta=result['meta'];stamps=result.get('timestamp',[])
        dates=[datetime.fromtimestamp(t,UTC).astimezone(ZoneInfo(meta['exchangeTimezoneName'])).date() for t in stamps]
        audit['latest_source_date']=max(dates).isoformat() if dates else None
        audit['provider_session']=meta.get('currentTradingPeriod',{}).get('regular')
        if symbol not in EQUITIES:
            reason={'DX-Y.NYB':'unverified_DXY_cash_close_not_ICE_futures_settlement',
                'CL=F':'unverified_continuous_futures_daily_bar_not_official_settlement',
                'KRW=X':'unverified_FX_daily_window_not_US_cash_session'}.get(symbol,'unverified_instrument_contract')
            return unavailable(audit,reason)
        if knowledge<cap+timedelta(minutes=20):return unavailable(audit,'session_not_completed_with_buffer')
        opening=datetime.combine(cap.astimezone(NY).date(),time(9,30),NY).astimezone(UTC)
        period=audit['provider_session'] or {}
        if (meta.get('symbol')!=symbol or meta.get('exchangeTimezoneName')!='America/New_York' or
            meta.get('instrumentType')!=('INDEX' if symbol.startswith('^') else 'EQUITY') or
            period.get('start')!=int(opening.timestamp()) or period.get('end')!=int(cap.timestamp())):
            return unavailable(audit,'regular_session_metadata_mismatch')
        indices=[i for i,t in enumerate(stamps) if t==int(opening.timestamp())]
        if not indices:return unavailable(audit,'target_session_bar_not_available')
        values=[];quote=result['indicators']['quote'][0]
        for i in indices:
            b={k:quote[k][i] for k in ('open','high','low','close','volume')}
            if any(v is None or not isinstance(v,(float,int)) or not math.isfinite(v) for v in b.values()):raise ValueError('invalid_OHLCV')
            if not (0<b['low']<=min(b['open'],b['close'])<=max(b['open'],b['close'])<=b['high']) or b['volume']<0:raise ValueError('invalid_OHLCV_range')
            values.append(b)
        if any(b!=values[0] for b in values):raise ValueError('conflicting_duplicate_bar')
        return {**audit,'status':'available_completed_regular_session','reason':None,'stale_reason':None,
            'bar':values[0],'effective_at':cap.isoformat(),'completed_at':cap.isoformat(),
            'completion_basis':'regular-session calendar + matching provider period + 20m buffer; vendor revisable, final flag absent'}
    except (ValueError,TypeError,KeyError,IndexError) as exc:return unavailable(audit,'invalid_source_bar: '+str(exc))
