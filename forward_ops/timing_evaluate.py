"""Bug-fix data preparation only; invokes the original v2 reasoning functions."""
try:
    from .admission import project_bundle
    from .source_timing import treasury_rows,assess_yahoo,previous_us_close,TIMING,POLICY
except ImportError:
    from admission import project_bundle
    from source_timing import treasury_rows,assess_yahoo,previous_us_close,TIMING,POLICY


def project(bundle,session):
    # Preserve the old projector for Korean data and old replay. US data receives
    # explicit availability below, never the old 23:59:59-as-close convention.
    admitted,audit=project_bundle(bundle,session)
    cap=previous_us_close(bundle.market.data_cutoff);timing=[];raws=[]
    originals={r.source.source_id:r for r in bundle.market.sources}
    for raw in admitted.market.sources:
        sid=raw.source.source_id
        if sid not in ('treasury_10y','dxy','usdkrw'):raws.append(raw);continue
        original=originals[sid]
        state=treasury_rows(original,bundle.market.data_cutoff,cap)[1] if sid=='treasury_10y' else assess_yahoo(original,bundle.market.data_cutoff,cap)
        state={**state,'model_influence':sid=='treasury_10y' and state['status']=='available',
            'model_route':'existing_factor_us_10y_yield' if sid=='treasury_10y' else None}
        timing.append(state)
        # Original parser sees no US row. The verified Treasury rows are supplied
        # as typed observations by prepare below, with unmodified original values.
        raws.append(type(raw).model_validate({**original.model_dump(),'status':'unavailable',
            'error':state['reason'] or 'handled_by_source_timing_v1.0.1'}))
    market=type(admitted.market).model_validate({**admitted.market.model_dump(),'sources':tuple(raws)})
    admitted=type(admitted).model_validate({**admitted.model_dump(),'market':market})
    from reasoning.live_v2 import digest
    audit.update(policy_version=POLICY,timing_version=TIMING,timing_sources=timing,admitted_bundle_hash=digest(admitted.model_dump(mode='json')))
    for row in audit['sources']:
        if row['source_id'] in ('treasury_10y','dxy','usdkrw'):
            actual=next(x for x in timing if x['source_id']==row['source_id'])
            row.update(status=actual['status'],reason=actual['reason'],admitted_sha256=originals[row['source_id']].sha256,
                timestamp_policy=TIMING,latest_admitted_effective_at=actual.get('effective_at'),excluded_by_market_cutoff=None)
    return admitted,audit


def prepare(admitted,original):
    from reasoning.live import prepare as frozen_prepare,SourceStatus
    from reasoning.market_data import make_observation
    fixture,statuses,_=frozen_prepare(admitted.market);observations=list(fixture.observations);updated=list(statuses)
    raw=next((r for r in original.market.sources if r.source.source_id=='treasury_10y'),None)
    if raw:
        rows,state=treasury_rows(raw,original.market.data_cutoff,previous_us_close(original.market.data_cutoff))
        observations.extend(make_observation(raw,'us_10y_yield','percent',value,effective,'date') for effective,value in rows)
        latest=rows[-1][0] if rows else None
        status=SourceStatus(source_id=raw.source.source_id,instrument=raw.source.instrument,provider=raw.source.provider,
            authority=raw.source.authority,raw_sha256=raw.sha256,status='fresh' if rows else 'unavailable',
            latest_effective_at=latest,collected_at=raw.collected_at,age_hours=(original.market.data_cutoff-latest).total_seconds()/3600 if latest else None,
            rows=len(rows),excluded={},used_by_model=bool(rows),reason=state['reason'])
        updated=[status if s.source_id=='treasury_10y' else s for s in updated]
    fixture=type(fixture).model_validate({**fixture.model_dump(),'observations':tuple(observations)})
    return fixture,tuple(updated)


def evaluate(admitted,original):
    # Same source→semantic→run_mapped assembly as frozen live_v2.evaluate. Only
    # prepare differs; no new diagnostic symbol enters sources or the graph.
    from reasoning import live_v2 as model
    fixture,statuses=prepare(admitted,original)
    sources,priors=model.market_semantics(fixture)
    evidence=model.assess(original.documents,original.market.data_cutoff)
    sources=list(sources)+[model.source_from_fact(f) for f in evidence.facts]
    for raw in admitted.market.sources:
        if raw.source.source_id!='kospi' or raw.status!='available':continue
        bars,_=model.parse_yahoo(raw,admitted.market.data_cutoff)
        if bars:
            b=bars[-1]
            sources.append(model.SourceObservation(source_id=raw.source.source_id,source_field=raw.source.source_id,source_unit=raw.source.unit,
                value=b.close,economic_scope='market',series_id=raw.source.source_id,observed_at=b.closed_at,effective_at=b.closed_at,
                released_at=None,collected_at=raw.collected_at,data_mode=raw.data_mode,raw_ref='raw:'+raw.sha256))
    output=model.run_mapped(fixture,tuple(sources),original.lock)
    if output['p0']:
        sid='preferred_30m' if output['p0']['timeframe']=='30m' else 'preferred_daily'
        output['p0']['source_refs']=['raw:'+r.sha256 for r in admitted.market.sources if r.source.source_id==sid]
    output.update(raw_bundle_hash=model.digest(original.model_dump(mode='json')),lock=original.lock,
        sources=[s.model_dump(mode='json') for s in statuses],document_status=evidence.source_status,
        raw_observations=[s.model_dump(mode='json') for s in sources],prior_provenance=priors,
        bar_boundaries={k:{'count':len(v),'last':v[-1].closed_at.isoformat() if v else None} for k,v in fixture.bars.items()},
        data_timing_version=TIMING,findings=['Data timing bug fix; model/graph/weights/thresholds unchanged.',
            'Treasury effective time is approximate 15:30 ET with date precision; release time unknown.',
            'Unverified FX/DXY daily close unavailable; new US equity and oil diagnostics do not enter reasoning.',
            'Calibration remains unvalidated; reversal scores are not calibrated probabilities.'])
    return output
