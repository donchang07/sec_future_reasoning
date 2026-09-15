# Daily briefing email delivery — Plan

> Version: 1.0.0 | Date: 2026-09-15 | Status: Approved
> Level: Enterprise

## 1. Purpose

Extend the existing daily result-publication operation so that each newly published official pre-open briefing is also delivered once by email in the approved professional navy format. Delivery follows the existing 07:15 KST publication run and must never invoke prediction, recompute a decision, or modify a sealed Journal.

The connected Gmail account is already authorized and was manually verified with today's formatted briefing. The standing recipient is user-approved, but the address is personal contact data and therefore must remain in ignored local configuration rather than tracked source or public documentation.

## 2. Goals

- Send one professional HTML email for each new `official_preopen` Daily result after its public GitHub publication succeeds.
- Preserve the navy header, executive conclusion, horizon probability table, decision-gate explanation, data reliability summary, research-only notice, and full public briefing link used in the approved manual email.
- Run through the existing hidden `SEC-Frozen-Forward-Publish` task without opening console windows.
- Make normal retries idempotent through a local delivery ledger and a Gmail Sent-mail preflight check.
- Keep recipient data, Gmail message identifiers, dispatch prompts/results, and operational logs local and ignored.

## 3. Non-goals

- No change to the 19 engines, Price Wave/Reversal semantics, Multi-Timeframe Alignment, liquidity gates, forecast probabilities, Decision Policy, calibration, or any engine contract.
- No email for Event, Human Forecast, Shadow, held, private, raw-capture, or unsupported result records.
- No historical email backfill before the local activation date.
- No SMTP password, OAuth token, API key, Gmail credential, or recipient address in Git.
- No rewrite of an already sent email when a sealed result later gains a separate Outcome record.

## 4. Scope and operating policy

1. The existing 07:15 task runs `.venv\Scripts\pythonw.exe -m publication`.
2. The publisher validates and reconciles immutable public artifacts and returns only after `origin/main` is synchronized.
3. Email delivery selects at most the latest eligible `official_preopen` run per KST forecast date, beginning with the configured activation date.
4. A deterministic renderer creates both plain-text and HTML MIME alternatives from the validated typed Journal. It does not use a model for wording or decision logic.
5. A windowless, ephemeral Codex CLI invocation uses only the connected Gmail plugin to check Sent mail and either report the existing message or send the exact generated envelope once.
6. A successful Gmail message ID is recorded in a local atomic ledger. Missing configuration, no eligible result, or an already recorded run is a no-op.
7. Publication failure prevents delivery. Delivery failure is logged and retried on the next publication invocation without rerunning prediction.

## 5. Functional requirements

| ID | Requirement |
|---|---|
| DE-F01 | Generate a deterministic `multipart/alternative` envelope with professional navy HTML and a readable plain-text fallback. |
| DE-F02 | Use the sealed Journal's stored probabilities, confidence, action, timing, alignment, liquidity, source state, and evidence gaps without recomputation. |
| DE-F03 | Dispatch only eligible public `official_preopen` results after successful Git publication. |
| DE-F04 | Keep the approved recipient and activation date in `artifacts/local/publication/email-config.json`; never stage or publish them. |
| DE-F05 | Skip completed `(run_id, recipient, renderer_version)` deliveries from an atomic local ledger. |
| DE-F06 | Before a send, search Gmail Sent mail for the exact daily subject and recipient so a crash between send and ledger write does not cause a normal duplicate. |
| DE-F07 | Invoke Codex/Gmail without a console window, with a bounded timeout, read-only workspace access, an output schema, and no prediction command. |
| DE-F08 | Do not backfill dates earlier than local activation; support retry of unsent eligible dates on later runs. |
| DE-F09 | A Gmail failure must not roll back or alter a successful Git publication and must remain retryable. |
| DE-F10 | Preserve the existing once-daily 07:15 trigger, interactive limited principal, `StartWhenAvailable`, `IgnoreNew`, and hidden execution. |

## 6. Success criteria

- Renderer tests verify the approved headline, navy/gold/cyan palette, key metrics, plain-text fallback, escaping, and research-only notice.
- Selection tests reject Event/private/held/pre-activation records and choose one latest Daily run per KST date.
- Delivery tests cover missing config, ledger idempotency, Sent-mail recovery, subprocess flags, timeout/failure, malformed agent output, and atomic ledger updates without making real sends.
- Schedule-source tests retain one daily 07:15 trigger and allow sufficient bounded runtime for Git plus Gmail delivery.
- A live dry reconciliation of today's already-sent subject resolves to `already_sent` and records the existing Gmail message ID without sending a duplicate.
- The full regression suite passes, and today's Journal and explainability hashes remain unchanged.
- Plan, Design, Check, Report, and PDCA status updates are pushed with only feature-scoped files.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Connected Gmail authorization expires | Email retries fail | Preserve Git publication, log the delivery error locally, and retry after reconnecting Gmail. |
| Agent sends twice after a crash | Duplicate daily briefing | Local ledger plus exact Sent-mail subject/recipient preflight; unique daily subject. |
| Model changes generated email content | Inconsistent or invented briefing | Generate the complete MIME envelope deterministically in Python; the agent only transports exact fields. |
| Prompt injection through result text | Unauthorized tool behavior | Typed allowlisted Journal validation, HTML escaping, fixed dispatch instructions, read-only ephemeral CLI, and Gmail-only task wording. |
| Console windows reappear | User disruption | Parent remains `pythonw.exe`; all child Codex/Git subprocesses use `CREATE_NO_WINDOW`. |
| Contact data leaks to Git | Privacy breach | Store recipient, envelope, ledger, and result files only under ignored `artifacts/local/`; tests use reserved example addresses. |
| 07:15 run exceeds old task limit | Forced termination after successful send | Increase the bounded task execution limit while retaining `IgnoreNew` and hidden operation. |

## 8. Rollout and rollback

Implement test-first after Design approval. Install the updated task with a local recipient parameter, then run one manual publication reconciliation. Today's already-delivered email must be detected rather than resent. Rollback disables/removes only the local email configuration or restores the prior publisher entrypoint; it does not delete email, Git history, public results, or sealed Journals.

## 9. References

- `docs/01-plan/features/daily-0715-result-publication.plan.md`
- `docs/02-design/features/daily-0715-result-publication.design.md`
- `docs/02-design/features/professional-prediction-briefing.design.md`
- `docs/RESULT_PUBLICATION.md`
- Official OpenAI scheduled-task guidance: connected plugins can be used by scheduled tasks, and local project work requires the desktop/local environment to remain available.
