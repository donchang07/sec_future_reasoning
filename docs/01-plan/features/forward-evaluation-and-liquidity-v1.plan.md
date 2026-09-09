# forward-evaluation-and-liquidity-v1 — Plan

Date: 2026-09-09. Baseline: real-world-contract-v2.0.0 and live-forward-v2 executable `73c30f77608813bafcecf137e413e88b3c01d7cf`. Canonical PRD: docs/samsung_preferred_future_reasoning_prd_v1.1.html.

## Goal
Start durable daily/event forward collection, independent realized-outcome evaluation, auditable positioning input and a minimal local monitoring UI. Preserve all three historical live journals, recorded-code replays and 187 regression tests. Do not change the frozen engines, graph, weights, prior, calibration, Wave, Alignment, Liquidity algorithm or Decision thresholds.

## Scope
- Separate operations package with daily close scheduler, idempotency, raw capture, frozen execution, failure logs and replay.
- Typed human_supplied_market_close evidence for KOSPI foreign/institution cash, foreign index futures, stock futures, program, USD futures, common/preferred individual flow. No futures/cash sums, no invented unavailable data.
- Event runs for FOMC/CPI/employment/Samsung earnings with timestamped expectation, surprise, priced-in observations, long-yield response and challenger scenarios.
- Immutable outcome records, horizon accuracy/Brier/reliability/confidence bins, false/missed entry/sell opportunity diagnostics; separate Human Forecast store and comparison.
- Monitoring UI with all horizons, technical/liquidity gates, before/after feedback, contribution inspection, run/source/positioning/event/evaluation status.
- Minimum 20 distinct forward/event runs before any result-driven tuning discussion; no automatic tuning even after the minimum.

## Contract conflict findings — recorded before implementation
- FE-F01: Registry foreign_net_buy/institution_net_buy/program_net_buy means **Samsung preferred** flow, not KOSPI or derivatives. Derivative instrument/expiry/hedge intent is absent from frozen E09/E10. Collect and analyze instrument-specific interactions in an explicitly separate diagnostic sidecar; do not claim these alter E09/E10 or Liquidity. All newly supplied positioning, including exact individual-flow fields, stays in Shadow for this feature. Any model admission requires a separately verified source and contract PDCA.
- FE-F02: Frozen v2 admitted_fixture/run_mapped discards events; FOMC policy rate is not US10y yield. Support event-triggered actual market runs and independent surprise/priced-in/yield/challenger diagnostics. Direct event contributions need a future contract; never alias the rates or rewrite engines.
- FE-F03: Original lock hashes include test/code file inventory. New operations/tests must not invalidate historical replay: use an isolated original-code worktree for frozen execution and old v2 replay.
- FE-F04: Original outcome_due is an exact timestamp; after-close predictions can resolve to a later trading close than the colloquial “next day.” Preserve original due times and disclose actual measurement delay. No retroactive schedule rewrite.
- FE-F05: False/missed ENTRY/SELL requires an explicit outcome label and denominator; define these ex ante as directional opportunity diagnostics, not proof that an untradeable signal should have traded.

## Completion gates
Plan/Design pushed before code; 187 regressions retained; new boundary/evaluation/operations/UI tests; installed daily schedule with run log; one genuine post-close run if source availability permits; replay equal; no future outcomes invented; human inputs remain empty until actually supplied; monitoring visually checked; CI green; findings and operational limitations published. Twenty runs and future outcomes cannot be manufactured during implementation; feature completion denotes operating capability, not mature predictive validation.

## Sources / operation
KRX requires API application/authentication, so no authenticated source is claimed without a working response. Human transcription retains source reference, instrument, unit, session, effective/released/received times and revision lineage. Regular equity session ends 15:30 KST; schedule at 16:10 KST with complete-bar validation and no blind weekday=trading-day assumption.

References: [KRX market hours](https://global.krx.co.kr/contents/GLB/06/0602/0602020204/GLB0602020204T1.jsp), [KRX Open API](https://openapi.krx.co.kr/contents/OPP/MAIN/main/index.cmd), [existing factor scopes](../../02-design/features/sec-future-reasoning-v1-1/factor-registry.md).

## User clarification (before Do)
Baseline improvement is out of scope. Daily Prediction invokes the original v2 path unchanged. ALL new positioning and event input is shadow-only; no probability/confidence/decision influence. Post-outcome descriptive error/Shadow association is supported, without claiming causation. Twenty cases is a minimum research gate, never an automatic admission switch.
