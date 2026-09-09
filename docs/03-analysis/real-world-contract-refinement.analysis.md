# real-world-contract-refinement — Check

2026-09-09. Design: [v2 contract](../02-design/features/real-world-contract-refinement.design.md). Initial implementation `e960261`: 166 tests pass (129 existing + 37 new); both original recorded-version replays match. No live prediction generated.

## Initial review: 8/10 complete, two contract gaps to fix in Act

- RW-01: Same-series observations from different providers collected at different times can be mistaken for revisions of one provider. Conflicting simultaneous economic observations must remain conflicted even when their collection timestamps differ. Add a regression before the fix; distinguish provider revisions from cross-provider conflicts.
- RW-02: Matching financial period-end timestamps alone does not distinguish quarterly from year-to-date flows. Require a financial reporting-period key in semantic observations and factor evidence, group derived ratios by it, and reject cross-period E11 combinations. Existing same-period consolidated statements continue to map; incompatible pairs remain unmapped/non-applicable.

These gaps affect semantic mapping and E11 scope fidelity, so completion is withheld pending their fixes. Requirement matrix (48 factors × 3 horizons), seven memory families, 23-fact classification, Golden cases, original regressions, immutable journals/replay and version manifest are implemented. The manifest is a release candidate until the final version tag is published after Act verification.

## Preservation evidence

- First journal file SHA256: `3589081df5c7dd6c1bb9f83718d8acbe199e5de86dc4db40fdf5b362ab7fbb58`.
- Second journal file SHA256: `c88e2cc2aa6bffbd2360616013f964e207b6d36a1f42af2ecbd9f3473a406d5e`.
- First replay at `7c36073`, second at `1eb1885`: equal.
- Legacy engines, technical analysis, Decision, live adapters and model profile: no diff.

The new library is an opt-in contract assessment boundary. It does not activate v2 in the legacy live CLI or create a new forecast; subsequent live integration must explicitly select the released version and consume its structured states and gates.

## Final Act recheck: 10/10, 100%

Final implementation `816780a`, published contract tag `real-world-contract-v2.0.0` at `b9dc4a5`. RW-01 and RW-02 were reproduced by failing tests before fixes, then all four added boundary regressions passed. Provider revision ordering is now per-provider; financial period keys are mandatory for mapping and ratio derivation/E11 operands cannot mix reporting durations.

| Completion condition | Evidence | Result |
|---|---|---|
| Horizon requirement matrix | Registry + manifest: 48 active factors × 3 horizons, five requirement states | pass |
| Memory taxonomy | Seven families, independent-root aggregation, contradictions and unknowns | pass |
| E11 three domains | Company / Memory Business / Industry Supply; non_applicable explicit | pass |
| Semantic layer | Field/unit/scope/period/horizon/regime/version/cutoff validation, provider conflict guard | pass |
| All 23 facts classified | [Individual audit](real-world-contract-refinement.mapping-audit.md): 19 direct / 4 derived / 0 still unmapped | pass |
| New Golden tests | All 15 requested scenarios plus boundary/release regressions; 41 new tests | pass |
| Existing 129 regressions | 170 total tests pass | pass |
| Two live journals immutable | Original file SHA256 values above still identical | pass |
| Existing prediction replay | Both recorded-version replays equal | pass |
| New contract version | Published immutable tag and verified JSON release manifest | pass |

[Final code CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34319281921) and [tag-target CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34319310462): Python 3.11/3.12 success. Full legacy schema/catalog validate and deterministic fixture replay also passed in CI. The unimplemented full-product Golden release gate remains closed as designed; the 80-case catalog is not represented as fully executable.

No probability weight, prior, calibration, ENTRY/SELL threshold, legacy adapter or old journal was changed. The previous feature remains historically incomplete at 7/9. Completing this contract feature does not claim a new live forecast or retrospectively upgrade its result.
