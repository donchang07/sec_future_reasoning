"""Offline entry point: python -m reasoning validate|export-schemas|release-check."""
import argparse
import json
from pathlib import Path

from .validation import export_schemas, release_ready, validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "export-schemas", "release-check", "run-fixture", "inspect-journal", "verify-journal"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--results", type=Path)
    parser.add_argument("--fixture", type=Path, default=Path('fixtures/samsung-preferred-v1.json'))
    parser.add_argument("--output", type=Path, default=Path('artifacts/local/prediction-journal.json'))
    parser.add_argument("--journal", type=Path)
    parser.add_argument("--horizon", choices=('1w','1m','1y'))
    parser.add_argument("--engine", choices=tuple(f'E{i:02}' for i in range(1,20)))
    parser.add_argument("--generation", type=int, choices=(0,1))
    parser.add_argument("--replay", action='store_true')
    args = parser.parse_args()
    try:
        if args.command in ('run-fixture','inspect-journal','verify-journal'):
            from .fixture import Fixture
            from .workflow import run_fixture
            from .journal import SealedRun, write_journal, read_journal
            if args.command=='run-fixture':
                snapshot=run_fixture(Fixture.model_validate_json(args.fixture.read_text(encoding='utf-8')))
                write_journal(args.output,SealedRun.seal(snapshot))
                print(json.dumps({'run_id':str(snapshot.run_id),'journal':str(args.output),'executions':len(snapshot.executions),
                    'horizons':[dict(horizon=h.horizon,probabilities=h.final.probabilities.model_dump() if h.final else None,
                        confidence=h.final.confidence if h.final else None,decision=h.decision.action) for h in snapshot.horizons]},indent=2))
            else:
                sealed=read_journal(args.journal or args.output)
                if args.command=='verify-journal':
                    if args.replay and run_fixture(sealed.snapshot.input_fixture)!=sealed.snapshot:
                        raise ValueError('replay differs: inspect source/model/graph/calibration versions')
                    print(json.dumps({'valid':True,'sha256':sealed.sha256,'replayed':args.replay,'executions':len(sealed.snapshot.executions)}))
                else:
                    records=[r.model_dump(mode='json') for r in sealed.snapshot.executions
                        if (args.horizon is None or r.horizon==args.horizon) and (args.engine is None or r.engine_id==args.engine)
                        and (args.generation is None or r.generation==args.generation)]
                    print(json.dumps(records,ensure_ascii=False,indent=2))
        elif args.command == "export-schemas":
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
