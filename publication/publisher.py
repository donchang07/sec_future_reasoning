"""Allowlisted immutable exports and scoped, retryable non-forced Git publication."""
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from uuid import UUID
from zoneinfo import ZoneInfo
from forward_ops.store import read_seal,digest

FIELDS=set('bar_boundaries contract_version data_cutoff data_mode document_status executions findings held held_basis horizons lock mapping_version outcome_due p0 prediction_timestamp prior_provenance raw_bundle_hash raw_observations run_id sources versions market_cutoffs operating_policy availability_diagnostic availability_raw_hash data_timing_version'.split())
SOURCES=set('common_daily dram_spot dxy exports_10 exports_20 exports_month kospi preferred_daily samsung_bs samsung_cf samsung_soi treasury_10y usdkrw'.split())
OUTCOME_FIELDS=set('run_id prediction_sha256 data_mode horizon due_at effective_at released_at collected_at source_ref price p0 return measurement_delay_hours policy_version'.split())
PRIVATE_KEYS={'api_key','password','access_token','authorization','credentials','submitter','human','shadow','human_forecast'}


def check_public(value):
    if isinstance(value,dict):
        if PRIVATE_KEYS.intersection(k.lower() for k in value):raise ValueError('Private field in public output')
        for v in value.values():check_public(v)
    elif isinstance(value,list):
        for v in value:check_public(v)
    elif isinstance(value,str) and re.search(r'(?i)([?&](api_key|token|access_token)=|bearer\s+[A-Za-z0-9_-]{12,}|https?://[^/\s]+:[^/\s]+@)',value):
        raise ValueError('Credential pattern in output')


def immutable(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if path.read_bytes()!=content:raise ValueError('immutable publication collision: '+path.name)
    else:
        with path.open('xb') as stream:stream.write(content)


def export_record(record,root,store=None):
    root=Path(root).resolve();j=record['system'];rid=str(UUID(j['run_id']))
    if set(j)-FIELDS or j.get('held') is not False or j.get('data_mode')!='live_forward' or j.get('contract_version')!='real-world-contract-v2.0.0':
        raise ValueError('Unsupported/private system journal')
    if any(s.get('source_id') not in SOURCES for s in j['raw_observations']):raise ValueError('Unapproved public source')
    check_public(j)
    if digest(j)!=record['baseline_journal_sha256']:raise ValueError('Registered journal hash mismatch')
    folder=Path(record['raw_folder']).resolve()
    if not folder.is_relative_to(root/'artifacts/local'):raise ValueError('Journal outside local artifact store')
    original=folder/'prediction-journal.json'
    if read_seal(original)!=j:raise ValueError('Original journal differs from registered journal')
    stamp=datetime.fromisoformat(j['prediction_timestamp'])
    if stamp.tzinfo is None:raise ValueError('Naive prediction timestamp')
    day=stamp.astimezone(ZoneInfo('Asia/Seoul')).date().isoformat()
    destination=root/'docs/predictions'/day/rid;paths=[]
    from reasoning.live_v2 import report
    text='# Published frozen prediction\n\nThis is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.\n\n'+report(j)
    for name,content in [('journal.json',original.read_bytes()),('explainability.md',text.encode())]:
        path=destination/name;immutable(path,content);paths.append(path)
    if store:
        for original_outcome in sorted(store.path('outcomes/'+rid).glob('*.json')):
            outcome=read_seal(original_outcome)
            if set(outcome)-OUTCOME_FIELDS or outcome.get('prediction_sha256')!=digest(j) or outcome.get('run_id')!=rid or outcome.get('horizon') not in ('1d','1w','1m','1y'):
                raise ValueError('Outcome public fields or prediction link invalid')
            check_public(outcome)
            path=destination/'outcomes'/(outcome['horizon']+'.json');immutable(path,original_outcome.read_bytes());paths.append(path)
    return paths


def git(root,*args):
    env={**os.environ,'GIT_TERMINAL_PROMPT':'0','GCM_INTERACTIVE':'never'}
    result=subprocess.run(['git',*args],cwd=root,env=env,capture_output=True,text=True,timeout=90)
    if result.returncode:raise RuntimeError('git '+args[0]+' failed: '+result.stderr.strip())
    return result.stdout.strip()


def managed(path):return path.startswith('docs/predictions/') and '..' not in Path(path).parts


def pending_is_public(root,remote,head,allowed):
    try:git(root,'merge-base','--is-ancestor',remote,head)
    except RuntimeError as exc:raise ValueError('Remote history diverged; no automatic merge or force push') from exc
    for line in git(root,'rev-list','--parents',remote+'..'+head).splitlines():
        parts=line.split()
        if len(parts)!=2:raise ValueError('Unrelated merge commit pending')
        paths=git(root,'diff-tree','--no-commit-id','--name-only','-r',parts[0]).splitlines()
        if not paths or not all(managed(p) and p in allowed for p in paths):raise ValueError('Unrelated unpushed commit; publication deferred')


def sync_git(root,paths):
    root=Path(root).resolve();names=sorted({p.resolve().relative_to(root).as_posix() for p in paths})
    if not names or not all(managed(p) for p in names):raise ValueError('Unexpected publication scope')
    if git(root,'branch','--show-current')!='main':raise ValueError('Publication requires main branch')
    staged=git(root,'diff','--cached','--name-only').splitlines()
    if set(staged)-set(names):raise ValueError('Unrelated staged paths; publication deferred')
    git(root,'fetch','origin','main')
    remote=git(root,'rev-parse','refs/remotes/origin/main');head=git(root,'rev-parse','HEAD')
    if head!=remote:pending_is_public(root,remote,head,set(names))
    # NUL pathspec avoids command length limits and shell/path interpretation.
    with tempfile.NamedTemporaryFile(delete=False) as stream:
        spec=Path(stream.name);stream.write(b'\0'.join(n.encode() for n in names)+b'\0')
    try:
        git(root,'add','--pathspec-from-file='+str(spec),'--pathspec-file-nul')
        changed=git(root,'diff','--cached','--name-only').splitlines()
        if set(changed)-set(names):raise ValueError('Staged scope changed during publication')
        if changed:
            git(root,'commit','--only','-m','docs: publish sealed prediction results','--pathspec-from-file='+str(spec),'--pathspec-file-nul')
        commit=git(root,'rev-parse','HEAD')
        pending_is_public(root,remote,commit,set(names))
        if commit!=remote:git(root,'push','origin',commit+':refs/heads/main')
        return {'pushed':commit!=remote,'commit':commit,'files':len(names)}
    finally:spec.unlink()


def publish(root,store):
    paths=[];links=[]
    for record in store.runs():
        exported=export_record(record,root,store);paths.extend(exported)
        j=record['system'];relative=exported[0].parent.relative_to(root/'docs/predictions').as_posix()
        links.append(f"| {j['prediction_timestamp']} | [{j['run_id']}]({relative}/explainability.md) | [Journal]({relative}/journal.json) |")
    if not paths:return {'pushed':False,'reason':'No completed registered public runs'}
    index=root/'docs/predictions/README.md'
    index.write_text('# Published Prediction Results\n\nAutomatically published within approximately five minutes of local completion when GitHub is reachable. Original journals remain immutable; linked outcomes are separate.\n\n| Prediction timestamp | Explainability | Sealed record |\n|---|---|---|\n'+'\n'.join(reversed(links))+'\n',encoding='utf-8',newline='\n')
    attrs=root/'docs/predictions/.gitattributes';immutable(attrs,b'* -text\n')
    return sync_git(root,paths+[index,attrs])
