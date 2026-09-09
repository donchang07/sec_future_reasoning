"""Month-level Customs nowcast vintages and comparable-period derived signals."""
STAGES={'nowcast_v1':1,'nowcast_v2':2,'nowcast_v3':3,'final':4}


def select_vintages(observations,cutoff):
    groups={}
    for o in observations:
        if not o.eligible(cutoff):continue
        groups.setdefault((o.series_id,o.month),[]).append(o)
    selected=[]
    for key,items in sorted(groups.items()):
        stage=max(STAGES[o.vintage_stage] for o in items)
        items=[o for o in items if STAGES[o.vintage_stage]==stage]
        release=max(o.released_at or o.collected_at for o in items)
        items=[o for o in items if (o.released_at or o.collected_at)==release]
        collected=max(o.collected_at for o in items)
        latest=[o for o in items if o.collected_at==collected]
        if len({(o.value,o.reported_yoy,o.prior_value,o.current_workdays,o.prior_workdays) for o in latest})>1:
            raise ValueError('conflicting export vintage: '+str(key))
        selected.append(sorted(latest,key=lambda o:o.raw_ref)[0])
    return tuple(selected)


def export_signals(current,previous=None):
    yoy=current.reported_yoy
    if yoy is None and current.prior_value is not None and current.prior_value>0:
        yoy=(current.value/current.prior_value-1)*100
    adjusted=None
    if yoy is not None and current.current_workdays is not None and current.prior_workdays is not None:
        adjusted=((1+yoy/100)*current.prior_workdays/current.current_workdays-1)*100
    acceleration=None
    if previous is not None and yoy is not None:
        y,m=map(int,current.month.split('-'));py,pm=map(int,previous.month.split('-'))
        full=lambda o:o.vintage_stage in ('nowcast_v3','final')
        comparable=(full(current) and full(previous)) or (not full(current) and not full(previous) and current.coverage_days==previous.coverage_days)
        prior_yoy=export_signals(previous)['yoy']
        if y*12+m-py*12-pm==1 and comparable and current.series_id==previous.series_id and prior_yoy is not None:
            acceleration=yoy-prior_yoy
    return {'yoy':yoy,'workday_adjusted_yoy':adjusted,'acceleration_pp':acceleration}
