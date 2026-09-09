"""Allowlisted source semantics. No observation can bypass this boundary."""
import hashlib
import json
from .types import MappingPolicy, MappingRule, MappingBatch, FactorEvidence, Unmapped, SourceObservation, MAPPING_VERSION
from .registry import MATRIX, rule_for, UNITS
from .exports import select_vintages, export_signals


def clip(v):return max(-1.,min(1.,v))


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def evidence(o,rule,value,signal,root,horizon,derived=None,extra_refs=()):
    key={'source':o.model_dump(mode='json'),'mapping':rule.model_dump(mode='json'),'value':value,'signal':signal,
        'derived_signals':derived or {},'extra_refs':extra_refs,'horizon':horizon}
    return FactorEvidence(evidence_id=digest(key),factor_id=rule.factor_id,value=value,
        unit=UNITS[rule.factor_id],signal=signal,root_id=root,series_id=o.series_id,source_refs=tuple(sorted(set((o.raw_ref,)+extra_refs))),
        effective_at=o.effective_at,collected_at=o.collected_at,data_mode=o.data_mode,horizon=horizon,
        economic_scope=o.economic_scope,mapping=rule,derived_signals=derived or {})


def derive_company(items,version,horizon):
    groups={}
    for e in items:
        if e.economic_scope=='company_consolidated':groups.setdefault(e.effective_at,{}).setdefault(e.factor_id,[]).append(e)
    derived=[]
    for period,group in sorted(groups.items()):
        # Ambiguous multiple source values may never choose the convenient operand.
        values={k:v[0] for k,v in group.items() if len({e.value for e in v})==1}
        def create(name,keys,calc,transform):
            if not all(k in values for k in keys):return
            inputs=[values[k] for k in keys];value=calc(*(e.value for e in inputs))
            if value is None:return
            rule=MappingRule(source_field='+'.join(keys),source_unit='krw_million',factor_id=name,
                economic_meaning=MATRIX[name].rationale,transform=transform,mapping_confidence=min(e.mapping.mapping_confidence for e in inputs),
                valid_horizon=('1w','1m','1y'),valid_regime=('*',),mapping_version=version,economic_scope='company_consolidated')
            refs=tuple(sorted({r for e in inputs for r in e.source_refs}))
            item=FactorEvidence(evidence_id=digest({'inputs':[e.evidence_id for e in inputs],'rule':rule.model_dump(mode='json'),'value':value}),
                factor_id=name,value=value,unit=UNITS[name],signal=None,root_id='company:'+period.isoformat(),series_id=name,
                source_refs=refs,effective_at=period,collected_at=max(e.collected_at for e in inputs),
                data_mode=inputs[0].data_mode,horizon=horizon,economic_scope='company_consolidated',mapping=rule)
            derived.append(item);values[name]=item
        create('samsung_operating_margin',('samsung_operating_profit','samsung_revenue'),lambda p,r:100*p/r if r>0 else None,'ratio_margin')
        create('samsung_capex',('samsung_capex_ppe_cash','samsung_capex_intangibles'),lambda a,b:a+b,'full_cash_capex')
        create('samsung_free_cash_flow',('samsung_operating_cash','samsung_capex'),lambda a,b:a-b,'free_cash_flow')
        create('samsung_cash_debt_ratio',('samsung_cash_end','samsung_debt'),lambda a,b:a/b if b>0 else None,'cash_debt_ratio')
    return derived


