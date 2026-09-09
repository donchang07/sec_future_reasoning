"""Ex-ante scoring. No fitting, no engine imports and no tuning output."""
from datetime import datetime
from math import sqrt
from zoneinfo import ZoneInfo

CLASSES=('up','down','flat')
DAYS={'1w':7,'1m':30,'1y':365}


def label(ret,horizon):
    band=.01*sqrt(DAYS[horizon]/7)
    return 'up' if ret>band else 'down' if ret < -band else 'flat'


def score(horizon,ret,held=False):
    f=horizon['final']
    if f is None:return None
    p=f['probabilities'];actual=label(ret,horizon['horizon'])
    winners=[k for k in CLASSES if p[k]==max(p.values())]
    correct=(winners[0]==actual) if len(winners)==1 else None
    action=horizon['decision']['action']
    return {'horizon':horizon['horizon'],'return':ret,'actual':actual,'probabilities':p,'confidence':f['confidence'],
        'correct':correct,'tie':len(winners)>1,'brier':sum((p[k]-(k==actual))**2 for k in CLASSES),'action':action,'held':held,
        'false_entry':action=='ENTRY' and actual!='up','missed_entry':not held and action=='WAIT' and actual=='up',
        'false_sell':action=='SELL' and actual!='down','missed_sell':held and action=='HOLD' and actual=='down'}


def bins(rows,value,target):
    result=[]
    for i in range(10):
        subset=[r for r in rows if min(9,int(value(r)*10))==i and target(r) is not None]
        result.append({'low':i/10,'high':(i+1)/10,'n':len(subset),
            'mean_prediction':sum(value(r) for r in subset)/len(subset) if subset else None,
            'observed_frequency':sum(target(r) for r in subset)/len(subset) if subset else None})
    return result


def metrics(rows):
    rows=[r for r in rows if r is not None];unique=[r for r in rows if r['correct'] is not None]
    reliability={k:bins(rows,lambda r:r['probabilities'][k],lambda r:r['actual']==k) for k in CLASSES}
    confidence=bins(rows,lambda r:r['confidence'],lambda r:r['correct'])
    ece={k:sum(b['n']*abs(b['mean_prediction']-b['observed_frequency']) for b in v if b['n'])/len(rows) if rows else None for k,v in reliability.items()}
    return {'n':len(rows),'unique_argmax_n':len(unique),'ties':len(rows)-len(unique),
        'directional_accuracy':sum(r['correct'] for r in unique)/len(unique) if unique else None,
        'brier':sum(r['brier'] for r in rows)/len(rows) if rows else None,'brier_range':[0,2],
        'reliability':reliability,'class_ece':ece,'confidence_bins':confidence,
        'actions':{k:sum(r[k] for r in rows) for k in ('false_entry','missed_entry','false_sell','missed_sell')},
        'denominators':{'entries':sum(r['action']=='ENTRY' for r in rows),'sells':sum(r['action']=='SELL' for r in rows),
            'unheld_up_opportunities':sum(not r['held'] and r['actual']=='up' for r in rows),
            'held_down_opportunities':sum(r['held'] and r['actual']=='down' for r in rows)},
        'limitation':'Directional opportunity diagnostics, not executable P&L or a calibrated trading strategy.'}


def select_close(bars,due,cutoff):
    eligible=[b for b in bars if due<=datetime.fromisoformat(b['closed_at'])<=cutoff]
    return min(eligible,key=lambda b:datetime.fromisoformat(b['closed_at'])) if eligible else None


def review_gate(records):
    def key(r):
        if 'review_key' in r:return r['review_key']
        if r.get('kind')=='imported' and 'system' in r:
            return 'session:'+datetime.fromisoformat(r['system']['data_cutoff']).astimezone(ZoneInfo('Asia/Seoul')).date().isoformat()
        return r['case_key']
    count=len({key(r) for r in records if r['eligible_case']})
    return {'distinct_cases':count,'minimum':20,'review_minimum_met':count>=20,'automatic_tuning_allowed':False,
        'shadow_model_influence':False,'note':'Even after 20 cases, a separate contract PDCA is required.'}


def shadow_comparison(rows):
    groups={}
    for row in rows:
        sh=row.get('shadow',{});features=set()
        for p in sh.get('positioning',{}).get('rows',[]):
            if p.get('freshness')=='stale':continue
            sign='positive' if p['value']>0 else 'negative' if p['value']<0 else 'zero'
            features.add((p['venue'],p['instrument'],p['investor'],p['measure'],sign))
        ev=sh.get('event')
        if ev:
            s=ev['surprise'];features.add(('event',ev['event']['event_type'],'surprise','standard_deviations','unknown' if s is None else 'positive' if s>0 else 'negative' if s<0 else 'zero'))
        if not features:features.add(('missing_shadow','unknown','unknown','unknown','unknown'))
        for feature in features:groups.setdefault(feature,[]).append(row)
    result=[]
    for feature,group in sorted(groups.items()):
        result.append({'feature':list(feature),'n':len(group),'baseline_errors':sum(r['correct'] is False for r in group),
            'baseline_correct':sum(r['correct'] is True for r in group),'mean_return':sum(r['return'] for r in group)/len(group),
            'baseline_brier':sum(r['brier'] for r in group)/len(group)})
    return {'groups':result,'causal_claim':False,'model_influence':False,'limitation':'Retrospective descriptive association; overlapping groups, no feature selection or correction fitted.'}
