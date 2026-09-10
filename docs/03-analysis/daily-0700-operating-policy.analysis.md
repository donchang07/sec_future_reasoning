# daily-0700-operating-policy — Check

2026-09-10. Implementation commit `6479777b64324bdbfad843dd6cd60a6fa4ae0e58`.

## Acceptance: 10/10 operational requirements verified

| Requirement | Evidence |
|---|---|
| Replace 16:10 with 07:00 KST | Old task disabled before implementation; sole daily trigger replaced after CI; next run 2026-09-11 07:00 KST |
| Frozen baseline unchanged | All 221 prior tests pass; original lock validates; new/old VersionBundle exactly equal |
| Separate market cutoffs | Korea 2026-09-09 15:30 KST; US 2026-09-09 16:00 EDT (=09-10 05:00 KST); knowledge cutoff actual 12:15:33 KST |
| Original raw retained and deterministic admission | Separate original/admitted bundle hashes, source hashes, 16 post-ceiling rows excluded; no value/timestamp substitution |
| One official daily case | Repeated dated exception returns the same run_id; exactly one daily:2026-09-10 record |
| Today's current-time exception | Run 2ce0e81e-6569-53de-8b7a-fc7ecd854d7a, actual timestamp 2026-09-10 12:15:33.112563 KST, explicit dated reason; not backdated |
| Preserve Outcome links and maturity | New and old due-time/immutable-link tests pass; old journal bytes unchanged; 12 outcomes pending, none fabricated |
| Preserve replay | Both historical v1 runs, original v2, prior Daily and new exception reproduce their original journal hashes |
| Tests and CI before activation | 245 tests: prior 221 + new 24; Python 3.11 and 3.12 CI successful at 03:15:15 UTC, activation and collection afterward |
| Explainability and no tuning | All four published initial/final ledgers reconstruct; 114 engine invocations; 112 success / 2 expected insufficient E18; operations manifest unchanged after output |

[CI 34432581517](https://github.com/donchang07/sec_future_reasoning/actions/runs/34432581517) also passed schema/catalog validation, fixture generation/replay and the deliberately closed unresolved product Golden release gate.

New tests cover time-window boundaries, date-scoped exceptions, US holidays/early closes/DST/calendar expiry, Korean midday exclusion, US conservative timestamp preservation, raw immutability/index alignment, collection cutoff, unavailable sources, Treasury filtering, historical version tampering, shadow worker rejection, duplicate daily cases, full admission/reasoning replay and Outcome compatibility.

## Remaining findings, preserved before result inspection

- **OP-F01:** Frozen US/FX daily timestamp semantics exclude the latest US source date under the cash-close ceiling. Today's Treasury/DXY and USD/KRW use the eligible September 8 provider date; this is not full September 9 US session coverage. No SOX/US-stock/oil directional factors were introduced. A separate source-contract PDCA is needed for better overnight coverage.
- **OP-F02:** Today's prior-close 30m input is stale under the original midday freshness rule. Its Wave and alignment are unavailable. Daily/weekly/monthly context remains available. No zero score is interpreted as a measured reversal probability.
- **OP-F03:** Task requires the local machine/network and logged-in user. 07:00 is the trigger, not a fabricated exact completion timestamp. Automatic attempts finishing after 09:00 do not publish. Calendar is explicitly supported through 2028; later years fail closed.
- Liquidity remains unavailable; 1y probability remains withheld for Memory coverage. These are frozen-model evidence limitations, not repaired by a schedule change.

Operational acceptance does not establish predictive accuracy or complete overnight market coverage. No model/configuration changes were made after today's result was inspected.
