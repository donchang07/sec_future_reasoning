"""Economic coverage and confidence policy; no new prior or probability weights."""
from statistics import mean
from ..schemas.contracts import Contract, Probability, AwareDatetime, DataMode, canonical_hash
from .types import Horizon, Requirement as R, MemoryState, Unmapped, Publication, CONTRACT_VERSION, MappingBatch, Candidate
from .registry import MATRIX, BUCKETS, MINIMUMS, MEMORY_FAMILIES, UNITS
from .constraints import LayeredConstraints, evaluate_e11, company_from_evidence


class Assessment(Contract):
    contract_version: str=CONTRACT_VERSION
    mapping_version: str
    horizon: Horizon
    data_cutoff: AwareDatetime
    data_mode: DataMode
    eligible: bool
    coverage: dict[str,Probability]
    hard_missing: tuple[str,...]
    strong_missing: tuple[str,...]
    penalized_modules: tuple[str,...]
    confidence_multiplier: Probability
    reasons: tuple[str,...]
    unmapped: tuple[Unmapped,...]
    memory: MemoryState
    constraints: LayeredConstraints
    evidence_ids: tuple[str,...]


def infer_memory(evidence):
    roots={};known=set()
    for e in evidence:
        if e.factor_id not in MEMORY_FAMILIES:continue
        known.add(e.factor_id)
        if e.signal is not None:
            roots.setdefault((e.factor_id,e.root_id),{})[e.evidence_id]=(e.signal,e.mapping.mapping_confidence)
    # Same economic root gets one aggregate vote; adding another SKU cannot create another family.
    root_scores={key:sum(v*q for v,q in rows.values())/sum(q for _,q in rows.values())
        for key,rows in roots.items() if sum(q for _,q in rows.values())>0}
    scores={f:mean(v for (family,root),v in root_scores.items() if family==f)
        if any(family==f for family,root in root_scores) else None for f in MEMORY_FAMILIES}
    positive=tuple(f for f,v in scores.items() if v is not None and v>0)
    negative=tuple(f for f,v in scores.items() if v is not None and v<0)
    directional=[v for v in scores.values() if v is not None]
    pos=sum(v for v in directional if v>0);neg=-sum(v for v in directional if v<0)
    return MemoryState(score=mean(directional) if directional else None,family_scores=scores,positive_families=positive,
        negative_families=negative,unknown_families=tuple(f for f,v in scores.items() if v is None),
        conflict=min(pos,neg)/(pos+neg) if pos+neg else 0.,root_contributions={f+'|'+r:v for (f,r),v in root_scores.items()})


def assess_contract(batch,cutoff,horizon,data_mode,*,memory_business=None,industry_supply=None):
    batch=MappingBatch.model_validate(batch)
    if batch.data_cutoff!=cutoff or batch.horizon!=horizon or batch.contract_version!=CONTRACT_VERSION:
        raise ValueError('mapping/assessment identity mismatch')
    if batch.data_mode is not None and batch.data_mode!=data_mode:raise ValueError('mixed assessment mode')
    for e in batch.evidence:
        if e.factor_id not in MATRIX or e.unit!=UNITS[e.factor_id] or e.economic_scope!=e.mapping.economic_scope:
            raise ValueError('semantic evidence mismatch')
        if e.horizon!=horizon or e.collected_at>cutoff or e.data_mode!=data_mode or e.mapping.mapping_version!=batch.mapping_version:
            raise ValueError('evidence identity mismatch')
    present={e.factor_id for e in batch.evidence if e.mapping.mapping_confidence>0}
    hard=tuple(sorted(k for k,s in MATRIX.items() if s.levels[horizon]==R.HARD and k not in present))
    strong=tuple(sorted(k for k,s in MATRIX.items() if s.levels[horizon]==R.STRONG and k not in present))
    penalized=tuple(sorted({MATRIX[k].module for k in strong}))
    credits={(m,b):0. for m,buckets in BUCKETS.items() for b in buckets}
    for e in batch.evidence:
        spec=MATRIX[e.factor_id]
        if spec.bucket is not None and spec.levels[horizon] in (R.HARD,R.STRONG,R.SUPPORTING):
            key=spec.module,spec.bucket;credits[key]=max(credits[key],e.mapping.mapping_confidence)
    coverage={m:mean(credits[(m,b)] for b in buckets) for m,buckets in BUCKETS.items()}
    constraints=evaluate_e11(company_from_evidence(batch.evidence),memory_business,industry_supply)
    reasons=['hard_missing:'+k for k in hard]
    reasons.extend('coverage:'+m for m,v in MINIMUMS[horizon].items() if coverage[m]+1e-12<v)
    if horizon=='1y' and len(present.intersection(MEMORY_FAMILIES))<2:reasons.append('memory_family_quorum')
    if constraints.fatal:reasons.append('E11_constraint_failure')
    multiplier=min(coverage[m] for m in MINIMUMS[horizon])*(.9**len(penalized))
    return Assessment(mapping_version=batch.mapping_version,horizon=horizon,data_cutoff=cutoff,data_mode=data_mode,
        eligible=not reasons,coverage=coverage,hard_missing=hard,strong_missing=strong,penalized_modules=penalized,
        confidence_multiplier=multiplier,reasons=tuple(reasons),unmapped=batch.unmapped,memory=infer_memory(batch.evidence),
        constraints=constraints,evidence_ids=tuple(e.evidence_id for e in batch.evidence))


def publish_candidate(candidate,assessment):
    candidate=Candidate.model_validate(candidate);assessment=Assessment.model_validate(assessment)
    if (candidate.horizon,candidate.data_cutoff,candidate.data_mode,candidate.contract_version)!=(assessment.horizon,assessment.data_cutoff,assessment.data_mode,assessment.contract_version):
        raise ValueError('candidate/assessment identity mismatch')
    return Publication(status='eligible' if assessment.eligible else 'withheld',
        probabilities=candidate.probabilities if assessment.eligible else None,
        confidence=candidate.confidence*assessment.confidence_multiplier if assessment.eligible else None,
        reasons=assessment.reasons,assessment_hash=canonical_hash(assessment))
