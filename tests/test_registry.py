import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from reasoning.registry import Registry
from reasoning.validation import validate_repository, release_ready, build_catalog, PRD

ROOT = Path(__file__).resolve().parents[1]


def test_registry_and_schema_match_source_documents():
    result = validate_repository(ROOT)
    assert result == {"factors": 49, "modules": 9, "engines": 19, "golden_cases": 80}


def test_duplicate_missing_or_connected_without_provider_rejected():
    data = json.loads((ROOT / "ontology/registry.json").read_text(encoding="utf-8"))
    data["factors"][0]["factor_id"] = data["factors"][1]["factor_id"]
    with pytest.raises(ValidationError):
        Registry.model_validate_json(json.dumps(data))
    data = json.loads((ROOT / "ontology/registry.json").read_text(encoding="utf-8"))
    data["factors"].pop()
    with pytest.raises(ValidationError):
        Registry.model_validate_json(json.dumps(data))
    data = json.loads((ROOT / "ontology/registry.json").read_text(encoding="utf-8"))
    data["factors"][0]["source_status"] = "connected"
    with pytest.raises(ValidationError):
        Registry.model_validate_json(json.dumps(data))


def test_catalog_is_not_a_passing_golden_suite():
    catalog = json.loads((ROOT / "tests/golden/catalog.json").read_text(encoding="utf-8"))
    assert len(catalog["cases"]) == 80
    assert not release_ready(catalog)
    assert {case["execution_status"] for case in catalog["cases"]} == {"unresolved"}


def test_empty_release_results_fail_closed():
    assert not release_ready({"cases": []})


def test_source_hash_is_independent_of_git_checkout_line_endings(tmp_path):
    source_path = tmp_path / PRD
    source_path.parent.mkdir(parents=True)
    source = (ROOT / PRD).read_bytes().replace(b"\r\n", b"\n")
    source_path.write_bytes(source)
    first = build_catalog(tmp_path)
    source_path.write_bytes(source.replace(b"\n", b"\r\n"))
    assert build_catalog(tmp_path) == first


def test_release_cli_reports_unresolved_catalog_explicitly():
    import subprocess
    import sys
    result = subprocess.run([sys.executable, "-m", "reasoning", "release-check"],
                            cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 1
    assert json.loads(result.stdout) == {"release_ready": False, "cases": 80}
