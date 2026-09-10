# US completed-bar timing fix — Design

2026-09-10. Versions: `source-timing-v1.0.1`, `daily-preopen-v1.0.1`, `forward-ops-v1.1.1`. Model contract remains real-world-contract-v2.0.0.

## Root cause and contract
Separate economic effective time, session completion, release time, collection time and prediction knowledge cutoff. A completed bar can still be revisable; no vendor final flag is invented. `available_completed_regular_session` means exchange session ended + existing 20-minute vendor buffer + target-date OHLCV present + provider regular-session metadata agrees. It does not mean exchange-certified final. For strict immutable-final consumers, provider_final remains unknown.

| Evidence | Economic / completion basis | Admission |
|---|---|---|
| Nasdaq, SOX, NVDA, AMD, MU, AVGO, TSM | Regular cash session 16:00 ET, official 13:00 early closes, ZoneInfo DST; daily timestamps and metadata must match that session | Completed target-date regular bar, finite valid OHLCV; no extended-hours last price; diagnostic-only |
| US Treasury 10y par yield | Official NEW_DATE, approximately 15:30 ET observation; date precision, publication time unknown | XML row actually collected by knowledge cutoff; target cash-session date must be present; effective estimate must not exceed US ceiling; no delayed-release fallback presented as current |
| Yahoo DXY cash index | Vendor daily period differs from 16:00 cash close; not ICE DX futures settlement | unavailable for prior-US-close contract until the exact daily-close semantics or a timestamped cash-close observation is verified |
| Yahoo WTI CL=F | Continuous futures OHLCV is not an official dated-contract settlement | unavailable; do not use intraday daily bar or relabel it as CME settlement |
| USD/KRW | Provider London daily window, not US equity session | unavailable for requested cash-close timing; no stale prior-date substitution into current baseline |

For unavailable sources report target session, source latest date, source availability, completion reason, staleness reason, collected_at, released_at=null where unknown, provider_final=null, revisable, authority, and raw hash. Collection after 07:00 produces `availability_at_0700=unknown_not_captured_by_0700`, even when the target row exists now. Actual future 07:00 captures can establish availability at that knowledge cutoff.

## Implementation boundaries
Add operations-only timing adapter. Preserve reasoning/, config/, prior admission.py and worker.py bytes. Treasury Observation gets an approximately 15:30 effective time with date precision and original raw provenance. No weight/value/unit/directional transform changes. Replace only data-preparation assembly for new policy: original Korean preparation and semantic mapping → original run_mapped. All E01–E19/technical/decision functions and lock remain unchanged. DXY/FX availability is explicit, not silently classified fresh because an older date is under a four-day SLA.

Collect US market diagnostics separately before the market knowledge cutoff; persist a separate immutable capture/audit and attach its diagnostic results with model_influence=false. They must not enter InputBundle, semantic mapping or the factor profile. Treasury already exists in the frozen factor registry; it alone receives the corrected timing. Other original sources, missing flow handling and one-feedback rule are unchanged.

New journals record timing version and evidence audit. No new Prediction is issued in this task and no old journal is recomputed under the patch. Existing 07:00 task uses the versioned new path after CI. Existing 1.1.0 replay dispatch loads operations files from pinned commit 6479777 and validates its recorded manifest; original 1.0.0 replay remains pinned to f13d6c1. Replay regenerated diagnostics use saved raw captures, never the network.

## Tests before implementation
Treasury prior-session row available at 07:00; release captured late cannot enter earlier cutoff; missing target date; future date; duplicate/conflicting rows; cash session early close excludes later Treasury observation; DST; equity session metadata agreement; missing/invalid OHLCV; stale session; current/incomplete bar; post-market last price ignored; unverified DXY/FX/WTI withheld; later capture cannot certify historical 07:00; diagnostics do not enter model; all frozen files unchanged; legacy 1.1.0 raw replay preserved. Run original 245 plus added tests and CI. Capture current raw evidence without issuing a prediction, hash/replay the audit, publish findings.

## Primary references
- Nasdaq regular and extended hours / 2026 calendar: https://www.nasdaq.com/market-activity/stock-market-holiday-schedule
- Treasury methodology and approximate quote time: https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics
- ICE DX futures specifications (not Yahoo DXY cash-index definition): https://www.ice.com/api/productguide/spec/194/pdf
- CME settlement definition (not continuous-futures daily OHLCV): https://www.cmegroup.com/market-data/daily-settlements.html
