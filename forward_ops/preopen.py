"""Official daily policy and version-aware replay, outside the frozen model."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4
from .admission import KST,eligible
from .source_timing import POLICY,VERSION
from .runtime import ROOT,BASELINE_ROOT,LOCK_PATH,bootstrap,operations_manifest,harvest_outcomes
from .store import read_seal,digest

LEGACY_COMMIT='f13d6c18ee8356ed804d091c5ddbe424414eb121'


def invoke(request,folder,script):
    path=folder/'worker-request.json'
    with path.open('x',encoding='utf-8') as stream:json.dump(request,stream)
    result=subprocess.run([sys.executable,str(script),str(path)],cwd=ROOT,text=True,capture_output=True,timeout=300)
    with (folder/'worker.log').open('x',encoding='utf-8') as stream:stream.write(result.stdout+result.stderr)
    if result.returncode:raise RuntimeError('Frozen worker failed: '+str(folder/'worker.log'))
    return json.loads((folder/'result.json').read_text(encoding='utf-8'))


def run_official(store,exception_date=None,exception_reason=None,now=None):
    started=now or datetime.now(timezone.utc)
    if not eligible(started,exception_date,exception_reason):return {'status':'skipped','reason':'Outside 07:00–08:59 KST automatic window'}
    session=started.astimezone(KST).date().isoformat();key='daily:'+session
    def existing():return next((r for r in store.records('runs') if r['case_key']==key),None)
    match=existing()
    if match:return {'status':'already_sealed','run_id':match['system']['run_id']}
    marker=store.path('active.lock')
    with marker.open('x') as stream:stream.write(started.isoformat())
    attempt=str(uuid4());folder=store.path('attempts/'+attempt);folder.mkdir(parents=True)
    try:
        match=existing()
        if match:return {'status':'already_sealed','run_id':match['system']['run_id']}
        lock=bootstrap();manifest=operations_manifest()
        policy={'version':POLICY,'nominal_time':'07:00','timezone':'Asia/Seoul','forecast_session':session,
            'exception_date':exception_date,'exception_reason':exception_reason,'actual_started_at':started.isoformat(),
            'run_kind':'current_time_exception' if exception_date else 'official_preopen',
            'operations_manifest_sha256':digest(manifest)}
        request={'case_key':key,'review_key':'session:'+session,'kind':'daily','event_id':None,'started_at':started.isoformat(),
            'operations_version':VERSION,'operations_manifest':manifest,'operating_policy':policy,
            'shadow':store.shadow(started),'model_influence':False}
        store.write('attempts/'+attempt+'/operations-request.json',request)
        result=invoke({'command':'collect','baseline_root':str(BASELINE_ROOT),'lock':lock,'output':str(folder),'policy':policy},
            folder,ROOT/'forward_ops/preopen_worker.py')
        if operations_manifest()!=manifest:raise ValueError('Operations changed during run')
        if result['status']!='success':
            store.write('logs/'+attempt+'.json',{**result,'case_key':key});return result
        system=read_seal(folder/'prediction-journal.json')
        store.write('runs/'+system['run_id']+'.json',{**request,'run_id':system['run_id'],'system':system,
            'baseline_journal_sha256':result['sha256'],'raw_folder':str(folder),
            'eligible_case':any(h['final'] is not None for h in system['horizons']),'baseline_lock_sha256':digest(lock)})
        count=len(harvest_outcomes(store,folder))
        store.write('logs/'+attempt+'.json',{**result,'case_key':key,'outcomes_created':count})
        return {**result,'outcomes_created':count}
    except Exception as exc:
        if not store.path('logs/'+attempt+'.json').exists():store.write('logs/'+attempt+'.json',{'status':'error','case_key':key,'error':str(exc)})
        raise
    finally:marker.unlink()


def legacy_worker(record,commit=LEGACY_COMMIT,script='forward_ops/worker.py'):
    manifest=record['operations_manifest']
    if not manifest or 'forward_ops/worker.py' not in manifest:raise ValueError('Missing recorded operations manifest')
    contents={}
    for path,sha in manifest.items():
        if not (path.startswith('forward_ops/') or path=='scripts/install-forward-schedule.ps1') or '..' in Path(path).parts:
            raise ValueError('Unexpected historical operations path')
        body=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT).decode('utf-8').replace('\r\n','\n')
        if hashlib.sha256(body.encode()).hexdigest()!=sha:raise ValueError('Recorded legacy operations version mismatch')
        contents[path]=body
    folder=ROOT/'artifacts/local/operations-versions'/commit
    for path,body in contents.items():
        target=folder/path;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            if target.read_text(encoding='utf-8')!=body:raise ValueError('Historical worker cache changed')
        else:
            with target.open('x',encoding='utf-8') as stream:stream.write(body)
    return folder/script


def replay_any(store,run_id):
    record=store.run(run_id);bootstrap()
    folder=store.path('replays/'+str(uuid4()));folder.mkdir(parents=True)
    request={'command':'replay','baseline_root':str(BASELINE_ROOT),'lock':record['system']['lock'],'output':str(folder),
        'bundle_path':str(Path(record['raw_folder'])/'raw-bundle.json')}
    version=record['operations_version']
    if version==VERSION:
        if record['operations_manifest']!=operations_manifest():raise ValueError('Operations replay version drift')
        request['policy']=record['operating_policy'];script=ROOT/'forward_ops/preopen_worker.py'
    elif version=='forward-ops-v1.1.0':
        request['policy']=record['operating_policy']
        script=legacy_worker(record,'6479777b64324bdbfad843dd6cd60a6fa4ae0e58','forward_ops/preopen_worker.py')
    elif version in ('forward-ops-v1.0.0','original-live-forward-v2'):
        request['daily_date']=None
        script=(legacy_worker(record) if record.get('operations_manifest')!=operations_manifest() else ROOT/'forward_ops/worker.py') if version=='forward-ops-v1.0.0' else ROOT/'forward_ops/worker.py'
    else:raise ValueError('Unrecognized operations version')
    result=invoke(request,folder,script)
    if result.get('sha256')!=record['baseline_journal_sha256']:raise ValueError('Frozen replay mismatch')
    result={'run_id':run_id,'replay_equal':True,'sha256':result['sha256']}
    store.write(str(folder.relative_to(store.root))+'/verification.json',result)
    return result
