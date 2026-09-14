# Daily 07:15 result publication — Design

> Version: 1.0.0 | Date: 2026-09-14 | Status: Approved
> Level: Enterprise | Plan: `docs/01-plan/features/daily-0715-result-publication.plan.md`

## 1. Design boundary

This is an operations-trigger change around the existing `publication` package. The publisher, forecast pipeline, registered-run store, immutable Journal/Outcome contracts, Git allowlist, and the existing 07:00 prediction task remain unchanged.

```text
07:00 Daily prediction (unchanged)
    -> sealed local registered run
07:15 SEC-Frozen-Forward-Publish (changed trigger)
    -> pythonw.exe -m publication (unchanged action)
    -> validate/export public artifacts (unchanged)
    -> scoped Git commit/push when needed (unchanged)
```

The operating PC uses Asia/Seoul local time. Windows Task Scheduler interprets the trigger in local time; no application-level timezone conversion is introduced.

## 2. Scheduler contract

`scripts/install-result-publication.ps1` continues to register the same task name with `-Force`. This atomically replaces the existing task definition instead of creating a second scheduled task.

The installer captures `Get-Date` once and calculates the first future local occurrence of 07:15. It then creates:

```powershell
New-ScheduledTaskTrigger -Daily -At $nextPublication
```

The resulting calendar trigger has a one-day interval and no repetition interval. Selecting the first future occurrence prevents task re-registration after 07:15 from being interpreted as a missed run that should execute immediately.

Unchanged settings are:

- action: project `.venv\Scripts\pythonw.exe -m publication`;
- working directory: project root;
- principal: current interactive user, limited run level;
- `StartWhenAvailable`: enabled;
- multiple instances: `IgnoreNew`;
- execution time limit: four minutes;
- task visibility: hidden.

`StartWhenAvailable` applies after a scheduled 07:15 occurrence is genuinely missed. Because the principal is interactive, the PC and user session still need to be available.

## 3. Timing and failure semantics

- A Daily prediction completed between 07:00 and 07:15 is eligible for same-day publication.
- A run completed after 07:15 waits until the next scheduled day unless an operator invokes `.venv/Scripts/python.exe -m publication` manually.
- A validation, repository-state, or network failure is recorded locally and retried at the next daily execution, not every five minutes.
- Re-registration does not invoke the publisher and therefore creates no forecast or publication commit.

This schedule intentionally trades near-real-time Event publication and rapid Git retry for one predictable Git reconciliation per day.

## 4. Files and compatibility

| File | Change |
|---|---|
| `scripts/install-result-publication.ps1` | Replace five-minute repeating trigger and description with daily 07:15 scheduling. |
| `tests/test_publication_schedule.py` | Add a portable source-contract regression test for the PowerShell task definition. |
| `docs/RESULT_PUBLICATION.md` | Describe daily timing, manual publication, and next-day retry behavior. |
| `AGENTS.md` | Replace the permanent five-minute reconciliation rule with daily 07:15. |
| PDCA Plan/Design/Check/Report and status | Record design, evidence, and completion. |

No schema, API, data migration, package version, or publisher code change is required.

## 5. Security and Git safety

The schedule change grants no new permissions. `publication.publisher` continues to reject private fields and credential patterns, export only allowlisted public artifacts, require `main`, fetch `origin/main`, reject unrelated staged/unpushed/divergent work, commit only managed paths, and never force-push. Local raw captures and operational logs remain ignored.

Task registration is an operating-system mutation and is performed only after source and test verification. Verification reads the installed task's action, start boundary, daily interval, repetition interval, safety settings, last result, and next run.

## 6. Test and rollout plan

1. Add a failing test that requires a daily trigger, 07:15 calculation, and absence of five-minute repetition while preserving action and safety settings.
2. Change the installer and update current operating documentation and permanent instructions.
3. Run the new test, all publication tests, and the full test suite.
4. Record hashes of existing published Journals before task registration and confirm they are unchanged afterward.
5. Re-run the installer to replace `SEC-Frozen-Forward-Publish`.
6. Inspect the live task: one daily trigger, start time 07:15 local, no repetition, correct action, `Ready`, and next run at 07:15.
7. Run design-to-implementation gap analysis. A six-of-six requirement match is 100% and clears the 90% report threshold.

## 7. Rollback

Rollback is limited to task configuration and the installer commit. If the new task definition is invalid, do not run prediction or modify publication artifacts; restore a reviewed scheduler definition and re-register the same task name. Existing published results and sealed local Journals require no rollback.
