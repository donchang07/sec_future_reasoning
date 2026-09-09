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
