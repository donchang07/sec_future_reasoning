"""Fail-closed release evidence validation. A status string is not execution proof."""
import hashlib
from pathlib import Path
from typing import Annotated, Literal
from uuid import UUID
from pydantic import Field, ValidationError
from .schemas.contracts import Contract, VersionBundle


class CaseEvidence(Contract):
    case_id: str
    execution_status: Literal["passed"]
    run_id: UUID
    fixture_hash: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
    versions: VersionBundle
    fixture_path: str
    journal_path: str


def verify_release(results, required_ids):
    try:
        cases = [CaseEvidence.model_validate(x) for x in results["cases"]]
        if len(cases) != len(required_ids) or {x.case_id for x in cases} != required_ids:
            return False
        # Until all original PRD assertions have executable evaluators, even a
        # well-formed journal cannot establish their success. Explicit fail closed.
        for case in cases:
            if hashlib.sha256(Path(case.fixture_path).read_bytes()).hexdigest() != case.fixture_hash:
                return False
            from .journal import read_journal
            journal = read_journal(Path(case.journal_path))
            if journal.snapshot.run_id != case.run_id or journal.snapshot.versions != case.versions:
                return False
        return False
    except (KeyError, TypeError, ValueError, OSError, ValidationError):
        return False
