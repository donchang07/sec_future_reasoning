"""Domain contracts. No forecast algorithms or decision thresholds live here."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Annotated, Literal, TYPE_CHECKING
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

if TYPE_CHECKING:
    from .artifacts import Artifact

Number = Annotated[float, Field(strict=True, allow_inf_nan=False)]
Probability = Annotated[float, Field(strict=True, ge=0, le=1, allow_inf_nan=False)]
NonNegative = Annotated[float, Field(strict=True, ge=0, allow_inf_nan=False)]
Text = Annotated[str, Field(strict=True, min_length=1, pattern=r"\S")]
Slug = Annotated[str, Field(strict=True, pattern=r"^[a-z][a-z0-9_-]*$")]
Count = Annotated[int, Field(strict=True, ge=0)]
EngineId = Literal["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10",
                   "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19"]
ENGINE_IDS = tuple(f"E{i:02}" for i in range(1, 20))
Horizon = Literal["1d", "1w", "1m", "3m", "1y"]
ModuleId = Literal["macro", "ai_demand", "memory", "supply", "earnings", "capital_flow",
                   "valuation", "preferred", "market_regime"]
MODULE_IDS = ("macro", "ai_demand", "memory", "supply", "earnings", "capital_flow",
              "valuation", "preferred", "market_regime")
Vector = tuple[Number, Number, Number]


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False,
                              validate_default=True, revalidate_instances="always")


class EngineVersion(Contract):
    engine_id: EngineId
    version: Text


class VersionBundle(Contract):
    ontology: Text
    graph: Text
    model: Text
    prompt: Text
    calibration: Text
    policy: Text
    source_registry: Text
    calendar: Text
    code_commit: Annotated[str, Field(pattern=r"^[0-9a-f]{40}$")]
    engines: tuple[EngineVersion, ...]

    @model_validator(mode="after")
    def complete_engines(self):
        ids = [item.engine_id for item in self.engines]
        if len(ids) != 19 or set(ids) != set(ENGINE_IDS):
            raise ValueError("all 19 distinct engine versions must be pinned")
        return self


class Observation(Contract):
    observation_id: UUID
    factor_id: Slug
    source_id: Slug
    revision_id: Text
    unit: Text
    value: Number
    observed_at: AwareDatetime
    published_at: AwareDatetime
    available_at: AwareDatetime

    @model_validator(mode="after")
    def chronology(self):
        if not self.observed_at <= self.published_at <= self.available_at:
            raise ValueError("observation chronology must be observed <= published <= available")
        return self


def select_as_of(observations: tuple[Observation, ...], cutoff: datetime) -> tuple[Observation, ...]:
    """Keep source conflicts separate; select revisions only known at cutoff."""
    if cutoff.tzinfo is None or cutoff.utcoffset() is None:
        raise ValueError("cutoff must be timezone aware")
    selected: dict[tuple, Observation] = {}
    for item in observations:
        if item.published_at > cutoff or item.available_at > cutoff:
            continue
        key = (item.factor_id, item.source_id, item.observed_at)
        old = selected.get(key)
        if old is None or (item.available_at, item.published_at, str(item.observation_id)) > (
                old.available_at, old.published_at, str(old.observation_id)):
            selected[key] = item
    return tuple(sorted(selected.values(), key=lambda x: (x.factor_id, x.source_id, x.observed_at)))


class ProbabilityVector(Contract):
    up: Probability
    down: Probability
    flat: Probability

    @model_validator(mode="after")
    def normalized(self):
        if abs(self.up + self.down + self.flat - 1.) > 1e-9:
            raise ValueError("probabilities must sum to 1")
        return self

    def vector(self) -> Vector:
        return self.up, self.down, self.flat


class Contribution(Contract):
    sequence: Count
    stage: Literal["causal", "scenario", "challenge", "history", "calibration", "history_cap"]
    engine_id: EngineId
    version: Text
    evidence_refs: tuple[Text, ...]
    edge_ids: tuple[Text, ...] = ()
    before: ProbabilityVector
    after: ProbabilityVector
    delta_pp: Vector

    @model_validator(mode="after")
    def correct_delta(self):
        for before, after, delta in zip(self.before.vector(), self.after.vector(), self.delta_pp):
            if abs(100 * (after - before) - delta) > 1e-9:
                raise ValueError("contribution delta does not reconstruct probability change")
        return self


class Falsifier(Contract):
    factor_id: Slug
    operator: Literal["gt", "ge", "lt", "le", "eq"]
    threshold: Number
    unit: Text
    horizon: Horizon
    evidence_refs: tuple[Text, ...]


class Forecast(Contract):
    schema_version: Literal["1.0.0"] = "1.0.0"
    forecast_id: UUID
    run_id: UUID
    horizon: Horizon
    data_cutoff: AwareDatetime
    target_at: AwareDatetime
    versions: VersionBundle
    prior: ProbabilityVector
    probabilities: ProbabilityVector
    without_history_probabilities: ProbabilityVector
    ledger: tuple[Contribution, ...]
    confidence: Probability
    price_low: NonNegative
    price_high: NonNegative
    calibration_status: Literal["unvalidated", "validated"]
    evidence_refs: Annotated[tuple[Text, ...], Field(min_length=1)]
    falsifiers: tuple[Falsifier, ...] = ()

    @model_validator(mode="after")
    def consistent_forecast(self):
        if self.target_at <= self.data_cutoff:
            raise ValueError("target must be after cutoff")
        if self.price_low > self.price_high:
            raise ValueError("price range is reversed")
        previous = self.prior.vector()
        for index, row in enumerate(self.ledger):
            if row.sequence != index or any(abs(a-b) > 1e-9 for a, b in zip(previous, row.before.vector())):
                raise ValueError("ledger sequence or before/after chain is broken")
            previous = row.after.vector()
        if any(abs(a-b) > 1e-9 for a, b in zip(previous, self.probabilities.vector())):
            raise ValueError("ledger must reconstruct final probabilities")
        return self


def canonical_json(model: Contract) -> str:
    def normalize(value):
        if isinstance(value, datetime):
            return value.astimezone(timezone.utc).isoformat()
        if isinstance(value, UUID):
            return str(value)
        if isinstance(value, dict):
            return {key: normalize(item) for key, item in value.items()}
        if isinstance(value, (tuple, list)):
            return [normalize(item) for item in value]
        return value
    return json.dumps(normalize(model.model_dump(mode="python")), ensure_ascii=False,
                      sort_keys=True, separators=(",", ":"), allow_nan=False)


def canonical_hash(model: Contract) -> str:
    return hashlib.sha256(canonical_json(model).encode("utf-8")).hexdigest()


class JournalSnapshot(Contract):
    forecast: Forecast
    observations: tuple[Observation, ...]
    artifacts: tuple[Artifact, ...] = ()

    @model_validator(mode="after")
    def snapshot_cutoff(self):
        if len({x.observation_id for x in self.observations}) != len(self.observations):
            raise ValueError("duplicate observation in journal")
        if len({x.artifact_id for x in self.artifacts}) != len(self.artifacts):
            raise ValueError("duplicate artifact in journal")
        for observation in self.observations:
            if observation.available_at > self.forecast.data_cutoff:
                raise ValueError("journal contains evidence unavailable at cutoff")
        for artifact in self.artifacts:
            if artifact.run_id != self.forecast.run_id or artifact.data_cutoff != self.forecast.data_cutoff:
                raise ValueError("journal artifact run/cutoff mismatch")
            expected = {x.engine_id: x.version for x in self.forecast.versions.engines}
            if artifact.engine_version != expected[artifact.engine_id]:
                raise ValueError("journal artifact engine version mismatch")
        return self


class SealedJournal(Contract):
    snapshot: JournalSnapshot
    sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]

    @model_validator(mode="after")
    def verify(self):
        if self.sha256 != canonical_hash(self.snapshot):
            raise ValueError("journal snapshot hash mismatch")
        return self

    @classmethod
    def seal(cls, snapshot: JournalSnapshot) -> SealedJournal:
        return cls(snapshot=snapshot, sha256=canonical_hash(snapshot))
