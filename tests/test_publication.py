import json,subprocess
from pathlib import Path
import pytest
from forward_ops.store import seal,digest
from publication.publisher import export_record,sync_git


def run_record(root):
    folder=root/'artifacts/local/run';folder.mkdir(parents=True)
    j={'run_id':'00000000-0000-0000-0000-000000000001','data_mode':'live_forward','contract_version':'real-world-contract-v2.0.0',
        'mapping_version':'test','held':False,'prediction_timestamp':'2026-09-11T07:00:10+09:00','data_cutoff':'2026-09-11T07:00:10+09:00',
        'horizons':[],'p0':None,'raw_observations':[],'sources':[],'findings':[]}
    (folder/'prediction-journal.json').write_text(json.dumps(seal(j)),encoding='utf-8')
    return {'system':j,'raw_folder':str(folder),'baseline_journal_sha256':digest(j),'shadow':{'private':'DO NOT PUBLISH'},'human':{'private':'DO NOT PUBLISH'}}


def test_export_exact_journal_and_excludes_outer_private(tmp_path):
    r=run_record(tmp_path);paths=export_record(r,tmp_path)
    p=next(p for p in paths if p.name=='journal.json')
    assert p.read_bytes()==(Path(r['raw_folder'])/'prediction-journal.json').read_bytes()
    assert all('DO NOT PUBLISH' not in p.read_text(encoding='utf-8') for p in paths)
    assert len(paths)==2 and export_record(r,tmp_path)==paths


@pytest.mark.parametrize('changes',[{'held':True},{'shadow':{}},{'api_key':'secret'},{'raw_observations':[{'source_id':'human_supplied'}]}])
def test_private_or_unknown_journal_refused(tmp_path,changes):
    r=run_record(tmp_path);r['system'].update(changes);r['baseline_journal_sha256']=digest(r['system'])
    with pytest.raises(ValueError):export_record(r,tmp_path)


def test_immutable_publication_collision(tmp_path):
    r=run_record(tmp_path);paths=export_record(r,tmp_path);paths[0].write_text('tampered')
    with pytest.raises(ValueError,match='immutable'):export_record(r,tmp_path)


def git(root,*args):
    return subprocess.check_output(['git',*args],cwd=root,stderr=subprocess.STDOUT,text=True).strip()


def repo(tmp_path):
    bare=tmp_path/'remote.git';git(tmp_path,'init','--bare',str(bare))
    root=tmp_path/'repo';git(tmp_path,'init','-b','main',str(root))
    git(root,'config','user.name','Test');git(root,'config','user.email','test@example.invalid')
    (root/'initial.txt').write_text('initial');git(root,'add','initial.txt');git(root,'commit','-m','initial')
    git(root,'remote','add','origin',str(bare));git(root,'push','-u','origin','main')
    return root,bare


def output(root):
    p=root/'docs/predictions/test.txt';p.parent.mkdir(parents=True);p.write_text('public output');return p


def test_git_scope_idempotency_and_unstaged_preservation(tmp_path):
    root,bare=repo(tmp_path);p=output(root);(root/'initial.txt').write_text('private edit')
    first=sync_git(root,[p]);head=git(root,'rev-parse','HEAD')
    assert first['pushed'] and git(bare,'rev-parse','main')==head
    assert git(root,'diff','--name-only')=='initial.txt'
    assert not sync_git(root,[p])['pushed'] and git(root,'rev-parse','HEAD')==head


def test_unrelated_staged_change_is_not_committed(tmp_path):
    root,_=repo(tmp_path);p=output(root);(root/'initial.txt').write_text('private edit');git(root,'add','initial.txt')
    head=git(root,'rev-parse','HEAD')
    with pytest.raises(ValueError,match='staged'):sync_git(root,[p])
    assert git(root,'rev-parse','HEAD')==head and git(root,'diff','--cached','--name-only')=='initial.txt'


def test_failed_push_retries_same_public_commit(tmp_path,monkeypatch):
    from publication import publisher
    root,bare=repo(tmp_path);p=output(root);original=publisher.git
    def failing(path,*args):
        if args[0]=='push':raise RuntimeError('offline')
        return original(path,*args)
    monkeypatch.setattr(publisher,'git',failing)
    with pytest.raises(RuntimeError):sync_git(root,[p])
    head=git(root,'rev-parse','HEAD');monkeypatch.setattr(publisher,'git',original)
    assert sync_git(root,[p])['pushed'] and git(root,'rev-parse','HEAD')==head
    assert git(bare,'rev-parse','main')==head


def test_unrelated_unpushed_commit_refused(tmp_path):
    root,_=repo(tmp_path);p=output(root)
    (root/'initial.txt').write_text('unpublished work');git(root,'add','initial.txt');git(root,'commit','-m','private work')
    with pytest.raises(ValueError,match='[Uu]nrelated'):sync_git(root,[p])


def test_outcome_hash_binding_and_immutability(tmp_path):
    from forward_ops.store import Store
    r=run_record(tmp_path);s=Store(tmp_path/'artifacts/local/store');rid=r['system']['run_id']
    s.write('outcomes/'+rid+'/1d.json',{'run_id':rid,'prediction_sha256':'wrong','horizon':'1d'})
    with pytest.raises(ValueError,match='Outcome'):export_record(r,tmp_path,s)


def test_divergent_remote_never_forced(tmp_path):
    root,bare=repo(tmp_path);p=output(root)
    git(root,'add','docs/predictions/test.txt');git(root,'commit','-m','pending publication')
    other=tmp_path/'other';git(tmp_path,'clone','--branch','main',str(bare),str(other))
    git(other,'config','user.name','Test');git(other,'config','user.email','test@example.invalid')
    (other/'remote.txt').write_text('remote work');git(other,'add','remote.txt');git(other,'commit','-m','remote work');git(other,'push')
    remote=git(bare,'rev-parse','main')
    with pytest.raises(ValueError,match='diverged'):sync_git(root,[p])
    assert git(bare,'rev-parse','main')==remote
