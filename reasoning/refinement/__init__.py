"""Opt-in v2 contract API. No live collection or changes to the legacy engine path."""
from .types import CONTRACT_VERSION, MappingPolicy, SourceObservation, Candidate, Requirement
from .registry import MATRIX
from .mapping import map_observations
from .exports import select_vintages, export_signals
from .constraints import CompanyFinancials, MemoryBusiness, IndustrySupply, evaluate_e11
from .assessment import assess_contract, publish_candidate, infer_memory
