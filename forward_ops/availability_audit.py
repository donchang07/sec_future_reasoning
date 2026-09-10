"""Capture/replay market availability diagnostics without producing predictions."""
import json
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4
from urllib.parse import quote
try:
    from .source_timing import assess_yahoo,treasury_rows,previous_us_close,TIMING
except ImportError:
    from source_timing import assess_yahoo,treasury_rows,previous_us_close,TIMING

SYMBOLS={'nasdaq':'^IXIC','sox':'^SOX','nvda':'NVDA','amd':'AMD','micron':'MU','broadcom':'AVGO','tsmc_adr':'TSM',
    'dxy':'DX-Y.NYB','wti':'CL=F','usdkrw':'KRW=X'}


def collect():
    from concurrent.futures import ThreadPoolExecutor
    from reasoning.market_data import yahoo,collect_one,SOURCES
    units={'nasdaq':'index','sox':'index','dxy':'index','wti':'usd_per_barrel','usdkrw':'krw_per_usd'}
    sources=[yahoo(sid,quote(symbol,safe=''),range_='5d',tz='Europe/London' if sid=='usdkrw' else 'America/New_York',
        unit=units.get(sid,'usd_per_share')) for sid,symbol in SYMBOLS.items()]
    sources=[s.model_copy(update={'url':s.url+'&includePrePost=false'}) for s in sources]+[SOURCES['treasury_10y']]
    with ThreadPoolExecutor(max_workers=4) as pool:raw=tuple(pool.map(collect_one,sources))
    return {'captured_at':datetime.now(timezone.utc).isoformat(),'data_mode':'live_forward','sources':[r.model_dump(mode='json') for r in raw]}


def assess(capture,knowledge=None):
    from reasoning.market_data import RawResponse
    knowledge=knowledge or datetime.fromisoformat(capture['captured_at']);cap=previous_us_close(knowledge)
    rows=[]
    for value in capture['sources']:
        raw=RawResponse.model_validate(value)
        result=treasury_rows(raw,knowledge,cap)[1] if raw.source.source_id=='treasury_10y' else assess_yahoo(raw,knowledge,cap)
        rows.append(result)
    return {'timing_version':TIMING,'data_mode':capture['data_mode'],'knowledge_cutoff':knowledge.isoformat(),
        'market_cutoff':cap.isoformat(),'model_influence':False,'sources':rows}


def main():
    import argparse
    from .store import seal,digest
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--replay',type=Path);a=p.parse_args()
    if a.replay:
        capture=json.loads((a.replay/'raw.json').read_text(encoding='utf-8'))
        saved=json.loads((a.replay/'audit.json').read_text(encoding='utf-8'))
        result=assess(capture)
        if seal(result)!=saved:raise ValueError('Availability audit replay mismatch')
        print(json.dumps({'replay_equal':True,'sha256':digest(result)}));return
    root=Path(__file__).resolve().parents[1]/'artifacts/local/availability-audits'/str(uuid4());root.mkdir(parents=True)
    capture=collect();result=assess(capture)
    for name,value in [('raw.json',capture),('audit.json',seal(result))]:
        with (root/name).open('x',encoding='utf-8') as stream:json.dump(value,stream,ensure_ascii=False,sort_keys=True)
    print(json.dumps({'folder':str(root),'sha256':digest(result),'sources':[(r['source_id'],r['status'],r['reason']) for r in result['sources']]},indent=2))


if __name__=='__main__':main()
