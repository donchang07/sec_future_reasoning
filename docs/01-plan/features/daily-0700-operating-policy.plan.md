# daily-0700-operating-policy — Plan

Date: 2026-09-10. Operating policy: daily-preopen-v1.0.0.

## Purpose and scope
Replace the 16:10 KST scheduled baseline with one official 07:00 KST forecast per calendar day. The forecast uses prior Korean market close prices/flows and observations no later than the previous US cash-market close. Preserve frozen real-world-contract-v2.0.0, all model artifacts, historical journals and evaluation semantics. Today alone, permit an explicitly dated exception at the actual execution time; never backdate it.

## Requirements and success criteria
1. Disable the old task now; activate the replacement only after local regression and GitHub CI pass.
2. Version and hash the operational admission policy before collection. Keep raw responses untouched, with separate admitted input and an exclusion audit.
3. Record actual prediction/collection times, nominal schedule, exception reason, Korean observed prior close, US prior session close and source-specific last accepted time.
4. Exclude today's Korean intraday/daily bars even for today's midday exception. Keep incomplete weekly/monthly periods excluded through the frozen parser.
5. Keep one official daily case key across operating policy versions, with an exclusive active-run lock and retry idempotency.
6. Preserve old Prediction and Outcome records, old model replay, P0 linkage, due timestamps and horizon evaluation. Add regression tests before implementation.
7. Execute, seal and replay today's authorized exception after validation. Publish PDCA artifacts and a human-readable result.

## Boundaries and findings
No new directional factor, weight, threshold or calibration changes. US equities/SOX/chip stocks/oil are not all connected to the frozen model; scheduling does not imply new factor coverage. Shadow evidence remains separate.

The existing non-Korean daily parser assigns conservative provider-local end-of-day timestamps. Some latest US/FX observations cannot be admitted before a cash-market-close ceiling under that contract. Retain older eligible observations and disclose freshness; do not silently relabel their time. A later source-contract change can resolve this limitation.

## Delivery sequence
Plan → Design → tests and operations implementation → regression/replay/CI → enable 07:00 schedule → today's exception and replay → Check/Act report. Documents are committed and pushed at completion. No routine permission prompts.

## Risks
The Windows task needs this machine and its interactive user session available. Late automatic starts must skip outside the pre-open retry window. Market holidays and daylight saving require explicit calendar treatment. Historical outcome maturity remains anchored to each original prediction timestamp, not the new schedule.
