"""Isolated preopen admission followed by the unchanged frozen v2 evaluator."""
import json
import sys
from pathlib import Path
from admission import eligible,KST
from source_timing import POLICY
from timing_evaluate import project,evaluate
import availability_audit


def main():
    request=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    allowed={'command','baseline_root','lock','output','bundle_path','policy'}
    if set(request)-allowed:raise ValueError('shadow/human/unknown input forbidden in model worker')
    baseline=Path(request['baseline_root']).resolve();sys.path.insert(0,str(baseline))
    from reasoning import live_v2 as model
    if not Path(model.__file__).resolve().is_relative_to(baseline):raise ValueError('wrong model root')
    model.verify_lock(request['lock'],baseline)
    output=Path(request['output']);output.mkdir(parents=True,exist_ok=True)
    if request['command']=='collect':
        from concurrent.futures import ThreadPoolExecutor
        from reasoning.act_sources import DOCUMENTS,collect_document
        with ThreadPoolExecutor(max_workers=4) as pool:documents=tuple(pool.map(collect_document,DOCUMENTS))
        diagnostics=availability_audit.collect()
        model.write_immutable(output/'availability-raw.json',diagnostics)
        bundle=model.InputBundle(market=model.collect_snapshot(),documents=documents,lock=request['lock'])
        model.write_immutable(output/'raw-bundle.json',bundle)
    else:
        bundle=model.InputBundle.model_validate_json(Path(request['bundle_path']).read_text(encoding='utf-8'))
        diagnostics=json.loads((Path(request['bundle_path']).parent/'availability-raw.json').read_text(encoding='utf-8'))
    policy=request['policy'];cutoff=bundle.market.data_cutoff
    if policy['version']!=POLICY:raise ValueError('Worker policy version mismatch')
    if cutoff.astimezone(KST).date().isoformat()!=policy['forecast_session'] or not eligible(cutoff,policy['exception_date'],policy['exception_reason']):
        model.write_immutable(output/'result.json',{'status':'not_ready','reason':'Collection finished outside authorized session/window'});return
    try:admitted,audit=project(bundle,policy['forecast_session'])
    except ValueError as exc:
        model.write_immutable(output/'result.json',{'status':'not_ready','reason':str(exc)});return
    model.write_immutable(output/'admitted-bundle.json',admitted)
    model.write_immutable(output/'admission.json',audit)
    journal=evaluate(admitted,bundle)
    journal.update(operating_policy=policy,market_cutoffs=audit)
    journal['availability_diagnostic']=availability_audit.assess(diagnostics,cutoff)
    journal['availability_raw_hash']=model.digest(diagnostics)
    journal['findings']+=['OP-F02: prior-close intraday bars remain subject to frozen freshness, including midday exceptions.']
    model.verify_lock(request['lock'],baseline)
    model.write_immutable(output/'prediction-journal.json',model.seal(journal))
    (output/'explainability.md').write_text(model.report(journal),encoding='utf-8')
    from reasoning.live import prepare
    fixture,_,_=prepare(bundle.market)
    raw=next((r for r in bundle.market.sources if r.source.source_id=='preferred_daily'),None)
    model.write_immutable(output/'closes.json',{'bars':[b.model_dump(mode='json') for b in fixture.bars['1d']],
        'collected_at':raw.collected_at.isoformat() if raw else None,'source_ref':'raw:'+raw.sha256 if raw else None})
    model.write_immutable(output/'result.json',{'status':'success','run_id':journal['run_id'],'sha256':model.digest(journal)})


if __name__=='__main__':main()
