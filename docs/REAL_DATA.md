# Real data minimum slice

## Capture, inspect, replay

```powershell
python -m pip install -r requirements.lock
python -m pytest -q
python -m reasoning.live collect --output artifacts/local/live
python -m reasoning.live verify --journal artifacts/local/live/SNAPSHOT_ID/prediction-journal.json
python -m reasoning.live replay --journal artifacts/local/live/SNAPSHOT_ID/prediction-journal.json
```

Replace SNAPSHOT_ID with the directory printed by collect. Windows can use `.\.venv\Scripts\python.exe`. `collect` is a new current-time live_forward capture, never an as-of backtest. `replay` uses the journal's embedded immutable raw responses, original cutoff and pinned profile without HTTP or a new prediction timestamp. Same code/version/raw snapshot yields the same result. Changed code/model versions cause replay mismatch rather than rewriting the old forecast.

Each capture directory contains raw-snapshot.json, prediction-journal.json, explainability.md and outcome-schedule.json. All are created exclusively. The Journal contains source manifests, raw response hashes, collection time, unknown released-at, effective time, freshness, per-observation data_mode, missing/conflicting factors, all 114 engine execution records, primary/context technical results and three Horizon decisions. The full market data remains local because vendor redistribution permission has not been established. GitHub receives code, documentation, non-price summaries and hashes.

The 6 instrument/series feeds are preferred, common, Treasury US10Y, USD/KRW, KOSPI and DXY; these are **2 providers, not 6 independent providers**. Preferred has separate 30m and daily requests. Treasury is official XML. Yahoo is an isolated public JSON fallback without a promised stable API/SLA. No HTML scraping is used. Missing DRAM and investor/program flows remain unavailable. KOSPI and DXY are captured context; adding new causal graph edges is deferred. Four source factors and three OHLCV-derived factors can enter the frozen model.

Current frozen profile still makes DRAM critical. Therefore the first run may correctly return null/insufficient_evidence for all final forecasts. Its prior is never reported as a final probability. E11 receives no invented accounting values: an availability boundary reports non-applicable identities, not passed constraints. The independent decision gates block action. Numerical Horizon forecasts and all-19-applicable reasoning cannot be claimed complete until the required real evidence is available.

The existing engines.py, technical.py and decision.py bytes are pinned in config/live-model-profile.json and tested. The profile contains model settings only, no observations, OHLCV, events, historical cases or accounting values from the synthetic fixture. Fixture observations and new fixture journals carry synthetic_fixture by default; real observations require collection/effective timestamps and source references. Legacy 1.0 fixture Journal hashes can still be verified without changing their files.

Reversal values remain **uncalibrated scores** from the original algorithm, not validated Bottom/Top reversal probabilities. The report displays this limitation explicitly. It shows positive/negative paths up to five each, E09 interaction effects, E12 horizon effects, E13 history, E19 blocking checks and decision gates. A probability ledger is printed only when E18 actually produces one.

## Outcome structure

The schedule creates pending +1 calendar day, +7 calendar days and +1 calendar month references to the original run/hash. Actual future outcomes are separate exclusive-create files using `reasoning.live.attach_outcome`. The caller supplies a real source ref, observed_at, collected_at and price; observations before due_at or after collection time are rejected. This function does not fetch a price or certify caller-supplied evidence. An automatic verified price adapter/linker remains follow-up work. The original Journal is never changed.

## Tests and scope

The original 89 tests remain. New tests cover unavailable/stale/conflicting sources, revision/cutoff/unknown release, Korean timezone, partial daily/30m/week bars, mode mixing, immutable storage, source XML parsing, frozen engine hashes, offline complete snapshot replay and early Outcome rejection. New unit-test responses are synthetic_fixture and never published as live observations.

Plan and Design: [Plan](01-plan/features/real-data-minimum-slice.plan.md), [Design/source matrix](02-design/features/real-data-minimum-slice.design.md). Full-product release stays closed. UI, Supabase, Neo4j and all-49 source integration are outside this feature.
