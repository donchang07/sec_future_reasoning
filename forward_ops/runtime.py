"""Scheduling, frozen worker invocation and immutable forward-case registration."""
import json
import hashlib
import shutil
import subprocess
import sys
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4
from zoneinfo import ZoneInfo
from .store import Store,read_seal,digest
from .evaluation import select_close

ROOT=Path(__file__).resolve().parents[1]
BASELINE_COMMIT='73c30f77608813bafcecf137e413e88b3c01d7cf'
LOCK_PATH=ROOT/'docs/03-analysis/live-forward-v2.pre-run-lock.json'
DEFAULT_STORE=ROOT/'artifacts/local/forward-evaluation-v1'
BASELINE_ROOT=ROOT/'artifacts/local/frozen-v2-baseline'
KST=ZoneInfo('Asia/Seoul')


def operations_manifest():
    paths=[p for p in (ROOT/'forward_ops').rglob('*') if p.suffix in ('.py','.js','.css','.html')]
    paths += [ROOT/'scripts/install-forward-schedule.ps1']
    return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest() for p in sorted(paths) if p.exists()}


def bootstrap():
    lock=read_seal(LOCK_PATH)
    if not BASELINE_ROOT.exists():
        subprocess.run(['git','worktree','add','--detach',str(BASELINE_ROOT),BASELINE_COMMIT],cwd=ROOT,check=True,capture_output=True,text=True)
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=BASELINE_ROOT,text=True).strip()
    if head!=BASELINE_COMMIT:raise ValueError('baseline worktree commit mismatch')
    for name,sha in lock['historical_journals'].items():
        source=ROOT/name;target=BASELINE_ROOT/name
        if hashlib.sha256(source.read_bytes()).hexdigest()!=sha:raise ValueError('historical source changed')
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest()!=sha:raise ValueError('historical replay copy changed')
        else:shutil.copyfile(source,target)
    return lock


def eligible_session(now):
    local=now.astimezone(KST)
    return local.weekday()<5 and (local.hour,local.minute)>=(15,50)


def worker(request,folder):
    request_path=folder/'worker-request.json'
    with request_path.open('x',encoding='utf-8') as f:json.dump(request,f)
    result=subprocess.run([sys.executable,str(ROOT/'forward_ops/worker.py'),str(request_path)],cwd=ROOT,text=True,capture_output=True,timeout=240)
    with (folder/'worker.log').open('x',encoding='utf-8') as f:f.write(result.stdout+result.stderr)
    if result.returncode:raise RuntimeError('Frozen worker failed; inspect '+str(folder/'worker.log'))
    return json.loads((folder/'result.json').read_text(encoding='utf-8'))


def harvest_outcomes(store,folder,now=None):
    now=now or datetime.now(timezone.utc)
    raw=json.loads((folder/'closes.json').read_text(encoding='utf-8'))
    if raw['collected_at'] is None:return []
    collected=datetime.fromisoformat(raw['collected_at']);created=[]
    for run in store.runs():
        j=run['system']
        for h,due in j['outcome_due'].items():
            if store.path('outcomes/'+j['run_id']+'/'+h+'.json').exists():continue
            selected=select_close(raw['bars'],datetime.fromisoformat(due),min(collected,now))
            if selected:
                created.append(store.add_outcome(j['run_id'],h,selected,collected,raw['source_ref'],now))
    return created


