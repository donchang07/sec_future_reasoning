# live-forward-v2 — Design

Date: 2026-09-09. Contract: real-world-contract-v2.0.0. Pre-prediction design.

## Frozen executable boundary
Add reasoning/live_v2.py only, plus tests. Import the released refinement package and original engines/technical/decision unchanged. Lock normalized UTF-8 source hashes for all reasoning Python, config JSON, ontology/catalog data, dependency lock and new tests, git commit, Python/dependency versions and historical journal byte hashes. Hash the lock and publish it before collection. Verify lock before/after execution and replay. Documents and PDCA metadata may change after the lock; executable files may not.

## Sources and cutoff
Reuse all 11 market SourceSpecs and 8 documentary SourceSpecs without changing provider/parser configuration. Yahoo provides preferred 30m/daily, common daily, KOSPI, FX and DXY; US Treasury XML supplies 10y; Samsung IR PDFs, TrendForce spot and Customs HWPX supply documentary facts. KRX access documentation is an access probe, not a flow observation. The three KRX flow feeds and contract ASP remain unavailable when adapters return unavailable.

Collect documentary data, then market data; cutoff is after the last collection. Persist exact responses before evaluation. Existing parsers exclude incomplete 30m and daily candles, and aggregate only complete weeks/months. No in-progress candle relabeled complete. Unknown release times remain null and collection time is the conservative availability bound. Existing source freshness rules apply before mapping. Retain KOSPI/DXY raw facts as unmapped when the released mapping has no rule.

For existing market factor histories, create typed SourceObservations with actual previous values from the same series and raw response. Keep a prior-reference table with previous timestamp/value. No invented prior for spot, financials or exports. Original documentary converters and v2 mapping/nowcast revision rules apply unchanged.

## Contract adapter, not model retuning
For each horizon, map and assess all source facts using the released mapping and requirement matrix. Use original profile factors/edges/seed; replace only the obsolete global critical gate with the v2 assessment gate in a separate runner. No profile file mutation. E11 projects applicable checks from the already released three-domain evaluator into typed Foundation constraints; retain all non_applicable checks in the assessment.

E01 receives only validated factor histories. Preserve its original level/baseline normalization and quality calculation for direction-capable factors: semantic signal is an eligibility check, not a new scaling or weight. Record both the semantic change signal and original engine normalization. Value-only mapped factors may supply anchors/coverage but normalized=None and no factor_effects; unknown is not zero. No new graph nodes, aliases or edges. New memory/export/financial types remain semantic/module/constraint evidence where the frozen graph has no directional route; report that limitation explicitly.

Run E01–E19 generation 0, calculate the unchanged technical evidence once, run generation 1 with that same batch. E06 feeds Regime/Flow and E10 Reflexivity exactly as existing code. Missing flow gets no artificial flow contribution. E09 continues duplicate-root prevention. E18 is withheld for an ineligible assessment; do not construct a candidate probability in that case. Eligible E18 uses the original numeric method, then publish_candidate applies the released confidence multiplier without changing its probability. Preserve original challenger confidence and its existing numerical algorithm; do not feed the new coverage penalty back into calibration.

Decision calls the original decide function with final published probability/confidence, Wave, Alignment, actual liquidity and E19 status. Position held=false explicitly. Report failed/passed gates and counterfactual sell applicability without changing thresholds.

## Journal and replay
Typed input bundle contains raw market snapshot, raw documents, lock and snapshot hash. Output contains all SourceObservations/prior provenance, source freshness, mapping dispositions and assessments, all 114 engine invocation results and artifacts, before/after forecasts, technical results, actual contribution paths, ledger and decisions. Store contract/mapping/matrix/ontology/engine/graph/policy versions. Each evidence disposition distinguishes mapped value-only, directional but unsupported graph, directional with engine path, and unmapped.

Use exclusive file creation, canonical SHA256 sealing and unique run_id derived from lock and fresh raw bundle. Save P0 from latest eligible completed preferred 30m close (fall back to latest complete daily close only if 30m unavailable), including bar time/frame/raw provenance; never claim it is an executable current quote. Schedule 1d/1w as elapsed calendar durations and 1m/1y as calendar anniversaries. Outcomes append to separate files referencing the sealed journal; first complete close on/after due time, no future outcome supplied now.

Replay validates the current frozen files/dependencies, reparses exact raw bytes, reruns all engines, compares the entire canonical journal hash. Historical journals retain their original recorded-code replay environments. Report generation is deterministic and included in the frozen executable.

## Tests before first forward execution
Retain 170 regressions. Add tests for pin drift, seal immutability, data-mode/cutoff violations, unmapped and value-only input exclusion, unsupported graph evidence, original normalization unchanged, horizon withholding, three-domain E11 projection, one feedback/114 invocations, decision liquidity blocking, probability-ledger reconstruction, raw replay equality, P0 closed-bar selection, calendar yearly outcome and append-only outcome identity. Use synthetic fixtures/offline mocked inputs only; never label test-generated data as a published live prediction.

## Findings policy
No code or configuration changes after the first live output. Any integration defect, implausible probability, missing graph coverage or confidence issue is preserved in the sealed run and next-PDCA findings. Completion requires actual evidence and successful checks, not an attractive prediction.
