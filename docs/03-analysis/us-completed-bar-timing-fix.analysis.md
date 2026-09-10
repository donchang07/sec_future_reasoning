# US completed-bar timing bug fix — Check

2026-09-10. Code `64ff66ba355919eea49b95bbb1c59327f4018fe8`. Source timing `source-timing-v1.0.1`; daily policy `daily-preopen-v1.0.1`.

## Acceptance: 9/9

| Requirement | Verification |
|---|---|
| Diagnose actual timing bug | Treasury's date-end timestamp wrongly falls beyond cash close; official approximately 15:30 ET observation is earlier |
| Instrument-specific completion | Treasury daily observation separate from Nasdaq/SOX/equity regular session; DXY/FX/continuous oil not relabelled |
| Availability and missing reasons | Exact target session, source date, collected/released times, provider final flag, raw hash, explicit stale/unverified reasons |
| No look-ahead | Late capture cannot certify 07:00; future source rows/current bars excluded; target missing does not silently fall back |
| Model unchanged | reasoning/, config/, fixtures/ and requirements.lock unchanged; frozen file-hash regression passes |
| Diagnostic separation | New stock/index/oil diagnostics never enter InputBundle/factor mapping; only existing Treasury factor receives timing correction |
| Historical immutability | All five existing prediction replays reproduce their original hashes, including v1.0.0 preopen run through pinned operations commit |
| Regression/CI | 266 tests = 245 previous + 21 timing tests; Python 3.11/3.12 CI passed before installation |
| Auditable real capture | Current 11-source availability capture sealed and replayed; no Prediction Journal created |

[CI 34433429184](https://github.com/donchang07/sec_future_reasoning/actions/runs/34433429184) passed tests, schema/catalog validation, fixture generation/replay and the deliberately closed unimplemented product release gate.

Actual audit: `41437225-f7bf-425e-8b8f-485592d496a3`, knowledge cutoff 2026-09-10 12:26:25.937891 KST. Audit hash `b8ca2b4f77a74657098e50d8f970498002b46b7ef956407706785602e2c878b3`. Seven equity/index regular-session series plus official Treasury target-date row are available at this capture. Three remaining series are unavailable for the requested close contract, with unverified source semantics. All eleven retain `availability_at_0700=unknown_not_captured_by_0700`.

## Findings
- **UT-F01:** A later raw capture cannot prove earlier 07:00 availability. The next scheduled collection will preserve actual availability at its own knowledge cutoff. No historical 07:00 run was fabricated.
- **UT-F02:** Yahoo regular-session completion is calendar/provider-metadata validation, not an exchange-certified immutable final flag. Provider revisions remain possible and captured bytes remain immutable.
- **UT-F03:** DXY cash index is not ICE DX futures settlement, CL=F daily close is not a verified dated-contract settlement, and London FX daily bars are not US cash-session bars. Keep unavailable until a separate verified Source contract exists.
- **UT-F04:** The equity calendar is an upper-bound cash-session reference. If Treasury has no row for that date (including different market holidays), the explicit target-date-unavailable/source-holiday reason applies; do not fabricate a Treasury observation.

The data-timing repair is complete. Proof that every requested source is available at tomorrow's actual run remains forward observation, not a claim made by this audit.
