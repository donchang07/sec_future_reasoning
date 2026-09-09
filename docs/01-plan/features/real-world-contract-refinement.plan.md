# real-world-contract-refinement — Plan

2026-09-09 · contract-only PDCA feature · PRD v1.1.

## Problem and objective

The previous feature collected real financial, spot and export facts but the fixture-era global critical flag and single-product accounting contract could not represent them. Publish a versioned, executable real-world evidence contract without rewriting either historical live decision or changing forecast weights, prior, calibration or Decision Policy.

## Scope

1. Five requirement levels for every factor, separately for 1w/1m/1y; module coverage gates and confidence penalties with recorded economic rationale.
2. Seven distinct memory evidence families; independent-family aggregation with explicit contradictions and no spot/contract/HBM/export substitution.
3. Customs monthly vintage selection (v1/v2/v3/final), YoY, working-day adjustment and comparable-period acceleration.
4. E11 v2 company / memory-business / industry-supply constraints; independently reported facts and non-applicability tracked separately.
5. Typed source observation → versioned semantic mapping → factor evidence → module state. Unit, scope, time, regime, source and mapping-version validation fail closed.
6. Individually classify all 23 preserved facts; apply new mappings only in a separate contract audit, never inside the old journals.
7. Test-first implementation, all 129 existing regressions, both immutable journal checks and recorded-version replay, version manifest and report.

No live collection or new prediction in this feature. No UI/database expansion, fitted coefficients, threshold changes, backtest-based parameter tuning or rewriting the previous feature's 7/9 history. This feature publishes contract assessment and a probability eligibility/confidence boundary for subsequent integration; it does not reinterpret the old E18 outputs as new predictions.

## Acceptance gates

Ten gates correspond to the user's completion criteria: requirement matrix; memory taxonomy; three E11 domains; executable semantic layer; 23-fact disposition ledger; at least 15 new named Golden cases; 129 unchanged regressions; two live journals immutable; both recorded prediction replays; new contract version published. All ten must pass before completion.

## Implementation sequence

Plan → Design with fixed matrix, formulas and test assertions → write failing Golden tests → isolated versioned contract modules → offline Check/Act → report and contract manifest. Publish each completed document and phase status to origin. Preserve `.codex/config.toml` as unrelated local work.

## Risks and controls

Coverage thresholds are ex-ante research policy, not statistically calibrated certainty. Do not infer them from the current price or the two WAIT results. Require nontechnical macro evidence even for 1w; require multiple independent memory families and financial coverage for 1y. More source rows must not manufacture more independent coverage. Unknown does not become a zero signal. Candidate direction probabilities are unchanged by missingness-only penalties; withholding returns null. Confidence remains distinct from direction and Decision gates.

References: [PRD](../../samsung_future_reasoning_prd_v1.1.html), [previous Act](../../04-report/real-data-minimum-slice.act2.md), [previous evidence](../../03-analysis/real-data-minimum-slice.act2-evidence.json).
