# live-forward-v2 — Plan

Date: 2026-09-09. Status: approved for Design under standing project authorization.

## Goal and scope
Create the first immutable live_forward Samsung preferred prediction using the released real-world-contract-v2.0.0. Preserve both historical journals and the v1 execution path. Use the current PRD and the released contract refinement design as the source of truth.

Implement a separate orchestration adapter, provenance lock, fresh collection, horizon-specific contract assessment, two engine generations separated by exactly one technical feedback, explainability, P0 and append-only outcome references, and deterministic replay. No UI or new factor/graph/model tuning.

## Fixed boundaries
Do not edit the released refinement package, contract manifest, model profile, original engines, technical algorithms, decision policy, graph, weights, prior, calibration or thresholds (ENTRY 80%, SELL 70%). Freeze the new orchestration code and dependencies before collection/prediction. After observing the first output, code/config changes are prohibited; defects become findings for the next PDCA.

## Acceptance
1. Plan and Design published before implementation; frozen executable hashes published before live collection.
2. All existing actual source adapters attempted; partial candles excluded and provenance retained. No fixture mixing or synthetic replacement.
3. Semantic validation precedes engine inputs; mapped value-only facts do not become directional signals. Unsupported graph routes are explicitly disclosed.
4. Independent 1w/1m/1y coverage decisions, E01–E19 invocation traces before/after one feedback, withheld probability where required.
5. Unchanged technical/alignment/liquidity/decision functions; unavailable liquidity cannot pass its gate.
6. Immutable new journal and readable contribution reconstruction, P0, pending 1d/1w/1m/1y outcomes.
7. Raw replay matches, old journals unchanged with recorded-code replays preserved, 170 regression tests plus new integration tests and CI pass.
8. Final report includes required horizon table and separate feedback probabilities. No requirement that a forecast or ENTRY must exist.

## Sequence and risk controls
Plan → Design → offline tests and adapter → CI → immutable lock → one fresh collection and prediction → replay/check → report/Act. Missing providers remain unavailable. The released coverage contract can accept value-only financial evidence; the frozen graph cannot represent every new memory family. Record this limitation rather than changing semantics, graph or model to obtain a desired result. Position is unheld because no actual holding has been supplied; record this explicit policy input.
