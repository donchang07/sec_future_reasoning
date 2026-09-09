"""Append-only local records. Human and shadow stores never feed the model worker."""
import hashlib
import json
from datetime import datetime,timezone
from math import isfinite
from pathlib import Path
from .models import Position,Event,position_diagnostics,event_diagnostic
from .evaluation import score,metrics,review_gate,shadow_comparison,DAYS


def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def seal(value):return {'snapshot':value,'sha256':digest(value)}
def read_seal(path):
    value=json.loads(Path(path).read_text(encoding='utf-8'))
    if digest(value['snapshot'])!=value['sha256']:raise ValueError('record seal mismatch')
    return value['snapshot']


class Store:
    def __init__(self,root):self.root=Path(root).resolve();self.root.mkdir(parents=True,exist_ok=True)

    def path(self,name):
        p=(self.root/name).resolve()
        if not p.is_relative_to(self.root):raise ValueError('path outside store')
        return p

    def write(self,name,value):
        p=self.path(name);p.parent.mkdir(parents=True,exist_ok=True)
        with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(seal(value),f,ensure_ascii=False,sort_keys=True,allow_nan=False)
        return p

    def records(self,folder):return [read_seal(p) for p in sorted(self.path(folder).glob('*.json'))]
    def runs(self):return sorted(self.records('runs'),key=lambda r:r['system']['data_cutoff'])
    def run(self,run_id):return read_seal(self.path('runs/'+str(run_id)+'.json'))

    def add_position(self,position,received):
        position=Position.model_validate(position)
        if position.released_at>received:raise ValueError('position after receipt')
        data={**position.model_dump(mode='json'),'received_at':received.isoformat()}
        if position.revision_of and not self.path('positioning/'+position.revision_of+'.json').exists():raise ValueError('unknown revision parent')
        key=digest(data)
        if not self.path('positioning/'+key+'.json').exists():self.write('positioning/'+key+'.json',data)
        return key

    def add_event(self,event,received):
        event=Event.model_validate(event);diagnostic=event_diagnostic(event,received)
        data={'event':event.model_dump(mode='json'),'received_at':received.isoformat(),'diagnostic':diagnostic}
        self.write('events/'+event.event_id+'.json',data)
        return event.event_id

    def shadow(self,cutoff,event_id=None):
        groups={};conflicts=[];superseded=[];received_refs=[]
        for row in self.records('positioning'):
            received=datetime.fromisoformat(row['received_at'])
            if received>cutoff:continue
            p=Position.model_validate({k:v for k,v in row.items() if k!='received_at'})
            if p.released_at>cutoff:continue
            groups.setdefault(p.key(),{}).setdefault((p.source_ref,p.submitter),[]).append(row)
        selected=[]
        for key,providers in groups.items():
            candidates=[]
            for rows in providers.values():
                latest=max(r['received_at'] for r in rows)
                candidates.extend(r for r in rows if r['received_at']==latest)
                superseded.extend(digest(r) for r in rows if r['received_at']!=latest)
            if len({r['value'] for r in candidates})>1:
                conflicts.append({'economic_key':list(key),'record_refs':[digest(r) for r in candidates]});continue
            r=min(candidates,key=digest);selected.append({k:v for k,v in r.items() if k!='received_at'})
            received_refs.append({'record_sha256':digest(r),'received_at':r['received_at']})
        # An unresolved latest-day conflict must not silently fall back to yesterday.
        selected=[r for r in selected if not any(tuple(c['economic_key'][1:])==
            (r['venue'],r['instrument'],r['investor'],r['measure'],r['expiry']) and c['economic_key'][0]>=r['trade_date'] for c in conflicts)]
        diagnostic=position_diagnostics(selected,cutoff);diagnostic['conflicts']=conflicts;diagnostic['superseded_refs']=superseded
        ev=None
        if event_id:
            record=read_seal(self.path('events/'+event_id+'.json'))
            if datetime.fromisoformat(record['received_at'])>cutoff:raise ValueError('event received after cutoff')
            ev=event_diagnostic(record['event'],cutoff)
        return {'positioning':diagnostic,'event':ev,'received_refs':received_refs,'cutoff':cutoff.isoformat(),'model_influence':False}

    def add_outcome(self,run_id,horizon,bar,collected_at,source_ref,now=None):
        r=self.run(run_id);j=r['system'];now=now or datetime.now(timezone.utc)
        if horizon not in ('1d',*DAYS):raise ValueError('unknown outcome horizon')
        due=datetime.fromisoformat(j['outcome_due'][horizon]);effective=datetime.fromisoformat(bar['closed_at'])
        if not due<=effective<=collected_at<=now:raise ValueError('outcome chronology')
        price=float(bar['close'])
        if not isfinite(price) or price<=0 or not source_ref or not j['p0'] or j['p0']['value']<=0:raise ValueError('outcome price/provenance')
        value={'run_id':run_id,'prediction_sha256':r['baseline_journal_sha256'],'data_mode':'live_forward','horizon':horizon,
            'due_at':due.isoformat(),'effective_at':effective.isoformat(),'released_at':None,'collected_at':collected_at.isoformat(),
            'source_ref':source_ref,'price':price,'p0':j['p0']['value'],'return':price/j['p0']['value']-1,
            'measurement_delay_hours':(effective-due).total_seconds()/3600,'policy_version':'forward-evaluation-v1.0.0'}
        self.write('outcomes/'+run_id+'/'+horizon+'.json',value)
        return value

    def add_human(self,data,received):
        allowed={'run_id','horizon','probabilities','confidence','human_id','rationale','revision_of'}
        if set(data)-allowed:raise ValueError('unknown human forecast fields')
        r=self.run(data['run_id']);j=r['system'];h=data['horizon']
        if h not in DAYS:raise ValueError('human horizon')
        p=data['probabilities']
        if set(p)!=set(('up','down','flat')) or any(not isinstance(v,(int,float)) or not isfinite(v) or not 0<=v<=1 for v in p.values()) or abs(sum(p.values())-1)>1e-9:
            raise ValueError('human probability vector')
        confidence=data['confidence']
        if not isinstance(confidence,(int,float)) or not isfinite(confidence) or not 0<=confidence<=1 or not data['human_id']:raise ValueError('human confidence/identity')
        if received<datetime.fromisoformat(j['data_cutoff']):raise ValueError('human forecast before referenced run')
        value={**data,'forecast_origin':'human','received_at':received.isoformat(),'blinded':False,
            'late':received>=datetime.fromisoformat(j['outcome_due'][h]),'model_influence':False,'prediction_sha256':r['baseline_journal_sha256']}
        if data.get('revision_of') and not self.path('human/'+data['revision_of']+'.json').exists():raise ValueError('unknown human revision')
        key=digest(value);self.write('human/'+key+'.json',value);return key

    def evaluation(self):
        rows={h:[] for h in DAYS};human={h:[] for h in DAYS};pending=0;ancillary=[]
        human_groups={}
        for record in self.records('human'):
            if not record['late']:
                k=(record['run_id'],record['horizon'],record['human_id'])
                if k not in human_groups or record['received_at']<human_groups[k]['received_at']:human_groups[k]=record
        runs=self.runs()
        for r in runs:
            j=r['system'];rid=j['run_id']
            for h in ('1d',*DAYS):
                path=self.path('outcomes/'+rid+'/'+h+'.json')
                if not path.exists():pending+=1;continue
                outcome=read_seal(path)
                if outcome['prediction_sha256']!=r['baseline_journal_sha256']:raise ValueError('outcome identity mismatch')
                if h=='1d':ancillary.append(outcome);continue
                forecast=next(x for x in j['horizons'] if x['horizon']==h)
                result=score(forecast,outcome['return'],j.get('held',False))
                if result:rows[h].append({**result,'run_id':rid,'shadow':r.get('shadow',{})})
                for (run_key,horizon_key,human_id),hf in human_groups.items():
                    if (run_key,horizon_key)!=(rid,h):continue
                    # Human probabilities are evaluated independently, without borrowing system action.
                    hr=score({'horizon':h,'final':{'probabilities':hf['probabilities'],'confidence':hf['confidence']},'decision':{'action':'HUMAN'}},outcome['return'])
                    human[h].append({**hr,'run_id':rid,'human_id':human_id})
        return {'policy_version':'forward-evaluation-v1.0.0','pending_outcomes':pending,'ancillary_1d':ancillary,'review_gate':review_gate(runs),
            'system':{h:metrics(v) for h,v in rows.items()},'human':{h:metrics(v) for h,v in human.items()},
            'shadow_comparison':{h:shadow_comparison(v) for h,v in rows.items()},'human_records':self.records('human'),
            'limitations':['Overlapping horizons are not independent trials.','Exact due timestamps can defer measurement to a later market close.',
                'Human records are unblinded; late entries excluded; first prospective record per person/run/horizon is primary.']}
