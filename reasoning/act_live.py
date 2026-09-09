"""Continue real-data-minimum-slice Act with immutable documentary evidence."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Literal
from pydantic import model_validator
from .act_sources import DOCUMENTS, Document, EvidenceBundle, assess, collect_document
from .live import RawSnapshot, LiveJournal, collect_snapshot, evaluate, explain, write_immutable
from .schemas.contracts import Contract, canonical_hash


class ActJournal(Contract):
    schema_version: Literal['act-1.0.0'] = 'act-1.0.0'
    feature: Literal['real-data-minimum-slice'] = 'real-data-minimum-slice'
    data_mode: Literal['live_forward'] = 'live_forward'
    documents: tuple[Document, ...]
    evidence: EvidenceBundle
    live: LiveJournal

    @model_validator(mode='after')
    def integrity(self):
        if len({d.source_id for d in self.documents}) != len(self.documents):
            raise ValueError('duplicate document source')
        if any(d.collected_at > self.live.data_cutoff for d in self.documents):
            raise ValueError('supplementary document after cutoff')
        if self.live.data_mode != self.data_mode:
            raise ValueError('mixed journal data mode')
        if assess(self.documents, self.live.data_cutoff) != self.evidence:
            raise ValueError('evidence does not reconstruct from original bytes')
        return self


class SealedAct(Contract):
    snapshot: ActJournal
    sha256: str

    @model_validator(mode='after')
    def integrity(self):
        if canonical_hash(self.snapshot) != self.sha256:
            raise ValueError('Act journal hash mismatch')
        return self


def evaluate_act(documents, market_snapshot):
    evidence = assess(documents, market_snapshot.data_cutoff)
    # No fake Accounting instance, no spot->contract substitution, no profile tuning.
    live = evaluate(market_snapshot)
    return ActJournal(documents=tuple(documents), evidence=evidence, live=live)


def report(journal):
    evidence, run = journal.evidence, journal.live.run
    lines = ['# real-data-minimum-slice — second forward evidence', '',
        f'Run ID: {run.run_id}', f'Data cutoff: {journal.live.data_cutoff.isoformat()}',
        'Data mode: live_forward. The frozen model ran after the additional source collection.', '',
        '**Not completed: supplementary source evidence is not a compatible replacement for missing critical contract ASP or original E11 inputs.**',
        'No supplemental values enter the probability algorithm. New source availability and model usability are reported separately.', '',
        '## Additional source status', '| Source | Status |', '|---|---|']
    lines.extend(f'| {key} | {value} |' for key, value in evidence.source_status.items())
    lines += ['', '## Source-level factors', '| Factor / scope | Value | Unit | Effective | Released | Collected | Mapping |', '|---|---:|---|---|---|---|---|']
    for f in evidence.facts:
        lines.append(f'| {f.factor_id}: {f.scope} | {f.value} | {f.unit} | {f.effective_at.isoformat()} | {f.released_at} | {f.collected_at.isoformat()} | {f.mapping} |')
    lines += ['', '## Export nowcast selection', 'Same-month releases are revisions; only the latest eligible release is selected. No sum, extrapolation, or model contribution.',
        '| Month | Days covered | USD million | Same-period YoY % | Source |', '|---|---:|---:|---:|---|']
    lines.extend(f'| {f.month} | {f.coverage_days} | {f.value} | {f.yoy_percent} | {f.source_id} |' for f in evidence.selected_exports)
    lines += ['', '## E11 evidence assessment', 'The following are independent statement checks, not the original E11 capacity/revenue/free-cash-flow identities.',
        '| Identity | Left | Right | Residual | Passed |', '|---|---:|---:|---:|---|']
    lines.extend(f'| {c.name} | {c.left} | {c.right} | {c.residual} | {c.passed} |' for c in evidence.checks)
    lines += ['Missing original E11 inputs: '+', '.join(evidence.original_e11_missing),
        'Missing critical factor: '+', '.join(evidence.missing_critical), '', '## Execution census']
    from collections import Counter
    lines.append(str(dict(Counter(e.result.status for e in run.executions))))
    lines += ['', '## Model forecast and decision', 'The following original live report describes engine-compatible inputs. The supplementary source tables above do not replace its unavailable inputs.', '', explain(journal.live)]
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('collect', 'replay', 'verify'))
    parser.add_argument('--output', type=Path, default=Path('artifacts/local/live'))
    parser.add_argument('--journal', type=Path)
    args = parser.parse_args()
    if args.command == 'collect':
        with ThreadPoolExecutor(max_workers=4) as pool:
            documents = tuple(pool.map(collect_document, DOCUMENTS))
        market = collect_snapshot()
        folder = args.output/str(market.snapshot_id)
        # Persist raw inputs before evaluation, including failures.
        write_immutable(folder/'raw-documents.json', {'documents': [d.model_dump(mode='json') for d in documents]})
        write_immutable(folder/'raw-snapshot.json', market)
        journal = evaluate_act(documents, market)
        sealed = SealedAct(snapshot=journal, sha256=canonical_hash(journal))
        write_immutable(folder/'prediction-journal.json', sealed)
        with (folder/'explainability.md').open('x', encoding='utf-8', newline='\n') as out:
            out.write(report(journal))
        write_immutable(folder/'outcome-schedule.json', {'run_id': str(journal.live.run.run_id), 'journal_sha256': sealed.sha256,
            'pending': {k: v.isoformat() for k, v in journal.live.outcome_due.items()}})
        print(f'journal={folder / "prediction-journal.json"}\nrun_id={journal.live.run.run_id}\nsha256={sealed.sha256}')
        print(journal.evidence.source_status)
    else:
        if args.journal is None:
            parser.error('--journal is required')
        sealed = SealedAct.model_validate_json(args.journal.read_text(encoding='utf-8'))
        if args.command == 'replay':
            replayed = evaluate_act(sealed.snapshot.documents, sealed.snapshot.live.raw_snapshot)
            if replayed != sealed.snapshot:
                raise ValueError('Act replay differs; use recorded code version')
        print(f'valid=True replayed={args.command == "replay"} sha256={sealed.sha256}')


if __name__ == '__main__':
    main()
