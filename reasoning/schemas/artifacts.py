"""Discriminated typed artifacts for the nineteen engine boundaries."""
from __future__ import annotations

from typing import Annotated, Literal, Union
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from .contracts import (
    Contract, Count, EngineId, Falsifier, Forecast, JournalSnapshot, ModuleId,
    NonNegative, Number, Probability, SealedJournal, Slug, Text, Vector, Horizon,
)


class PayloadBase(Contract):
    applicable: bool = True
    reason: Text | None = None

    @model_validator(mode="after")
    def applicability_reason(self):
        if not self.applicable and self.reason is None:
            raise ValueError("non-applicable output needs a reason")
        if self.applicable and hasattr(self, "items") and not self.items:
            raise ValueError("empty output must explicitly declare non-applicability")
        return self


class FactorSignal(Contract):
    factor_id: Slug
    observation_ids: Annotated[tuple[UUID, ...], Field(min_length=1)]
    unit: Text
    level: Number
    change: Number | None
    velocity: Number | None
    acceleration: Number | None
    percentile: Probability | None
    normalized: Annotated[float, Field(strict=True, ge=-1, le=1)] | None
    quality: Probability


class DataInterpretation(PayloadBase):
    kind: Literal["E01"] = "E01"
    items: tuple[FactorSignal, ...]


class EvidenceSpan(Contract):
    evidence_ref: Text
    start: Count
    end: Count

    @model_validator(mode="after")
    def bounds(self):
        if self.end <= self.start:
            raise ValueError("evidence span must be nonempty")
        return self


class StructuredEvent(Contract):
    event_id: UUID
    event_type: Slug
    actor_ids: tuple[Slug, ...]
    factor_refs: tuple[Slug, ...]
    actual: Number | None
    unit: Text
    occurred_at: AwareDatetime
    published_at: AwareDatetime
    evidence_spans: Annotated[tuple[EvidenceSpan, ...], Field(min_length=1)]


class EventUnderstanding(PayloadBase):
    kind: Literal["E02"] = "E02"
    items: tuple[StructuredEvent, ...]


class SurpriseObject(Contract):
    event_id: UUID
    actual: Number
    expected: Number | None
    surprise: Number | None
    scale: Annotated[float, Field(strict=True, gt=0)] | None
    consensus_ids: tuple[Text, ...]

    @model_validator(mode="after")
    def unknown_consensus(self):
        if self.surprise is not None and (self.expected is None or self.scale is None or not self.consensus_ids):
            raise ValueError("normalized surprise requires consensus and scale")
        return self


class ExpectationSurprise(PayloadBase):
    kind: Literal["E03"] = "E03"
    items: tuple[SurpriseObject, ...]


class PricedInEstimate(Contract):
    event_id: UUID
    surprise_id: UUID
    priced_in_fraction: Probability | None
    residual_shock: Number | None
    pre_event_start: AwareDatetime
    pre_event_end: AwareDatetime

    @model_validator(mode="after")
    def known_residual(self):
        if self.pre_event_start >= self.pre_event_end:
            raise ValueError("pre-event window must be ordered")
        if self.priced_in_fraction is None and self.residual_shock is not None:
            raise ValueError("unknown priced-in fraction cannot yield known residual")
        return self


class PricedIn(PayloadBase):
    kind: Literal["E04"] = "E04"
    items: tuple[PricedInEstimate, ...]


class SituationState(PayloadBase):
    kind: Literal["E05"] = "E05"
    theme_ids: tuple[Slug, ...]
    positive_refs: tuple[Text, ...]
    negative_refs: tuple[Text, ...]
    conflict_ids: tuple[Text, ...]
    missing_ids: tuple[Text, ...]
    dominant_module_ids: tuple[ModuleId, ...]


class FactorContribution(Contract):
    factor_id: Slug
    contribution: Number


class OutgoingEffect(Contract):
    target: ModuleId
    effect: Number
    lag_days: NonNegative


class ModuleState(Contract):
    module_id: ModuleId
    score: Annotated[float, Field(strict=True, ge=-100, le=100)] | None
    direction: Literal["positive", "negative", "neutral", "unknown"]
    momentum: Number | None
    regime: Slug | None
    confidence: Probability | None
    coverage: Probability
    top_factors: tuple[FactorContribution, ...]
    outgoing_effects: tuple[OutgoingEffect, ...]

    @model_validator(mode="after")
    def unknown_is_not_neutral(self):
        if self.direction == "unknown" and self.score is not None:
            raise ValueError("unknown module must not contain a numeric score")
        if self.direction != "unknown" and (self.score is None or self.confidence is None):
            raise ValueError("known module needs score and confidence")
        return self


class StateEstimation(PayloadBase):
    kind: Literal["E06"] = "E06"
    items: tuple[ModuleState, ...]


class Hypothesis(Contract):
    hypothesis_id: UUID
    direction: Literal["up", "down", "flat"]
    horizon: Horizon
    claim_codes: tuple[Slug, ...]
    support_refs: tuple[Text, ...]
    contradict_refs: tuple[Text, ...]
    falsifiers: tuple[Falsifier, ...]


class HypothesisGeneration(PayloadBase):
    kind: Literal["E07"] = "E07"
    items: tuple[Hypothesis, ...]


class CausalPath(Contract):
    path_id: Text
    hypothesis_id: UUID
    node_ids: Annotated[tuple[Text, ...], Field(min_length=2, max_length=7)]
    edge_ids: Annotated[tuple[Text, ...], Field(min_length=1, max_length=6)]
    root_evidence_group: Text
    sign: Literal[-1, 1]
    strength: Probability
    confidence: Probability
    graph_version: Text

    @model_validator(mode="after")
    def simple_path(self):
        if len(self.node_ids) != len(self.edge_ids) + 1 or len(set(self.node_ids)) != len(self.node_ids):
            raise ValueError("causal path must be connected and cycle free")
        return self


class CausalExpansion(PayloadBase):
    kind: Literal["E08"] = "E08"
    items: tuple[CausalPath, ...]


class AdjustedPath(Contract):
    path_id: Text
    original_effect: Number
    adjusted_effect: Number
    adjustment_codes: tuple[Slug, ...]
    competing_refs: tuple[Text, ...]
    root_group: Text


class Interaction(PayloadBase):
    kind: Literal["E09"] = "E09"
    items: tuple[AdjustedPath, ...]


class NumericRange(Contract):
    low: Number
    high: Number

    @model_validator(mode="after")
    def ordered(self):
        if self.low > self.high:
            raise ValueError("range must be ordered")
        return self


class ActorResponse(Contract):
    actor_id: Slug
    trigger_refs: tuple[Text, ...]
    action_code: Slug
    response_range: NumericRange
    constraint_refs: tuple[Text, ...]
    feedback_refs: tuple[Text, ...]


class ActorReflexivity(PayloadBase):
    kind: Literal["E10"] = "E10"
    items: tuple[ActorResponse, ...]


class ConstraintResult(Contract):
    target_id: Text
    constraint_id: Slug
    lhs: Number
    rhs: Number
    tolerance: NonNegative
    valid: bool
    evidence_refs: tuple[Text, ...]


class ConstraintIdentity(PayloadBase):
    kind: Literal["E11"] = "E11"
    items: tuple[ConstraintResult, ...]


class TemporalPath(Contract):
    path_id: Text
    horizon: Horizon
    lag_hours: NonNegative
    active_fraction: Probability
    decay: Probability
    effect: Number


class TemporalReasoning(PayloadBase):
    kind: Literal["E12"] = "E12"
    items: tuple[TemporalPath, ...]


class HistoricalEvidence(PayloadBase):
    kind: Literal["E13"] = "E13"
    case_ids: tuple[Text, ...]
    similarity: Probability | None
    recency: Probability | None
    sample_count: Count
    regime_match: bool
    relevance: Probability
    capped_delta: Vector

    @model_validator(mode="after")
    def history_invariants(self):
        if self.sample_count != len(self.case_ids):
            raise ValueError("sample count must match case IDs")
        if abs(sum(self.capped_delta)) > 1e-9:
            raise ValueError("historical probability deltas must sum to zero")
        if not self.applicable and (any(self.capped_delta) or self.relevance != 0):
            raise ValueError("non-applicable history cannot change probabilities")
        return self


class ChallengeClaim(Contract):
    claim_code: Slug
    evidence_refs: Annotated[tuple[Text, ...], Field(min_length=1)]
    confidence: Probability


class ChallengeReport(PayloadBase):
    kind: Literal["E14"] = "E14"
    claims: tuple[ChallengeClaim, ...]
    refutation_refs: tuple[Text, ...]
    severity: Literal["none", "warning", "fatal"]
    fatal: bool
    replacement_hypothesis_id: UUID | None
    confidence: Probability

    @model_validator(mode="after")
    def supported_fatal(self):
        if self.fatal != (self.severity == "fatal") or (self.fatal and not self.refutation_refs):
            raise ValueError("fatal challenge must have consistent severity and evidence")
        return self


class Override(Contract):
    factor_id: Slug
    value: Number
    unit: Text


class ShockDistribution(Contract):
    distribution_id: Text
    factor_id: Slug
    family: Literal["normal", "empirical", "fixed"]
    location: Number
    scale: NonNegative
    version: Text


class Scenario(Contract):
    scenario_id: UUID
    scenario_kind: Literal["base", "upside", "downside", "tail", "user"]
    hypothesis_id: UUID
    prior_weight: Probability
    overrides: tuple[Override, ...]
    shock_distributions: tuple[ShockDistribution, ...]
    constraint_refs: tuple[Text, ...]

    @model_validator(mode="after")
    def distinct_overrides(self):
        if len({x.factor_id for x in self.overrides}) != len(self.overrides):
            raise ValueError("duplicate scenario override")
        return self


class ScenarioGeneration(PayloadBase):
    kind: Literal["E15"] = "E15"
    items: tuple[Scenario, ...]


class ValidatedScenario(Contract):
    scenario_id: UUID
    valid: bool
    violations: tuple[Slug, ...]
    accepted_distribution_refs: tuple[Text, ...]

    @model_validator(mode="after")
    def validation_consistent(self):
        if self.valid == bool(self.violations):
            raise ValueError("scenario validity contradicts violations")
        return self


class ConsistencyValidation(PayloadBase):
    kind: Literal["E16"] = "E16"
    items: tuple[ValidatedScenario, ...]


class SimulationResult(Contract):
    scenario_id: UUID
    seed: Count
    samples: Annotated[int, Field(strict=True, gt=0)]
    return_quantiles: Vector
    class_counts: tuple[Count, Count, Count]
    price_anchor: Annotated[float, Field(strict=True, gt=0)]
    distribution_version: Text

    @model_validator(mode="after")
    def sample_consistency(self):
        if sum(self.class_counts) != self.samples or tuple(sorted(self.return_quantiles)) != self.return_quantiles:
            raise ValueError("simulation counts or quantiles inconsistent")
        return self


class Simulation(PayloadBase):
    kind: Literal["E17"] = "E17"
    items: tuple[SimulationResult, ...]


class ProbabilityCalibration(PayloadBase):
    kind: Literal["E18"] = "E18"
    forecast: Forecast


class MetaCheck(PayloadBase):
    kind: Literal["E19"] = "E19"
    publishable: bool
    failed_checks: tuple[Slug, ...]
    offending_engines: tuple[EngineId, ...]
    driver_refs: tuple[Text, ...]
    falsifiers: tuple[Falsifier, ...]
    error_class: Slug | None

    @model_validator(mode="after")
    def publish_checks(self):
        if self.publishable and (not self.applicable or not self.driver_refs):
            raise ValueError("publication requires applicable meta check and drivers")
        if self.publishable and (self.failed_checks or self.offending_engines or self.error_class):
            raise ValueError("failed meta checks cannot publish")
        return self


PAYLOAD_TYPES = {cls.model_fields["kind"].default: cls for cls in (
    DataInterpretation, EventUnderstanding, ExpectationSurprise, PricedIn, SituationState,
    StateEstimation, HypothesisGeneration, CausalExpansion, Interaction, ActorReflexivity,
    ConstraintIdentity, TemporalReasoning, HistoricalEvidence, ChallengeReport,
    ScenarioGeneration, ConsistencyValidation, Simulation, ProbabilityCalibration, MetaCheck,
)}
Payload = Annotated[Union[tuple(PAYLOAD_TYPES.values())], Field(discriminator="kind")]


class Artifact(Contract):
    schema_version: Literal["1.0.0"] = "1.0.0"
    artifact_id: UUID
    run_id: UUID
    engine_id: EngineId
    engine_version: Text
    created_at: AwareDatetime
    data_cutoff: AwareDatetime
    input_artifact_ids: tuple[UUID, ...] = ()
    evidence_refs: tuple[Text, ...] = ()
    payload: Payload

    @model_validator(mode="after")
    def matching_engine(self):
        if self.engine_id != self.payload.kind:
            raise ValueError("engine ID does not match payload kind")
        if self.created_at < self.data_cutoff:
            raise ValueError("artifact creation cannot precede its cutoff")
        if isinstance(self.payload, ProbabilityCalibration) and (
            self.payload.forecast.run_id != self.run_id or self.payload.forecast.data_cutoff != self.data_cutoff
        ):
            raise ValueError("forecast candidate run/cutoff differs from envelope")
        return self


class Warning(Contract):
    code: Slug
    message: Text
    severity: Literal["info", "warning", "error"] = "warning"
    evidence_refs: tuple[Text, ...] = ()


class EngineResult(Contract):
    status: Literal["success", "insufficient_evidence", "conflict", "retry", "failed"]
    output_artifact: Artifact | None = None
    confidence: Probability | None = None
    evidence_refs: tuple[Text, ...] = ()
    warnings: tuple[Warning, ...] = ()
    next_engine: EngineId | None = None
    retry_engine: EngineId | None = None
    trace_id: UUID

    @model_validator(mode="after")
    def valid_status(self):
        if self.status == "success":
            if self.output_artifact is None or self.confidence is None:
                raise ValueError("success requires typed artifact and confidence")
            payload = self.output_artifact.payload
            if payload.applicable and not (self.evidence_refs or self.output_artifact.evidence_refs):
                raise ValueError("applicable success requires evidence")
            if self.retry_engine is not None:
                raise ValueError("success cannot request retry")
            if hasattr(payload, "confidence") and payload.confidence != self.confidence:
                raise ValueError("result/payload confidence mismatch")
            if isinstance(payload, ProbabilityCalibration) and payload.forecast.confidence != self.confidence:
                raise ValueError("result/forecast confidence mismatch")
        else:
            if self.output_artifact is not None or not self.warnings:
                raise ValueError("non-success requires diagnostic warnings and no output")
            if self.status == "retry" and self.retry_engine is None:
                raise ValueError("retry requires an offending engine")
            if self.status != "retry" and self.retry_engine is not None:
                raise ValueError("only retry status can request retry")
        return self


JournalSnapshot.model_rebuild(_types_namespace={"Artifact": Artifact})
SealedJournal.model_rebuild(_types_namespace={"Artifact": Artifact})
