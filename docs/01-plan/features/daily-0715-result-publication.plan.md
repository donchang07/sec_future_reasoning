# Daily 07:15 result publication — Plan

> Version: 1.0.0 | Date: 2026-09-14 | Status: Approved
> Level: Enterprise

## 1. Purpose and background

Change the independent public-result publisher from five-minute polling to one execution per day at 07:15 local time (Asia/Seoul on the operating PC). The change removes repeated Git process launches while retaining immutable publication, safe retry, and separation from prediction execution.

The existing Daily prediction task remains at 07:00. A normally completed Daily result can therefore be reconciled about 15 minutes later on the same day. A prediction that finishes after 07:15, and an Event result created after that day's publication, normally wait until 07:15 the following day unless publication is run manually.

## 2. Scope

### In scope

- Replace the `SEC-Frozen-Forward-Publish` five-minute repetition trigger with a daily 07:15 trigger.
- Preserve `StartWhenAvailable`, interactive limited-user execution, hidden execution, overlap prevention, and the four-minute execution limit.
- Update the installer, permanent project rule, operating guide, and automated schedule-contract test.
- Re-register the existing Windows task and verify its action, daily trigger, next run, and last result.
- Preserve publisher behavior: verify and export registered public Journals and Outcomes, then safely commit/push only `docs/predictions/` changes.

### Out of scope

- Prediction timing, model logic, reasoning engines, weights, thresholds, data collection, and Journal contents.
- Changes to publication eligibility, Git transaction safety, immutable artifacts, or public/private data boundaries.
- Automatic reruns within the same day after a network, repository-state, or validation failure.

## 3. Requirements

- `S715-F01`: The installed task has exactly one calendar trigger with a one-day interval and start boundary at 07:15 local time; it has no five-minute repetition interval.
- `S715-F02`: The task action remains project `.venv\Scripts\pythonw.exe -m publication` with the repository as working directory.
- `S715-F03`: A missed 07:15 run starts when the logged-in operating environment next becomes available because `StartWhenAvailable` remains enabled.
- `S715-F04`: Reinstalling the task is idempotent and replaces the old trigger without creating a second task.
- `S715-F05`: No prediction is run by the publisher, and no sealed Journal or existing operations manifest is changed.
- `S715-F06`: Documentation states the once-daily retry latency and the interaction with the existing 07:00 Daily prediction.

## 4. Success criteria

- A source-level test rejects the old repetition schedule and confirms `-Daily -At 07:15` plus preserved safety settings.
- Publication tests and the full regression suite pass.
- The live Windows task reports the expected action and a next run at 07:15, with no repetition interval.
- No new prediction, publication commit, or modification to existing sealed result bytes is caused by task registration.
- Plan, Design, Check, Report, operating documentation, and PDCA status are published without staging `.codex/config.toml` or other unrelated work.

## 5. Risks and mitigations

| Risk | Effect | Mitigation |
|---|---|---|
| Publisher failure at 07:15 | Retry can be delayed until the next day | Retain manual `python -m publication`, durable logs, and `StartWhenAvailable`; document the daily retry policy. |
| 07:00 Daily prediction finishes after 07:15 | Same-day automatic publication is missed | Preserve manual publication and state the next-day fallback explicitly. |
| Installer leaves the old repetition trigger | Repeated Git windows continue | Re-register the same task name with `-Force`, inspect the live trigger, and test absence of `RepetitionInterval`. |
| Unrelated local changes are committed | User work is contaminated | Stage and commit only named project files; leave `.codex/config.toml` untouched. |

## 6. Delivery order

1. Publish this Plan and PDCA status.
2. Create and publish Design before implementation.
3. Add the schedule test, update installer and operating documentation, and run verification.
4. Re-register and inspect the live task.
5. Run gap analysis, publish Check and Report, and close PDCA status.

## 7. References

- `docs/samsung_future_reasoning_prd_v1.1.html`
- `docs/01-plan/features/prediction-result-publication.plan.md`
- `docs/02-design/features/prediction-result-publication.design.md`
- `docs/RESULT_PUBLICATION.md`