def map_observations(observations,cutoff,horizon,regime,policy=None):
    policy=policy or MappingPolicy()
    if horizon not in ('1w','1m','1y'):raise ValueError('unsupported horizon')
    # Revalidate even caller-created/copy-updated models.
    observations=tuple(SourceObservation.model_validate(o) for o in observations)
    modes={o.data_mode for o in observations}
    if len(modes)>1:raise ValueError('mixed data mode')
    if policy.version!=MAPPING_VERSION and (modes!={'synthetic_fixture'} or not policy.version.startswith('semantic-mapping-test-')):
        raise ValueError('unsupported mapping version; publish an explicit registry release')
    unmapped=[];eligible=[];superseded=[];rules={};historical_exports=[]
    def reject(o,reason):unmapped.append(Unmapped(source_ref=o.raw_ref,source_field=o.source_field,reason=reason))
    for o in observations:
        rule=rule_for(o.source_field,policy.version)
        if rule is None:reject(o,'no_mapping_rule');continue
        if o.source_unit!=rule.source_unit:reject(o,'unit_mismatch');continue
        if o.economic_scope!=rule.economic_scope:reject(o,'scope_mismatch');continue
        if horizon not in rule.valid_horizon:reject(o,'horizon_excluded');continue
        if '*' not in rule.valid_regime and regime not in rule.valid_regime:reject(o,'regime_excluded');continue
        if not o.eligible(cutoff):reject(o,'after_cutoff');continue
        if o.source_field=='semiconductor_export_demand':historical_exports.append(o)
        basis=(o.released_at or o.collected_at) if rule.factor_id=='semiconductor_export_momentum' else o.effective_at
        if (cutoff-basis).total_seconds()>MATRIX[rule.factor_id].max_age_days*86400:reject(o,'stale');continue
        if rule.factor_id in ('samsung_preferred_price','samsung_common_price','dram_spot_price','dram_contract_asp','hbm_price') and o.value<=0:
            reject(o,'nonpositive_price');continue
        if rule.transform=='cash_outflow_magnitude' and o.value>0:reject(o,'cash_outflow_sign');continue
        eligible.append(o);rules[(o.source_field,o.raw_ref)]=rule
    exports=[o for o in eligible if o.source_field=='semiconductor_export_demand']
    historical_groups={};comparators=[]
    for o in historical_exports:historical_groups.setdefault((o.series_id,o.month),[]).append(o)
    for group in historical_groups.values():
        try:comparators.extend(select_vintages(group,cutoff))
        except ValueError:continue  # Conflicting historical vintage cannot supply a comparison.
    selected_exports=[]
    groups={}
    for o in exports:groups.setdefault((o.series_id,o.month),[]).append(o)
    for group in groups.values():
        try:selected_exports.extend(select_vintages(group,cutoff))
        except ValueError:
            for o in group:reject(o,'conflicting_export_vintage')
    for o in exports:
        if o not in selected_exports:superseded.append(o.raw_ref)
    # Keep only latest eligible same-series snapshot; equal-time disagreement is conflict.
    nonexports={}
    for o in eligible:
        if o.source_field!='semiconductor_export_demand':
            nonexports.setdefault((o.source_field,o.series_id,o.economic_scope),[]).append(o)
    selected=[]
    for group in nonexports.values():
        latest=max((o.effective_at,o.released_at or o.collected_at,o.collected_at) for o in group)
        same=[o for o in group if (o.effective_at,o.released_at or o.collected_at,o.collected_at)==latest]
        if len({(o.value,o.prior_value) for o in same})>1:
            for o in group:reject(o,'conflicting_source_value')
            continue
        chosen=sorted(same,key=lambda o:o.raw_ref)[0];selected.append(chosen)
        superseded.extend(o.raw_ref for o in group if o!=chosen)
    items=[]
    for o in selected+selected_exports:
        rule=rules[(o.source_field,o.raw_ref)];value=o.value;signal=None;derived={};extra_refs=()
        root=rule.factor_id+':'+o.effective_at.isoformat()
        if rule.transform=='cash_outflow_magnitude':value=-value
        elif rule.transform=='reported_yoy':
            previous=[p for p in comparators if p.series_id==o.series_id and p.month<o.month]
            comparator=max(previous,key=lambda p:p.month) if previous else None
            derived=export_signals(o,comparator)
            if derived['acceleration_pp'] is not None:extra_refs=(comparator.raw_ref,)
            if derived['yoy'] is None:reject(o,'missing_comparable_yoy');continue
            value=derived['yoy'];signal=clip(value/100);root='kcs_exports:'+o.month
        elif o.prior_value is not None and o.prior_value>0:
            signal=clip(o.value/o.prior_value-1)
            if rule.factor_id=='memory_inventory':signal=-signal
        if rule.factor_id=='dram_spot_price':root='dram_spot_family:'+o.effective_at.date().isoformat()
        item=evidence(o,rule,value,signal,root,horizon,derived,extra_refs)
        items.append(item)
    items.extend(derive_company(items,policy.version,horizon))
    return MappingBatch(mapping_version=policy.version,horizon=horizon,regime=regime,data_cutoff=cutoff,
        data_mode=next(iter(modes)) if modes else None,evidence=tuple(sorted(items,key=lambda e:(e.factor_id,e.series_id,e.evidence_id))),
        unmapped=tuple(sorted(unmapped,key=lambda u:(u.source_field,u.source_ref,u.reason))),superseded_refs=tuple(sorted(set(superseded))))
