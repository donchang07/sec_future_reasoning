"""python -m forward_ops: operational commands, never tuning commands."""
import argparse
import json
from datetime import datetime,timezone
from pathlib import Path
from .store import Store
from .runtime import DEFAULT_STORE,bootstrap,run_daily,import_baseline,replay,harvest_outcomes


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=('bootstrap','daily','event','position','event-input','human','import','replay','outcomes','evaluate','serve'))
    p.add_argument('--store',type=Path,default=DEFAULT_STORE);p.add_argument('--input',type=Path)
    p.add_argument('--event-id');p.add_argument('--run-id');p.add_argument('--port',type=int,default=8677)
    a=p.parse_args();s=Store(a.store);now=datetime.now(timezone.utc)
    if a.command=='bootstrap':result={'baseline_verified':bool(bootstrap())}
    elif a.command in ('daily','event'):result=run_daily(s,a.command,a.event_id)
    elif a.command=='position':
        value=json.loads(a.input.read_text(encoding='utf-8'));rows=value if isinstance(value,list) else [value]
        from .models import Position
        positions=[Position.model_validate(row) for row in rows]
        if any(row.released_at>now for row in positions):raise ValueError('batch contains future source')
        result={'position_ids':[s.add_position(row,now) for row in positions],'model_influence':False}
    elif a.command=='event-input':result={'event_id':s.add_event(json.loads(a.input.read_text(encoding='utf-8')),now),'model_influence':False}
    elif a.command=='human':result={'human_id':s.add_human(json.loads(a.input.read_text(encoding='utf-8')),now),'model_influence':False}
    elif a.command=='import':result={'run_id':import_baseline(s,a.input)}
    elif a.command=='replay':result=replay(s,a.run_id)
    elif a.command=='outcomes':
        r=s.run(a.run_id);result={'outcomes_created':len(harvest_outcomes(s,Path(r['raw_folder'])))}
    elif a.command=='serve':
        from .web import serve
        serve(s,a.port);return
    else:result=s.evaluation()
    if __import__('sys').stdout is not None:print(json.dumps(result,ensure_ascii=False,indent=2))
    if isinstance(result,dict) and result.get('status')=='not_ready':raise SystemExit(2)


if __name__=='__main__':main()
