"""Offline classification only. No collection, candidate prediction or journal write."""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from .types import CONTRACT_VERSION, MAPPING_VERSION, SourceObservation, Requirement
from .registry import MATRIX, rule_for, MINIMUMS, MEMORY_FAMILIES
from .mapping import map_observations
from .constraints import evaluate_e11, company_from_evidence
from ..schemas.contracts import canonical_hash

ROOT=Path(__file__).resolve().parents[2]


def source_from_fact(f):
    """Explicit migration into a new audit object; original Fact is never edited."""
    if f.factor_id.startswith('dram_spot_'):scope='memory_spot'
    elif f.factor_id=='semiconductor_export_demand':scope='semiconductor_exports'
    else:scope='company_consolidated'
    stage=None
    if f.month:
        stage={10:'nowcast_v1',20:'nowcast_v2'}.get(f.coverage_days,'final')
    period=re.search(r'\b(H[12]|Q[1-4]|FY)\b',f.scope) if scope=='company_consolidated' else None
    return SourceObservation(source_id=f.source_id,source_field=f.factor_id,source_unit=f.unit,value=f.value,
        economic_scope=scope,series_id='kcs_semiconductor_exports' if f.month else f.factor_id,
        observed_at=f.observed_at,effective_at=f.effective_at,released_at=f.released_at,collected_at=f.collected_at,
        data_mode=f.data_mode,raw_ref=f.source_ref,reported_yoy=f.yoy_percent,month=f.month,
        coverage_days=f.coverage_days,vintage_stage=stage,
        reporting_period=f'{f.effective_at.year}-{period[1]}' if period else None)


def classify_facts(facts,cutoff):
    sources=[source_from_fact(f) for f in facts]
    batch=map_observations(sources,cutoff,'1w','unknown')
    rows=[]
    for source,original in zip(sources,facts):
        single=map_observations([source],cutoff,'1w','unknown')
        rule=rule_for(source.source_field)
        row={'source_id':source.source_id,'source_field':source.source_field,'source_unit':source.source_unit,
            'original_mapping':original.mapping,'source_ref':source.raw_ref,'value':source.value,
            'old_journal_untouched':True}
        if not single.evidence:
            row.update(disposition='still unmapped',reason='; '.join(u.reason for u in single.unmapped),mapping=None)
        else:
            e=single.evidence[0]
            row.update(disposition='directly mappable' if rule.transform=='identity' else 'derived evidence mappable',
                reason=rule.economic_meaning+'; '+('value only, no directional comparator' if e.signal is None else 'explicit comparable-period signal'),
                mapping=rule.model_dump(mode='json'),factor_value=e.value,signal=e.signal,
                selected_for_state=any(x.evidence_id==e.evidence_id for x in batch.evidence))
        rows.append(row)
    constraints=evaluate_e11(company_from_evidence(batch.evidence),None,None)
    return {'artifact_type':'contract_classification_audit','contract_version':CONTRACT_VERSION,'mapping_version':MAPPING_VERSION,
        'new_prediction_created':False,'cutoff_used_only_for_semantic_audit':cutoff.isoformat(),
        'counts':dict(Counter(r['disposition'] for r in rows)),'rows':rows,
        'mapped_evidence': [e.model_dump(mode='json') for e in batch.evidence],
        'batch_hash':canonical_hash(batch),'constraints':constraints.model_dump(mode='json'),
        'still_unavailable':['full_cash_capex','full_free_cash_flow','debt_ratio','memory_segment_identity','industry_supply_identity'],
        'note':'No historical forecast recalculated. Old unmapped fields remain unchanged; this is a new versioned audit.'}


def build_manifest():
    files=sorted((ROOT/'reasoning/refinement').glob('*.py'))
    frozen=['reasoning/engines.py','reasoning/technical.py','reasoning/decision.py','config/live-model-profile.json']
    sha=lambda p:hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest()
    return {'contract_version':CONTRACT_VERSION,'mapping_version':MAPPING_VERSION,'artifact_type':'contract_release',
        'live_prediction_enabled':False,'e11_version':'e11-real-world-v2.0.0','coverage_policy_version':'economic-bucket-quorum-v1',
        'calibration':'unchanged temperature 1.15; unvalidated','prior':[.4,.35,.25],
        'entry_threshold':.8,'sell_threshold':.7,
        'module_weight_policy':'unchanged reasoning.engines.WEIGHTS; requirement levels are not weights',
        'module_minimums':MINIMUMS,'memory_taxonomy':list(MEMORY_FAMILIES),
        'requirement_matrix':{k:v.model_dump(mode='json') for k,v in MATRIX.items()},
        'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},
        'frozen_sha256':{p:sha(ROOT/p) for p in frozen}}


def verify_manifest(path):
    saved=json.loads(Path(path).read_text(encoding='utf-8'))
    if saved!=build_manifest():raise ValueError('contract release manifest drift')
    return saved


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--journal',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--verify-manifest',type=Path)
    args=p.parse_args()
    if args.verify_manifest:
        verify_manifest(args.verify_manifest);print('contract manifest valid');return
    if not args.journal or not args.output:p.error('--journal and --output required')
    from ..act_live import SealedAct
    original=args.journal.read_bytes();sealed=SealedAct.model_validate_json(original)
    result=classify_facts(sealed.snapshot.evidence.facts,sealed.snapshot.live.data_cutoff)
    result['source_journal_sha256']=sealed.sha256
    result['source_journal_file_sha256']=hashlib.sha256(original).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    # Exclusive create: a classification audit may never replace a prior artifact.
    with args.output.open('x',encoding='utf-8',newline='\n') as out:json.dump(result,out,ensure_ascii=False,indent=2)
    if args.journal.read_bytes()!=original:raise ValueError('source journal changed during audit')
    print(json.dumps({'counts':result['counts'],'output':str(args.output),'new_prediction_created':False}))


if __name__=='__main__':main()
