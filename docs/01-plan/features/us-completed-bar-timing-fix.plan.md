# US completed-bar timing bug fix — Plan

2026-09-10. Scope: daily-preopen-v1.0.0 timing audit and separately versioned correction.

The source parser equates US daily observation time with provider-local 23:59:59. That is inappropriate for completed regular-session equities and the Treasury's approximately 15:30 ET daily yield observation. Correct source timing without changing model, graph, weights, calibration, thresholds, semantic factor meanings or historical predictions.

Audit Nasdaq, SOX, US semiconductor shares, Treasury 10y, DXY, WTI and USD/KRW. Preserve raw captures and distinguish source present now, session completed, exact release unknown, provider finality and availability at 07:00. Today's later collection cannot prove what was available at 07:00.

Deliver Plan → Design → tests → source timing bug-fix implementation → real availability audit (no new prediction) → Check/Act. Publish each phase. Release daily-preopen-v1.0.1 / source-timing-v1.0.1 for subsequent daily runs only after regression and CI. Keep the 07:00 schedule and existing one-journal-per-day key.

Success: instrument-specific completion/availability contracts; explicit unavailable/stale reasons; no incomplete or after-hours substitution; existing Treasury factor gets correct observation time only when the target daily release is actually captured; new Nasdaq/SOX/stock/oil evidence remains diagnostic-only; all 245 tests plus timing tests pass; all existing journal hashes/replays remain valid. Model output inspection/tuning and a second prediction for today are out of scope.

Risks: public vendor bars are revisable, not exchange-certified immutable finals; FX and futures settlements differ from daily OHLCV; date-only Treasury release time must remain unknown. Correctness requires withholding rather than timestamp invention when source semantics are unverified.
