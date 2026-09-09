"""Reproducibly transcribe reviewed design data; never synthesize market observations."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from reasoning.validation import build_registry, build_catalog, write_json


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    write_json(root / "ontology/registry.json", build_registry(root))
    write_json(root / "tests/golden/catalog.json", build_catalog(root))
    print("Generated reviewed registry and unresolved Golden catalog")
