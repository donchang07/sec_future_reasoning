"""Contract gates written before the implementation; not forecast accuracy tests."""
import json
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from reasoning.schemas.contracts import (
    ProbabilityVector, Contribution, Forecast, Observation, VersionBundle,
    EngineVersion, JournalSnapshot, SealedJournal, select_as_of, canonical_hash,
)
from reasoning.schemas.artifacts import Artifact, EngineResult, PAYLOAD_TYPES

NOW = datetime(2026, 9, 9, tzinfo=timezone.utc)


def versions():
    return VersionBundle(**{key: "test-v1" for key in (
        "ontology", "graph", "model", "prompt", "calibration", "policy", "source_registry", "calendar"
    )}, code_commit="a" * 40,
        engines=tuple(EngineVersion(engine_id=f"E{i:02}", version="1.0.0") for i in range(1, 20)))


def forecast():
    prior = ProbabilityVector(up=.5, down=.3, flat=.2)
    final = ProbabilityVector(up=.6, down=.25, flat=.15)
    row = Contribution(sequence=0, stage="causal", engine_id="E18", version="test-v1",
                       evidence_refs=("obs-1",), edge_ids=("edge-1",), before=prior,
                       after=final, delta_pp=(10., -5., -5.))
    return Forecast(forecast_id=uuid4(), run_id=uuid4(), horizon="1m", data_cutoff=NOW,
                    target_at=NOW + timedelta(days=30), versions=versions(), prior=prior,
                    probabilities=final, without_history_probabilities=final, ledger=(row,),
                    confidence=.7, price_low=60000., price_high=80000.,
                    calibration_status="unvalidated", evidence_refs=("obs-1",))


def observation(**updates):
    values = dict(observation_id=uuid4(), factor_id="us_10y_yield", source_id="test-source",
                  revision_id="r1", unit="percent", value=4.2, observed_at=NOW,
                  published_at=NOW, available_at=NOW)
    values.update(updates)
    return Observation(**values)


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), -.1, 1.1, True, "0.5"])
def test_invalid_probability(bad):
    with pytest.raises(ValidationError):
        ProbabilityVector(up=bad, down=.3, flat=.2)


def test_probability_sum_and_extra_fields():
    with pytest.raises(ValidationError):
        ProbabilityVector(up=.5, down=.3, flat=.3)
    with pytest.raises(ValidationError):
        ProbabilityVector(up=.5, down=.3, flat=.2, fabricated=True)


def test_forecast_ledger_reconstructs_and_roundtrips():
    item = forecast()
    assert Forecast.model_validate_json(item.model_dump_json()) == item
    assert item.ledger[-1].after == item.probabilities


@pytest.mark.parametrize("change", [
    {"delta_pp": [9., -5., -5.]}, {"sequence": 2},
    {"before": {"up": .4, "down": .4, "flat": .2}, "delta_pp": [20., -15., -5.]},
])
def test_ledger_corruption_is_rejected(change):
    data = forecast().model_dump(mode="json")
    data["ledger"][0].update(change)
    with pytest.raises(ValidationError):
        Forecast.model_validate_json(json.dumps(data))


def test_target_and_price_range():
    data = forecast().model_dump(mode="json")
    data["target_at"] = NOW.isoformat()
    with pytest.raises(ValidationError):
        Forecast.model_validate_json(json.dumps(data))
    data = forecast().model_dump(mode="json")
    data["price_low"] = 90000
    with pytest.raises(ValidationError):
        Forecast.model_validate_json(json.dumps(data))


def test_naive_time_and_availability_order():
    with pytest.raises(ValidationError):
        observation(observed_at=NOW.replace(tzinfo=None))
    with pytest.raises(ValidationError):
        observation(published_at=NOW + timedelta(days=1))


def test_revision_selection_prevents_future_leak_and_keeps_conflicting_sources():
    first = observation()
    future = observation(revision_id="r2", value=4.8, available_at=NOW + timedelta(days=1))
    other = observation(source_id="other-source", value=4.6)
    assert set(x.observation_id for x in select_as_of((future, other, first), NOW)) == {
        first.observation_id, other.observation_id}
    assert future in select_as_of((future, first), NOW + timedelta(days=1))


def test_all_engine_versions_required():
    data = versions().model_dump(mode="json")
    data["engines"].pop()
    with pytest.raises(ValidationError):
        VersionBundle.model_validate_json(json.dumps(data))


def test_journal_deep_immutability_hash_and_tampering():
    item = forecast()
    journal = JournalSnapshot(forecast=item, observations=(observation(),))
    sealed = SealedJournal.seal(journal)
    assert SealedJournal.model_validate_json(sealed.model_dump_json()) == sealed
    with pytest.raises(ValidationError):
        journal.forecast.confidence = .9
    with pytest.raises(TypeError):
        journal.observations[0] = observation()
    data = sealed.model_dump(mode="json")
    data["snapshot"]["forecast"]["confidence"] = .9
    with pytest.raises(ValidationError):
        SealedJournal.model_validate_json(json.dumps(data))
    assert canonical_hash(journal) == canonical_hash(JournalSnapshot.model_validate_json(journal.model_dump_json()))


def test_journal_rejects_observation_after_cutoff():
    with pytest.raises(ValidationError):
        JournalSnapshot(forecast=forecast(), observations=(observation(available_at=NOW+timedelta(days=1)),))


def test_success_missing_artifact_and_invalid_retry():
    with pytest.raises(ValidationError):
        EngineResult(status="success", confidence=.8, evidence_refs=("obs-1",), trace_id=uuid4())
    with pytest.raises(ValidationError):
        EngineResult(status="retry", trace_id=uuid4())


