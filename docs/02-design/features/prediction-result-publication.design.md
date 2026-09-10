# Prediction result publication — Design

2026-09-11. Publisher version prediction-publication-v1.0.0.

## Boundary and artifacts
Add publication/ package and scripts/install-result-publication.ps1. Do not edit forward_ops/, reasoning/, config/ or the existing prediction scheduler script: they belong to previously sealed operations manifests. A separate hidden Windows task runs every five minutes and reads completed registered v2 runs; it never invokes prediction. Existing 07:00 execution stays unchanged.

Export docs/predictions/KST-date/run_id/journal.json as the exact sealed system journal, verified against the registered baseline_journal_sha256. Generate deterministic explainability.md from that validated system journal using the existing report renderer, with a publication header explaining unavailable reversal sentinels. Store public Outcome seals separately under outcomes/horizon.json, checking prediction hash/run links. Keep prediction/report bytes immutable; an existing different artifact is an error. Publish an index README linking each run. Backfill registered historical runs as well as 9/11.

Only public v2 live_forward system output is eligible. Reject unknown top-level journal fields, unknown source IDs, private holdings, credential patterns and unexpected Outcome fields. Outer operational records, human forecasts, positioning/event submissions, worker logs and raw bundles are never exported. Copy no arbitrary user-supplied report file: render from the validated public journal.

## Git and retry transaction
Use configured origin/main and repository main only. Fetch first; reject divergent remote history and unrelated unpushed commits. Allow only outstanding docs/predictions commits as retryable publication commits. Reject unrelated staged paths; tolerate unrelated unstaged files without touching them. Commit exact exported paths using --only, validate the resulting commit changes only docs/predictions, then push the captured commit hash (never an unconstrained later HEAD; never force).

If a network push fails after commit, the next invocation verifies that the outstanding diff is confined to docs/predictions and retries the existing commit without rerunning inference or changing journals. If remote history diverges, report failure and retain artifacts; no automatic rebase/merge of user work. Use an exclusive local publisher lock and a bounded git timeout. Record timestamped local status/error logs outside Git. Repeat successful runs create no new commit. Every task invocation also reconciles publication of new linked public outcomes.

## Verification and rollout
Tests: exact seal export; report generation; no outer shadow/human/raw leakage; unknown/private fields refused; immutable collision refused; Outcome hash binding; git idempotency; unrelated unstaged/staged scope; push failure retry; divergent remote refusal. Use temporary local bare Git remotes for transaction tests. Run all 266 existing tests plus publication tests and CI before installing the recurring task. Verify today's GitHub file and old replay, task trigger, and unchanged existing operations manifest. Persist user preference in AGENTS.md. No new forecast is created.
