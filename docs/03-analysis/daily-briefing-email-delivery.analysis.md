# Daily briefing email delivery — Check

> Date: 2026-09-15 | Design: `docs/02-design/features/daily-briefing-email-delivery.design.md`
> Checked implementation: `22a65616fca6dba70c60b0eddfcba5dbafe1abad`

## Match rate: 100% (10/10)

The implementation matches all Plan functional requirements. Email is a post-publication delivery projection only: it neither invokes prediction nor changes a sealed Journal, the professional briefing, forecast values, or Decision Policy.

| Requirement | Result | Evidence |
|---|---|---|
| DE-F01 deterministic multipart presentation | Match | `render_email_envelope` emits fixed UTF-8 plain-text and inline-styled HTML alternatives with navy/cyan/gold design. |
| DE-F02 stored typed values only | Match | Renderer consumes stored horizons, confidence, action, timing, alignment, liquidity, source state, P0, and run metadata; no inference call composes content. |
| DE-F03 official Daily after Git publication | Match | `publication.__main__` calls `publish` first; selector admits only validated `live_forward`, non-held, approved-contract `official_preopen` records. |
| DE-F04 local-only recipient/config | Match | Installer writes `email-config.json` below ignored `artifacts/local/publication`; real contact data does not appear in tracked files or task metadata. |
| DE-F05 ledger idempotency | Match | Atomic local ledger key is run ID + recipient + renderer version; second live reconciliation returned `noop`. |
| DE-F06 Gmail Sent recovery | Match | Transport prompt requires exact recipient/subject Sent search; live reconciliation recovered today's existing message without a second send. |
| DE-F07 bounded windowless transport | Match | Native Codex uses ephemeral, read-only, low-effort execution, strict output schema, 180-second timeout, captured output, `shell=False`, and `CREATE_NO_WINDOW`. |
| DE-F08 activation boundary/backlog | Match | Selector excludes pre-activation dates, keeps the latest run per KST day, and orders unsent days oldest first. |
| DE-F09 independent retry semantics | Match | Initial transport identity mismatch failed closed after Git synchronization; no ledger success was written and the next run recovered safely. |
| DE-F10 daily task safety | Match | Live task is Ready with one daily trigger, no repetition, `pythonw.exe -m publication`, 10-minute limit, and next run at 2026-09-16 07:15 KST. |

## Test evidence

- Test-first collection initially failed because `publication.email_delivery` did not exist.
- Focused renderer, delivery, schedule, and briefing suite: **18 passed**.
- Full repository regression suite after the final transport correction: **298 passed**.
- Tests cover presentation values, escaping, explicit Unknown/withheld handling, selection gates, activation boundary, daily deduplication, local-ledger idempotency, corrupt-ledger fail-closed behavior, subprocess restrictions, result identity checks, disabled configuration, and installer privacy/schedule contracts.

## Live evidence

- Local email configuration was created with activation date 2026-09-15; recipient and Gmail identifiers remain ignored local state.
- First post-install reconciliation: Git `pushed=false`, email `status=complete`, `delivered=1`, `recovered=1`. Gmail Sent search showed exactly the previously approved message, not a duplicate.
- Immediate second reconciliation: Git `pushed=false`, email `status=noop`, reason `No pending official Daily briefing`; no transport agent was invoked.
- Live Windows task: `Ready`, start boundary 2026-09-16 07:15 KST, days interval 1, no repetition interval, execution limit `PT10M`, action project `pythonw.exe -m publication`.
- Local config, ledger, outbox, and result files all resolve through `.gitignore` rule `artifacts/local/`.
- Today's immutable artifacts remained byte-identical:
  - Journal SHA-256: `84EC3D6C2914BC325EFF895AA0A9DDF2F2B1F25645D88F489B2358EA8B552AD8`
  - Explainability SHA-256: `C408004379EA4F838D3AB9FF9459BB2C8CAC958B89A22BA8977C455B0384FAB1`

## Corrective iteration during Check

The first live attempt prohibited all non-Gmail tools while asking the transport agent to read a local envelope path. The agent therefore could not obtain the envelope and returned placeholder identity fields. Validation rejected the result, no ledger success was written, and Gmail retained exactly one existing message.

Design and implementation were corrected to have Python read the local outbox and inject the serialized envelope through standard input. This keeps contact data out of the process command line, requires no shell/filesystem tool from the agent, and retains a Gmail-only tool boundary. Both focused and full suites passed after the correction, and live recovery then succeeded.

## Residual operational constraints

- The PC, logged-in user session, GitHub network path, Codex authentication, and Gmail plugin connection must be available at execution time.
- A Gmail or Codex outage leaves the public Git result intact and defers only email delivery until a later manual or scheduled invocation.
- The scheduled transport incurs one lightweight Codex run per previously unsent Daily date; normal ledger no-op days do not invoke it.

## Recommendation

Proceed to completion report. No product or architecture gap remains in this feature scope, and no new prediction was created.