def test_unknown_result_stays_unknown():
    result = EngineResult(status="insufficient_evidence", trace_id=uuid4(),
                          warnings=({"code": "missing_data", "message": "No observations"},))
    assert result.confidence is None
    assert result.output_artifact is None


def test_engine_payload_discriminator_and_identity():
    assert set(PAYLOAD_TYPES) == {f"E{i:02}" for i in range(1, 20)}
    payload = {"kind": "E13", "applicable": False, "reason": "No mature historical cases",
               "case_ids": [], "similarity": None, "recency": None, "sample_count": 0,
               "regime_match": False, "relevance": 0., "capped_delta": [0., 0., 0.]}
    base = dict(artifact_id=str(uuid4()), run_id=str(uuid4()), engine_id="E13", engine_version="1.0.0",
                created_at=NOW.isoformat(), data_cutoff=NOW.isoformat(), payload=payload)
    artifact = Artifact.model_validate_json(json.dumps(base))
    assert artifact.payload.kind == "E13"
    base["engine_id"] = "E01"
    with pytest.raises(ValidationError):
        Artifact.model_validate_json(json.dumps(base))


def test_canonical_time_normalization():
    first = observation()
    data = first.model_dump()
    data["observed_at"] = NOW.astimezone(timezone(timedelta(hours=9)))
    assert canonical_hash(first) == canonical_hash(Observation(**data))


def test_success_rejects_empty_applicable_output_and_missing_evidence():
    base = dict(artifact_id=uuid4(), run_id=uuid4(), engine_id="E01", engine_version="1.0.0",
                created_at=NOW, data_cutoff=NOW, payload={"kind": "E01", "items": []})
    with pytest.raises(ValidationError):
        Artifact(**base)
    base["payload"] = {"kind": "E05", "theme_ids": [], "positive_refs": [], "negative_refs": [],
                       "conflict_ids": [], "missing_ids": [], "dominant_module_ids": []}
    base["engine_id"] = "E05"
    artifact = Artifact(**base)
    with pytest.raises(ValidationError):
        EngineResult(status="success", output_artifact=artifact, confidence=.8, trace_id=uuid4())


def test_unknown_module_cannot_be_numeric_neutral():
    from reasoning.schemas.artifacts import ModuleState
    data = dict(module_id="memory", score=0., direction="unknown", momentum=None, regime=None,
                confidence=None, coverage=0., top_factors=(), outgoing_effects=())
    with pytest.raises(ValidationError):
        ModuleState(**data)
    data["score"] = None
    assert ModuleState(**data).direction == "unknown"
    data["direction"] = "neutral"
    with pytest.raises(ValidationError):
        ModuleState(**data)


def test_journal_duplicate_observations_rejected():
    obs = observation()
    with pytest.raises(ValidationError):
        JournalSnapshot(forecast=forecast(), observations=(obs, obs))


def test_invalid_causal_path_and_scenario_counts():
    from reasoning.schemas.artifacts import CausalPath, SimulationResult, ValidatedScenario
    with pytest.raises(ValidationError):
        CausalPath(path_id="p1", hypothesis_id=uuid4(), node_ids=("a", "b", "a"),
                   edge_ids=("ab", "ba"), root_evidence_group="r1", sign=1,
                   strength=.5, confidence=.8, graph_version="v1")
    with pytest.raises(ValidationError):
        SimulationResult(scenario_id=uuid4(), seed=1, samples=10, class_counts=(5, 3, 1),
                         return_quantiles=(-.1, 0., .1), price_anchor=70000., distribution_version="v1")
    with pytest.raises(ValidationError):
        ValidatedScenario(scenario_id=uuid4(), valid=True, violations=("cash_identity",),
                          accepted_distribution_refs=())


@pytest.mark.parametrize("engine_id", [f"E{i:02}" for i in range(1, 20)])
def test_each_engine_roundtrip_and_extra_text_rejection(engine_id):
    """Explicit no-op artifacts exercise every union branch, not engine algorithms."""
    cls = PAYLOAD_TYPES[engine_id]
    payload = dict(kind=engine_id, applicable=False, reason="No applicable inputs in contract fixture")
    if "items" in cls.model_fields:
        payload["items"] = []
    if engine_id == "E05":
        payload.update(theme_ids=[], positive_refs=[], negative_refs=[], conflict_ids=[],
                       missing_ids=[], dominant_module_ids=[])
    elif engine_id == "E13":
        payload.update(case_ids=[], similarity=None, recency=None, sample_count=0,
                       regime_match=False, relevance=0., capped_delta=[0., 0., 0.])
    elif engine_id == "E14":
        payload.update(claims=[], refutation_refs=[], severity="none", fatal=False,
                       replacement_hypothesis_id=None, confidence=0.)
    elif engine_id == "E18":
        payload.update(forecast=forecast().model_dump(mode="json"))
        payload["applicable"] = True
    elif engine_id == "E19":
        payload.update(publishable=False, failed_checks=[], offending_engines=[], driver_refs=[],
                       falsifiers=[], error_class=None)
    data = dict(artifact_id=str(uuid4()), run_id=str(uuid4()), engine_id=engine_id,
                engine_version="1.0.0", created_at=NOW.isoformat(), data_cutoff=NOW.isoformat(), payload=payload)
    if engine_id == "E18":
        data["run_id"] = payload["forecast"]["run_id"]
    artifact = Artifact.model_validate_json(json.dumps(data))
    assert Artifact.model_validate_json(artifact.model_dump_json()) == artifact
    payload["unconstrained_reasoning"] = "Trust this text instead of evidence"
    with pytest.raises(ValidationError):
        Artifact.model_validate_json(json.dumps(data))
