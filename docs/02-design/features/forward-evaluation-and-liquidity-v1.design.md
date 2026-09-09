# forward-evaluation-and-liquidity-v1 — Design

Date: 2026-09-09. Operations/evaluation version: forward-ops-v1.0.0. Model remains real-world-contract-v2.0.0.

## Isolation and execution
Add forward_ops/ and tests only; no edits to reasoning/, frozen config, ontology, requirements or model policies. Create a detached baseline worktree at 73c30f7, verify every original pre-run lock file/runtime and historical journal hash. All actual prediction execution runs in a separate Python process loading reasoning exclusively from that worktree. Operations code has its own SHA256 manifest captured before collecting a run. Preserve the three existing live journals and their recorded-code replays.

Each run has an immutable request, exact original raw bundle, optional positioning input snapshots, original-shaped system forecast and an outer sealed operations record with baseline/operations hash, trigger, session/event identity and provenance. Replay reparses raw data and requests, executes the same frozen functions and compares the complete output. No forecast or outcome file is overwritten. Unique daily key=KST date; event key=official event_id. Exclusive process lock prevents duplicate collection. Failed attempts keep logs/raw artifacts; an already sealed run is never recomputed by a retry.

Daily schedule: weekdays 16:10 Asia/Seoul, Windows per-user Task Scheduler, pythonw/background, stdout/errors to durable logs, StartWhenAvailable. Data is authoritative for a trading session: require an eligible preferred daily bar for today's KST date. Weekends or absent current close generate an explicit skipped/not-ready status, not yesterday relabeled today. The task runs only when this user is logged in; a powered-off computer cannot collect. A manual daily command provides recovery and never backdates collection. Event runs have no daily-close restriction and use only completed available bars. Attempt outcome collection after a successful run.

## Positioning schema and admission
HumanMarketClose: provenance literal human_supplied_market_close, source reference, submitter label, server received_at; rows include trade_date, observed/effective/released times, Asia/Seoul, regular_close, venue, instrument, investor, measure, unit, signed value, optional expiry, revision_of. Every source is an assertion, never official API authority. Retain same-economic-key revisions; equal latest conflicting values are excluded, not summed. Futures require contract expiry and contracts units for net trading/position. Net trading is not an open-position change. USD futures direction is currency positioning, not automatically equity bullish/bearish.

| Evidence | Supported input | Frozen probability admission |
|---|---|---|
| KOSPI cash foreign / institution | KRW million net purchases, separate actor | Diagnostic only: scope differs from preferred |
| Foreign index futures / stock futures | contracts, instrument and expiry | Diagnostic only: no frozen graph node |
| Program market-wide | KRW million, scope explicitly KOSPI | Diagnostic only |
| USD futures | contracts, expiry, actor | Diagnostic only; no equity sign assumption |
| 005930 common individual flow | KRW million, actor | Diagnostic only |
| 005935 preferred foreign/institution | KRW million net purchases | Exact existing foreign_net_buy / institution_net_buy |
| 005935 program | KRW million, program actor | Exact existing program_net_buy |
| Semiconductor relative flow | sector net-buy/turnover minus market net-buy/turnover; all four operands | Existing semiconductor_relative_flow, computed with positive denominators |

Exact-compatible observations are converted to Foundation Observation plus existing Semantic Mapping before frozen run_mapped. No factor alias for broad market or derivatives. Include actual prior rows only when available; no invented comparator. Liquidity still requires all four original flow inputs plus original timing rule. Missing any stays null. The same dated session is required for all admitted close evidence to prevent cross-day splicing.

FE-F01 remains a contract conflict: separate interaction/actor diagnostics group same actor/date, show cash/futures concurrence or opposing positioning and possible hedging uncertainty, without adding amounts or assigning forecast weights. Horizon validity short/medium for daily net-trading, long requires longitudinal holdings not supplied. These are NOT replacements for the actual E09/E10 artifacts, which remain inspectable in the system journal.

