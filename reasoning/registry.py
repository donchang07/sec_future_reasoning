"""Validated ontology metadata; no fabricated provider connections or factor values."""
from typing import Annotated, Literal

from pydantic import Field, model_validator

from .schemas.contracts import Contract, Count, Horizon, ModuleId, Slug, Text, MODULE_IDS


class ModuleDefinition(Contract):
    module_id: ModuleId
    name: Text


class Freshness(Contract):
    basis: Literal["trading_days", "calendar_days", "bars", "event"]
    maximum_age: Count | None
    source_definition: Text

    @model_validator(mode="after")
    def age_policy(self):
        if self.basis != "event" and (self.maximum_age is None or self.maximum_age < 1):
            raise ValueError("non-event freshness requires a positive age")
        return self


class FactorDefinition(Contract):
    factor_id: Slug
    module_id: ModuleId
    name_ko: Text
    value_definition: Text
    unit: Slug
    value_type: Literal["number"] = "number"
    transform: Literal["level", "diff", "pct_change", "log_return", "yoy", "ratio"]
    comparison_period: Text
    warmup: Count
    cadence: Text
    expected_release_at: Text | None
    freshness_sla: Freshness
    critical_for_horizons: tuple[Horizon, ...]
    source_candidates: Annotated[tuple[Literal["OFF", "MKT", "FIL", "IND", "DER"], ...], Field(min_length=1)]
    source_status: Literal["not_connected", "connected"]
    source_id: Slug | None
    series_id: Text | None
    timezone: Text | None
    provenance_class: Literal["E", "D", "P"]
    prd_reference: Text
    derived_from: tuple[Slug, ...]
    auxiliary_inputs: tuple[Slug, ...]
    economic_sign_by_regime: Literal["graph_defined"]
    quality_tolerance_rule: Text
    ontology_version: Text
    unresolved_fields: tuple[Text, ...]

    @model_validator(mode="after")
    def honest_source_status(self):
        if self.source_status == "connected" and (
            not self.source_id or not self.series_id or not self.timezone or self.unresolved_fields
        ):
            raise ValueError("connected factor needs a verified source mapping")
        if len(set(self.critical_for_horizons)) != len(self.critical_for_horizons):
            raise ValueError("duplicate critical horizon")
        return self


class Registry(Contract):
    schema_version: Literal["1.0.0"] = "1.0.0"
    ontology_version: Text
    modules: Annotated[tuple[ModuleDefinition, ...], Field(min_length=9, max_length=9)]
    factors: Annotated[tuple[FactorDefinition, ...], Field(min_length=49, max_length=49)]

    @model_validator(mode="after")
    def identities(self):
        if {module.module_id for module in self.modules} != set(MODULE_IDS):
            raise ValueError("registry must contain all nine modules")
        ids = [factor.factor_id for factor in self.factors]
        if len(set(ids)) != 49:
            raise ValueError("registry must contain 49 unique factors")
        if {factor.module_id for factor in self.factors} != set(MODULE_IDS):
            raise ValueError("every module needs factors")
        graph = {factor.factor_id: factor.derived_from for factor in self.factors}
        def visit(key, active):
            if key in active:
                raise ValueError("derived factor cycle")
            for dependency in graph[key]:
                if dependency not in graph:
                    raise ValueError("unknown derived factor dependency")
                visit(dependency, active | {key})
        for factor in self.factors:
            if factor.ontology_version != self.ontology_version:
                raise ValueError("mixed ontology versions")
            visit(factor.factor_id, set())
        return self
