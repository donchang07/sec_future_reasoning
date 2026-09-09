"""Versioned real-world contracts; legacy schemas and model coefficients stay frozen."""
from enum import Enum
from typing import Literal
from pydantic import AwareDatetime, model_validator
from ..schemas.contracts import Contract, Number, Probability, ProbabilityVector, DataMode, Text

CONTRACT_VERSION = 'real-world-contract-v2.0.0'
MAPPING_VERSION = 'semantic-mapping-v1.0.0'
Horizon = Literal['1w','1m','1y']


class Requirement(str, Enum):
    HARD = 'Hard Required'
    STRONG = 'Strong Evidence'
    SUPPORTING = 'Supporting Evidence'
    OPTIONAL = 'Optional'
    UNAVAILABLE_ALLOWED = 'Unavailable Allowed'


class SourceObservation(Contract):
    source_id: Text
    source_field: Text
    source_unit: Text
    value: Number
    economic_scope: Text
    series_id: Text
    observed_at: AwareDatetime
    effective_at: AwareDatetime
    released_at: AwareDatetime | None
    collected_at: AwareDatetime
    data_mode: DataMode
    raw_ref: Text
    reporting_period: str | None = None
    prior_value: Number | None = None
    reported_yoy: Number | None = None
    current_workdays: Number | None = None
    prior_workdays: Number | None = None
    month: str | None = None
    coverage_days: int | None = None
    vintage_stage: Literal['nowcast_v1','nowcast_v2','nowcast_v3','final'] | None = None

    @model_validator(mode='after')
    def chronology(self):
        if not self.observed_at <= self.effective_at <= self.collected_at:
            raise ValueError('observation chronology')
        if self.released_at is not None and not self.effective_at <= self.released_at <= self.collected_at:
            raise ValueError('release chronology')
        if any(x is not None and x <= 0 for x in (self.current_workdays,self.prior_workdays)):
            raise ValueError('working days must be positive')
        if self.source_field == 'semiconductor_export_demand':
            import calendar
            if self.value<0 or (self.reported_yoy is not None and self.reported_yoy < -100):
                raise ValueError('invalid export amount/growth')
            if not self.month or not self.vintage_stage:
                raise ValueError('export month/stage required')
            try:
                y,m=map(int,self.month.split('-'));last=calendar.monthrange(y,m)[1]
            except (ValueError,TypeError):
                raise ValueError('invalid export month')
            days={'nowcast_v1':10,'nowcast_v2':20}.get(self.vintage_stage,last)
            if self.coverage_days != days or self.effective_at.strftime('%Y-%m') != self.month or self.effective_at.day != days:
                raise ValueError('export stage/period mismatch')
        return self

    def eligible(self, cutoff):
        return self.collected_at <= cutoff and self.effective_at <= cutoff and (self.released_at is None or self.released_at <= cutoff)


class FactorRequirement(Contract):
    factor_id: str
    module: str
    bucket: str | None
    levels: dict[Horizon, Requirement]
    rationale: str
    max_age_days: float


class MappingRule(Contract):
    source_field: str
    source_unit: str
    factor_id: str
    economic_meaning: str
    transform: Literal['identity','cash_outflow_magnitude','reported_yoy','ratio_margin','full_cash_capex','free_cash_flow','cash_debt_ratio']
    mapping_confidence: Probability
    valid_horizon: tuple[Horizon,...]
    valid_regime: tuple[str,...]
    mapping_version: str
    economic_scope: str


class MappingPolicy(Contract):
    version: str = MAPPING_VERSION


class FactorEvidence(Contract):
    evidence_id: str
    factor_id: str
    value: Number
    unit: str
    signal: Number | None
    root_id: str
    series_id: str
    source_refs: tuple[str,...]
    effective_at: AwareDatetime
    collected_at: AwareDatetime
    data_mode: DataMode
    horizon: Horizon
    economic_scope: str
    reporting_period: str | None = None
    mapping: MappingRule
    derived_signals: dict[str, Number | None] = {}

    @model_validator(mode='after')
    def mapping_binding(self):
        if self.factor_id!=self.mapping.factor_id or self.horizon not in self.mapping.valid_horizon:
            raise ValueError('evidence/mapping identity mismatch')
        if self.effective_at>self.collected_at or not self.source_refs:
            raise ValueError('evidence chronology/provenance')
        if self.signal is not None and not -1<=self.signal<=1:
            raise ValueError('normalized evidence signal out of range')
        return self


class Unmapped(Contract):
    source_ref: str
    source_field: str
    reason: str


class MappingBatch(Contract):
    contract_version: str = CONTRACT_VERSION
    mapping_version: str
    horizon: Horizon
    regime: str
    data_cutoff: AwareDatetime
    data_mode: DataMode | None
    evidence: tuple[FactorEvidence,...]
    unmapped: tuple[Unmapped,...]
    superseded_refs: tuple[str,...]


class MemoryState(Contract):
    score: Number | None
    family_scores: dict[str, Number | None]
    positive_families: tuple[str,...]
    negative_families: tuple[str,...]
    unknown_families: tuple[str,...]
    conflict: Probability
    root_contributions: dict[str, Number]


class Candidate(Contract):
    probabilities: ProbabilityVector
    confidence: Probability
    horizon: Horizon
    data_cutoff: AwareDatetime
    data_mode: DataMode
    contract_version: Literal['real-world-contract-v2.0.0'] = CONTRACT_VERSION
    origin: Literal['future_reasoning'] = 'future_reasoning'


class Publication(Contract):
    status: Literal['eligible','withheld']
    probabilities: ProbabilityVector | None
    confidence: Probability | None
    reasons: tuple[str,...]
    contract_version: str = CONTRACT_VERSION
    assessment_hash: str