## Event schema and conflict
Event types FOMC, CPI, employment, Samsung earnings. Explicit field/unit/actual, official released_at/source; consensus values and source captured before release; pre-event price move and expected move with pre-event timestamps; optional US10y before/after with timestamps. Validate chronology and units; missing expectation yields unknown surprise. Diagnostic surprise=(actual-mean)/population std only with at least two distinct estimates. Priced-in fraction can use only a supplied directional expected price move whose sign agrees with observed pre-move; do not infer equity direction from event type. Yield reaction is a separate observed delta. Challenger scenarios include expectation already priced, discount-rate response versus earnings/demand, and false-bottom/liquidity rejection.

FE-F02 remains: these diagnostics do not modify AI probability because frozen v2 discards event objects. Event runs execute the full frozen market path and report this limitation. FOMC selloff alone never creates ENTRY: unchanged decision requires all gates. Do not produce a fake event run without an actual supplied event.

## Outcome and metrics contract (ex ante)
Import the existing v2 run into the evaluation registry by reference/copy with its original seal. Exclude the two v1 no-forecast historical records from v2 forward sample count, but preserve them. New outcomes reference run_id and journal SHA; data_mode=live_forward; due_at from sealed original outcome_due. Select first completed preferred daily close >= due_at from newly collected raw data, preserving raw source/hash and effective/released/collected timestamps. Future/early outcomes rejected; no current quote substituted. Delayed data availability is disclosed, per FE-F04. Revisions are separate records, never edit a prediction; first observed outcome is the primary evaluation vintage.

Evaluate each 1w/1m/1y forecast only with matching-horizon outcome. 1d outcomes are ancillary return diagnostics, never reused to score 1w. Realized label uses the unchanged simulation flat band 0.01*sqrt(days/7), days={7,30,365}; strictly above/below is up/down, boundaries flat. Directional accuracy uses unique argmax (ties counted separately). Multiclass Brier=sum((p-y)^2), range 0..2. Probability reliability: per-class fixed ten bins with count, mean probability, observed frequency; report ECE. Confidence calibration: ten fixed bins against unique-argmax correctness, count and accuracy; never imply confidence is itself calibrated.

False ENTRY=ENTRY with outcome not up; missed ENTRY=unheld WAIT with outcome up. False SELL=SELL with outcome not down; missed SELL=held HOLD with outcome down. Report counts and eligible opportunity denominators. These are directional opportunity diagnostics without costs, path-dependent stops or tradability claims. Withheld horizons are excluded, not zeros. Report system and human scores separately; never combine them.

HumanForecast references a known run/horizon with probabilities/confidence and rationale, server timestamp and optional revision_of; never enters prediction request or model worker. Primary comparable human forecast must be submitted before due_at; later records are labeled late and excluded from prospective comparison. Human may have seen the AI: record blinded=false, no claim of blinded evaluation. Run uniqueness for the 20-sample guard is session or actual event identity; meaningful event requires actual/expectation and at least one system forecast. Twenty is a review minimum, not automatic permission or statistical sufficiency. No tuning endpoint.

## Minimal monitoring UI
Localhost-only HTTP service and static HTML/CSS/JS, no new dependencies. One screen shows three horizon rows, all requested probabilities/confidence/reversal/alignment/liquidity/decision and held status. Select run and horizon; drill into gates, before/after feedback, causal roots/edges and ledger, E09/E10 artifacts, coverage, source freshness, positioning/event diagnostics. Evaluation panel shows counts and empty/pending states, Brier/reliability/confidence and false/missed actions, separate human forecasts and 20-run progress. CLI JSON import is the structured input interface; UI explains current missing inputs. Escape text and use DOM textContent, never render source HTML. Read-only API and no public hosting.

## Tests / Check
Add tests first for typed units/scopes/expiry, revision conflict, cutoff and human chronology, compatible-only admission, no derivatives sum, event surprise/pricing with no hard-coded FOMC direction, closed-session/idempotency, outcome earliest-close identity and immutability, Brier/reliability/confidence/ties/withholding, false/missed denominators, human isolation/late exclusion, minimum-run deduplication, frozen drift and replay, API traversal/XSS safety. Retain 187 regressions, run CI, visually inspect desktop UI and drill-down. Complete Check after implementation; Act records remaining FE-F01/F02/F04 limitations without tuning.
