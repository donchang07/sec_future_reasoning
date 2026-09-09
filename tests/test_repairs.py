import json
from pathlib import Path
from datetime import datetime, timezone
from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError

from reasoning.validation import CASE_IDS, release_ready, build_registry
from reasoning.schemas.artifacts import Artifact, EngineResult
from reasoning.schemas.contracts import Observation, select_as_of

NOW = datetime(2026, 9, 9, tzinfo=timezone.utc)


def test_ck01_invalid_release_metadata_is_not_execution_evidence():
    data = {"cases": [dict(case_id=x, execution_status="passed", run_id="not-a-uuid",
                           fixture_hash="not-a-hash", versions="not-a-bundle") for x in CASE_IDS]}
    assert release_ready(data) is False


@pytest.mark.parametrize("applicable,drivers", [(False, ()), (True, ()), (False, ("source",))])
def test_ck02_meta_without_applicability_or_drivers_cannot_publish(applicable, drivers):
    with pytest.raises(ValidationError):
        artifact = Artifact(artifact_id=uuid4(), run_id=uuid4(), engine_id="E19", engine_version="1",
                            created_at=NOW, data_cutoff=NOW,
                            payload=dict(kind="E19", applicable=applicable, reason="no inputs", publishable=True,
                                         failed_checks=(), offending_engines=(), driver_refs=drivers,
                                         falsifiers=(), error_class=None))
        EngineResult(status="success", output_artifact=artifact, confidence=1., trace_id=uuid4())


@pytest.mark.parametrize("reverse", [False, True])
def test_ck03_ambiguous_same_source_revisions_raise_conflict(reverse):
    common = dict(factor_id="us_10y_yield", source_id="source", unit="percent",
                  observed_at=NOW, published_at=NOW, available_at=NOW)
    pair = (Observation(observation_id=UUID(int=2), revision_id="r1", value=4.2, **common),
            Observation(observation_id=UUID(int=1), revision_id="r2", value=4.8, **common))
    with pytest.raises(ValueError, match="revision conflict"):
        select_as_of(pair[::-1] if reverse else pair, NOW)


def test_ck04_factor_comparison_windows_have_independent_oracles():
    rows = {x["factor_id"]: x for x in build_registry(Path(__file__).resolve().parents[1])["factors"]}
    assert rows["samsung_eps_revision"]["comparison_period"] == "30_calendar_days"
    assert rows["dram_contract_asp"]["comparison_period"] == "1_calendar_month"
    assert rows["samsung_eps"]["comparison_period"] == "1_calendar_year"
    assert rows["preferred_rsi_14"]["comparison_period"] == "point_in_time"
    assert rows['us_cpi_yoy']['transform']=='diff'
    assert rows['gpu_demand_growth']['transform']=='level'
    assert rows['cxmt_memory_capacity']['comparison_period']=='1_calendar_month'
    assert rows['samsung_fcf']['transform']=='diff'
