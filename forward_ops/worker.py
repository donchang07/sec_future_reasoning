"""Isolated worker: loads the pinned reasoning tree, never shadow/human data."""
import json
import sys
from pathlib import Path


def main():
    request=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    allowed={'command','baseline_root','lock','output','daily_date','bundle_path'}
    if set(request)-allowed:raise ValueError('shadow/human/unknown input forbidden in model worker')
    baseline=Path(request['baseline_root']).resolve();sys.path.insert(0,str(baseline))
    from reasoning import live_v2 as model
    if not Path(model.__file__).resolve().is_relative_to(baseline):raise ValueError('wrong model import root')
    model.verify_lock(request['lock'],baseline)
    output=Path(request['output']);output.mkdir(parents=True,exist_ok=True)
    if request['command']=='collect':
        from concurrent.futures import ThreadPoolExecutor
        from reasoning.act_sources import DOCUMENTS,collect_document
        with ThreadPoolExecutor(max_workers=4) as pool:documents=tuple(pool.map(collect_document,DOCUMENTS))
        bundle=model.InputBundle(market=model.collect_snapshot(),documents=documents,lock=request['lock'])
        model.write_immutable(output/'raw-bundle.json',bundle)
    else:bundle=model.InputBundle.model_validate_json(Path(request['bundle_path']).read_text(encoding='utf-8'))
    from reasoning.live import prepare
    from zoneinfo import ZoneInfo
    fixture,_,_=prepare(bundle.market)
    last=fixture.bars['1d'][-1] if fixture.bars['1d'] else None
    if request.get('daily_date') and (last is None or last.closed_at.astimezone(ZoneInfo('Asia/Seoul')).date().isoformat()!=request['daily_date']):
        model.write_immutable(output/'result.json',{'status':'not_ready','reason':'No completed preferred daily bar for requested session','last':last.closed_at.isoformat() if last else None})
        return
    journal=model.evaluate(bundle)  # THE ORIGINAL v2 PATH, unchanged and one invocation.
    model.verify_lock(request['lock'],baseline)
    model.write_immutable(output/'prediction-journal.json',model.seal(journal))
    raw=next((r for r in bundle.market.sources if r.source.source_id=='preferred_daily'),None)
    model.write_immutable(output/'closes.json',{'bars':[b.model_dump(mode='json') for b in fixture.bars['1d']],
        'collected_at':raw.collected_at.isoformat() if raw else None,'source_ref':'raw:'+raw.sha256 if raw else None})
    model.write_immutable(output/'result.json',{'status':'success','run_id':journal['run_id'],'sha256':model.digest(journal)})


if __name__=='__main__':main()
