# live-forward-v2 — Check

Date: 2026-09-09. Result: 17/17 requested feature requirements verified, with explicitly permitted 1y withholding. This is not a whole-product release or validation of predictive accuracy.

## Evidence
Run `e51235a7-9c47-575b-b152-dab8cee04c17`, cutoff `2026-09-09T06:42:34.193123+00:00`.
Journal seal `40c54c137865fdbb9f24c2750455a2ffa974b16ff2c51059ddc12f2f2f958002`.
Pre-run lock `b811efe383dd2e504b2a30d59ee48468466872b8b71e8a6e8a65f5c662de7c34`, executable commit `73c30f77608813bafcecf137e413e88b3c01d7cf`.

| User requirement | Verified evidence |
|---|---|
| 1. Separate v2 path / preserve v1 | reasoning/live_v2.py added; v1 and two original journals unchanged |
| 2. Pre-execution hash freeze | Lock published at 3ec6a63 before fresh collection; verified again after prediction and replay |
| 3. Fresh completed data | 264 completed 30m, 4,931 daily, 1,042 weekly, 239 monthly bars; incomplete/invalid exclusions recorded |
| 4. All connected sources | All 11 market and 8 documentary specs attempted; seven market feeds fresh, seven documentary content feeds available; KRX access page is documentation only |
| 5. Semantic admission | 389 raw observations retain timestamps; per-horizon MappingBatch and evidence dispositions; value-only normalized=None; unsupported graph routes not aliased |
| 6. Independent horizon matrix | 1w/1m eligible; 1y coverage:memory and memory_family_quorum withheld |
| 7. E01–E19 | 114 invocations: 112 success, two legitimate E18 insufficient_evidence for 1y; 24 non_applicable payloads among successes |
| 8. Wave | Original algorithm ran 30m/daily, daily/weekly, weekly/monthly; full features and context retained |
| 9. Alignment / liquidity | Bull/bear alignment .4/.0 all horizons; buy/sell liquidity null, never estimated |
| 10. One feedback | Exactly generations 0 and 1; same technical batch once per horizon; Regime/Reflexivity applied, Flow effect zero because unavailable |
| 11. Decision | Original decide function; all WAIT, thresholds unchanged; gates recorded |
| 12. Explainability | 11-step ledger per numeric forecast reconstructs prior to final; positive/negative paths, missing confidence and feedback reasons retained |
| 13. Immutable journal | New exclusive sealed file; live_forward and real-world-contract-v2.0.0; no post-result code/config edits |
| 14. P0 / outcomes | 197,500 KRW last completed 30m close at 15:00 KST; separate append-only 1d/1w/1m/1y outcome schedule |
| 15. Replay | Same raw bundle + frozen code/contract/runtime => identical full canonical journal hash |
| 16. Regression / CI | 187 passed before and after live run; CI 34320231170 Python 3.11 and 3.12 passed |
| 17. No fitting to result | Lock still verifies; observations become findings only, no changes to executable files |

Both original live journals replay successfully in their recorded-code worktrees. Their sealed hashes remain `b74c172436e164e3989885d4a031970e66a5ae92ccb7a738ae31ddc3652e03cf` and `ffe85d54f1e805c898bfc31d941b66c680b2950cbe515716c5942be9e2a15cae`.

## Post-result findings (no fixes in this feature)
- LV2-F01: Frozen level/baseline normalization can have a different sign from the latest price change. For example, a daily price decline can still be positive relative to the original baseline. Semantic change only gates directional eligibility. This limitation is visible in dispositions and must be reviewed in a future PDCA, not tuned here.
- LV2-F02: New export momentum has no frozen graph edge; spot has no historical comparator. They supply semantic/coverage evidence, not fabricated contract-ASP contributions. Coverage can be sufficient while directional breadth and Confidence remain low.
- LV2-F03: Raw documentary adapter status strings still say available_unmapped because they describe the preserved v1 adapter. The v2 MappingBatch is authoritative for mapping status. No journal string was rewritten.
- LV2-F04: Source Observation provenance preserves release=null when unavailable; historical market timestamps therefore cannot be used as original historical availability in a backtest. Forward collection is the conservative known-at bound.
- LV2-F05: Outcome due dates are calendar anniversaries, not trading-session counts; future collection must choose the first completed close on/after due time and record that actual timestamp separately.

## PDCA bookkeeping
Preflight gap analysis moved bkit to Check before the Do completion call. Do implementation and its preflight evidence are complete; only task-chain metadata is reconciled. No prediction, model or contract files are changed for this bookkeeping correction.