def run_daily(store,kind='daily',event_id=None,now=None):
    started=now or datetime.now(timezone.utc)
    if kind not in ('daily','event'):raise ValueError('run kind')
    session=started.astimezone(KST).date().isoformat()
    if kind=='daily' and not eligible_session(started):return {'status':'skipped','reason':'Outside completed Korean weekday close window'}
    if kind=='event' and not event_id:raise ValueError('event run requires a stored actual event')
    key=('daily:'+session) if kind=='daily' else 'event:'+event_id
    matches=[r for r in store.runs() if r['case_key']==key]
    if matches:return {'status':'already_sealed','run_id':matches[0]['system']['run_id']}
    marker=store.path('active.lock')
    try:
        with marker.open('x') as f:f.write(str(started))
    except FileExistsError:raise RuntimeError('Another run is active; inspect active.lock before manual recovery')
    attempt=str(uuid4());folder=store.path('attempts/'+attempt);folder.mkdir(parents=True)
    try:
        lock=bootstrap();manifest=operations_manifest()
        shadow=store.shadow(started,event_id)  # Snapshot received evidence BEFORE collection.
        request={'case_key':key,'review_key':'session:'+session if kind=='daily' else key,'kind':kind,'event_id':event_id,'started_at':started.isoformat(),
            'operations_version':'forward-ops-v1.0.0','operations_manifest':manifest,'shadow':shadow,'model_influence':False}
        store.write('attempts/'+attempt+'/operations-request.json',request)
        result=worker({'command':'collect','baseline_root':str(BASELINE_ROOT),'lock':lock,'output':str(folder),
            'daily_date':session if kind=='daily' else None},folder)
        if result['status']!='success':
            store.write('logs/'+attempt+'.json',{**result,'case_key':key,'attempt':attempt,'at':datetime.now(timezone.utc).isoformat()})
            return result
        if operations_manifest()!=manifest:raise ValueError('Operations changed during run')
        system=read_seal(folder/'prediction-journal.json')
        numeric=any(h['final'] is not None for h in system['horizons'])
        meaningful=kind=='daily' or (shadow['event'] is not None and shadow['event']['surprise'] is not None)
        record={**request,'run_id':system['run_id'],'system':system,'baseline_journal_sha256':result['sha256'],
            'raw_folder':str(folder),'eligible_case':numeric and meaningful,'baseline_lock_sha256':digest(lock)}
        store.write('runs/'+system['run_id']+'.json',record)
        outcomes=harvest_outcomes(store,folder)
        store.write('logs/'+attempt+'.json',{'status':'success','case_key':key,'run_id':system['run_id'],'outcomes_created':len(outcomes),'at':datetime.now(timezone.utc).isoformat()})
        return {'status':'success','run_id':system['run_id'],'outcomes_created':len(outcomes)}
    except Exception as exc:
        if not store.path('logs/'+attempt+'.json').exists():store.write('logs/'+attempt+'.json',{'status':'error','case_key':key,'error':str(exc),'at':datetime.now(timezone.utc).isoformat()})
        raise
    finally:marker.unlink()


def import_baseline(store,path):
    j=read_seal(path)
    if j.get('data_mode')!='live_forward' or j.get('contract_version')!='real-world-contract-v2.0.0':raise ValueError('not a v2 forward journal')
    rid=j['run_id'];target=store.path('runs/'+rid+'.json')
    if target.exists():return rid
    record={'run_id':rid,'case_key':'imported:'+rid,'review_key':'session:'+datetime.fromisoformat(j['data_cutoff']).astimezone(KST).date().isoformat(),'kind':'imported','eligible_case':any(h['final'] is not None for h in j['horizons']),
        'system':j,'baseline_journal_sha256':digest(j),'shadow':{'positioning':{'rows':[],'conflicts':[],'interactions':[]},'event':None,'model_influence':False},
        'raw_folder':str(Path(path).resolve().parent),'operations_version':'original-live-forward-v2','note':'Original prediction copied unchanged; no new inference.'}
    store.write('runs/'+rid+'.json',record);return rid


def replay(store,run_id):
    record=store.run(run_id)
    if record['kind']=='imported':
        bundle=Path(record['raw_folder'])/'raw-bundle.json'
        lock=record['system']['lock']
    else:
        if record['operations_manifest']!=operations_manifest():raise ValueError('Operations replay version drift; use recorded version')
        bundle=Path(record['raw_folder'])/'raw-bundle.json';lock=read_seal(LOCK_PATH)
    bootstrap();folder=store.path('replays/'+str(uuid4()));folder.mkdir(parents=True)
    result=worker({'command':'replay','baseline_root':str(BASELINE_ROOT),'lock':lock,'output':str(folder),
        'bundle_path':str(bundle),'daily_date':None},folder)
    if result['sha256']!=record['baseline_journal_sha256']:raise ValueError('frozen replay mismatch')
    store.write(str(folder.relative_to(store.root))+'/verification.json',{'run_id':run_id,'replay_equal':True,'sha256':result['sha256']})
    return {'run_id':run_id,'replay_equal':True,'sha256':result['sha256']}
