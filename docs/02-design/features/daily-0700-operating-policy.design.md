# daily-0700-operating-policy — Design

Policy daily-preopen-v1.0.0; operations forward-ops-v1.1.0. Date 2026-09-10. Approved scope: operational admission only, frozen v2 model unchanged.

## Architecture and time contract
CLI daily → preopen scheduler guard → original raw bundle → deterministic market admission projection → original frozen live_v2.evaluate → sealed journal → unchanged Outcome store. Event command remains its existing separate path. Shadow never reaches either worker.

The daily trigger is 07:00 Asia/Seoul on every calendar day. Automatic catch-up/retries may begin from 07:00 until 08:59; delayed attempts after this window skip. Capture actual completion/prediction timestamp, never label delayed runs as executed at 07:00. Weekend/holiday forecasts can contain stale/withheld horizons. The single explicit exception is date-scoped by --exception-date and --exception-reason, must match the machine's current KST date, and is recorded as an exception. One daily:YYYY-MM-DD key is shared with the previous policy. Recheck under the exclusive lock before collection.

Global knowledge cutoff remains actual collection completion (frozen RawSnapshot contract). Market-effective ceilings are separate:
- Korea: the latest valid preferred daily bar strictly before the forecast's KST date, at 15:30 KST. Record that this is an observed source session, not an independently verified KRX calendar. If absent, fail not_ready. Stale dates remain disclosed by original freshness policy.
- US: latest completed NYSE core cash session, 16:00 America/New_York, or 13:00 official early close. Explicit official 2026–2028 calendar; unsupported years fail closed. ZoneInfo handles DST. This is an admission ceiling, not a claim that FX, Treasury or DXY all share NYSE trading hours.
- Korean OHLCV/KOSPI/flow observations must not exceed the Korean ceiling. US Treasury/FX/DXY must not exceed the US ceiling under their existing provider timestamp semantics. Exact release times remain null where not supplied. Documents keep original semantic/release eligibility at the actual knowledge cutoff. No fabricated earlier collection timestamp.

Raw HTTP bodies remain untouched in raw-bundle.json. admission produces admitted-bundle.json, with only eligible rows, new content hashes and per-source original→derived hash, excluded count, ceiling, latest admitted effective time and reason. No price/value/timestamp edits. JSON indicator arrays remain index-aligned; invalid sources fail unavailable. US Treasury XML rows are filtered by the original date-end effective timestamp. Document raw bodies remain unchanged. Evaluate the admitted bundle once; original feedback still runs exactly once. Journal embeds operating_policy, market_cutoffs, admission audit and original raw bundle hash alongside the original model fields. Model versions/lock and numerical algorithms remain unchanged.

## Compatibility and data safety
The old runtime and worker retain historical behavior. The CLI daily routes to the new module. Replay dispatch is by recorded policy: old operations manifests are validated against their pinned git revision, and the original worker is run from that revision; imported v2 uses its original lock. New policy replay regenerates admission from original raw data and compares the complete sealed journal, not merely probabilities. New operations manifest covers all executing operations code and the scheduler; refusal on version drift is required for new runs/replays.

P0 is the last usable admitted Korean price. outcome_due remains the original model's prediction timestamp plus calendar 1d/1w/1m/1y. Outcome selection still chooses the first observed close at or after due, never edits due or prediction, and preserves original journal SHA links. A prior 16:16 prediction does not acquire a 07:00 maturity retroactively. Cross-policy evaluation remains compatible; policy identifiers enable cohort separation.

## Findings fixed before result inspection
OP-F01: Conservative provider-local daily end timestamps can exclude the newest US date even after the US market has closed. Keep the frozen parser and record older eligible evidence/freshness; a source contract update is a separate PDCA. Treasury's documented approximate 15:30 quotes do not justify silently editing its frozen date-end observation timestamps.

OP-F02: Today's midday exception with prior-close 30m bars can trigger the frozen intraday freshness rule (over two hours old during Korean trading). Do not bypass this rule to obtain reversal output; report unavailable and failed timing gates if triggered.

OP-F03: US equity/SOX/chip/oil factor expansion is not part of a schedule change. Positioning/Event remain shadow-only. Scheduled task still requires machine/network and an interactive logged-in account.

## Tests and release gates
Add tests first: 07:00 and 09:00 boundaries; calendar weekends/US holiday/early close/DST; unsupported calendar; dated exception and no backdating; existing-day idempotency; Korean midday row exclusion; non-US-close daily exclusion; raw unchanged/parallel arrays; missing source; cutoff provenance; inherited partial bars and freshness; legacy version replay and tamper refusal; new raw replay reproducibility; Outcome links/due preservation and cross-policy evaluation; scheduler 07:00 with no 16:10 trigger. Run all 221 prior tests. CI must pass Python 3.11/3.12 before schedule activation. After activation execute today's exception, replay all preserved paths, publish Check and Act evidence. Never tune after inspecting results.

## Calendar references
NYSE regular hours, 2026–2028 holidays and early closes: https://www.nyse.com/trade/hours-calendars

US Treasury quote timing: https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics
