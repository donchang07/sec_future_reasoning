"""Offline entry point: python -m reasoning validate|export-schemas|release-check."""
import argparse
import json
from pathlib import Path

from .validation import export_schemas, release_ready, validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "export-schemas", "release-check"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--results", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "export-schemas":
            export_schemas(args.root)
            print("Exported six versioned JSON Schemas")
        elif args.command == "validate":
            print(json.dumps(validate_repository(args.root), sort_keys=True))
        else:
            path = args.results or args.root / "tests/golden/catalog.json"
            results = json.loads(path.read_text(encoding="utf-8"))
            ready = release_ready(results)
            print(json.dumps({"release_ready": ready, "cases": len(results.get("cases", []))}))
            return 0 if ready else 1
    except (ValueError, OSError) as error:
        print(f"Validation failed: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
