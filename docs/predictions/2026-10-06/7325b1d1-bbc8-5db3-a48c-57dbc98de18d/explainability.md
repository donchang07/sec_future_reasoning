# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 7325b1d1-bbc8-5db3-a48c-57dbc98de18d
Cutoff / prediction: 2026-10-06T10:10:23.403898+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: None

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | — | — | — | — | 0.0000% | 0.0000% | None/None | None/None | WAIT |
| 1m | — | — | — | — | 0.0000% | 0.0000% | None/None | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 0.0000% | None/None | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | insufficient_evidence | insufficient_evidence | None |
| 1m | insufficient_evidence | insufficient_evidence | None |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 100.17316774944445,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:22.444244Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-02T06:00:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "992a2f8e1c3df561a12df28406c2d984e65f24328eea6f643bb079e534a9d6da",
    "reason": "Freshness SLA exceeded; excluded from reasoning",
    "released_at": null,
    "rows": 216,
    "source_id": "preferred_30m",
    "status": "stale",
    "used_by_model": false
  },
  {
    "age_hours": 99.67316774944445,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:22.908201Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "15a36c9639328a75f522791d1e1fdb6f3bca9c84e8b26390f59cb9bf9bc71ec6",
    "reason": "Freshness SLA exceeded; excluded from reasoning",
    "released_at": null,
    "rows": 4930,
    "source_id": "preferred_daily",
    "status": "stale",
    "used_by_model": false
  },
  {
    "age_hours": 99.67316774944445,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:22.939741Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f713df3718ec01c3d2fc706ee0414dadf28cf3b07cf633aad0496f15660bc164",
    "reason": "Freshness SLA exceeded; excluded from reasoning",
    "released_at": null,
    "rows": 4932,
    "source_id": "common_daily",
    "status": "stale",
    "used_by_model": false
  },
  {
    "age_hours": 14.673167749444444,
    "authority": "official_original",
    "collected_at": "2026-10-06T10:10:22.492761Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-05T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251",
    "reason": null,
    "released_at": null,
    "rows": 191,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:22.938742Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "214d92ec515a38fa205843a3163103601187995c5edc4c176898b56da6eb72a5",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 99.67316774944445,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:22.978746Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "8699aa613a3407fa044ba6793c914afb057a53555cd36f75b920d0937c230757",
    "reason": "Freshness SLA exceeded; excluded from reasoning",
    "released_at": null,
    "rows": 241,
    "source_id": "kospi",
    "status": "stale",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T10:10:23.403898Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "79ecfa51989ddd78eae9fe2934d4d32f6ed25320bd74f47eb0b122c3caf8ac41",
    "reason": "unverified_DXY_cash_close_not_ICE_futures_settlement",
    "released_at": null,
    "rows": 0,
    "source_id": "dxy",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "unavailable",
    "collected_at": "2026-10-06T10:10:22.938742Z",
    "excluded": {},
    "instrument": "foreign_net_buy",
    "latest_effective_at": null,
    "provider": "not_connected",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "reason": "ValueError: No verified source credentials/series; unavailable",
    "released_at": null,
    "rows": 0,
    "source_id": "foreign_net_buy",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "unavailable",
    "collected_at": "2026-10-06T10:10:22.938742Z",
    "excluded": {},
    "instrument": "institution_net_buy",
    "latest_effective_at": null,
    "provider": "not_connected",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "reason": "ValueError: No verified source credentials/series; unavailable",
    "released_at": null,
    "rows": 0,
    "source_id": "institution_net_buy",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "unavailable",
    "collected_at": "2026-10-06T10:10:22.938742Z",
    "excluded": {},
    "instrument": "program_net_buy",
    "latest_effective_at": null,
    "provider": "not_connected",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "reason": "ValueError: No verified source credentials/series; unavailable",
    "released_at": null,
    "rows": 0,
    "source_id": "program_net_buy",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "unavailable",
    "collected_at": "2026-10-06T10:10:22.938742Z",
    "excluded": {},
    "instrument": "dram_contract_asp",
    "latest_effective_at": null,
    "provider": "not_connected",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "reason": "ValueError: No verified source credentials/series; unavailable",
    "released_at": null,
    "rows": 0,
    "source_id": "dram_contract_asp",
    "status": "unavailable",
    "used_by_model": false
  }
]
```
Document statuses: {'dram_spot': 'available_unmapped', 'exports_10': 'stale', 'exports_20': 'stale', 'exports_month': 'stale', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 0, 'last': None}, '1mo': {'count': 0, 'last': None}, '1w': {'count': 0, 'last': None}, '30m': {'count': 0, 'last': None}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: False; reasons: ['hard_missing:samsung_preferred_price', 'coverage:price_regime']
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'preferred_rsi_14', 'preferred_trend_alignment', 'preferred_volume_z', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8699aa613a3407fa044ba6793c914afb057a53555cd36f75b920d0937c230757'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-28T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1w/technical",
  "bearish_alignment": null,
  "bullish_alignment": null,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[]
```

negative_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "da164352-cba5-5c7d-921a-ddb44356a7b3",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  }
]
```

### Probability contribution reconstruction
Probability withheld. No prior is relabeled as a forecast; no numeric feedback delta exists.

### What Would Change My Mind
```json
{
  "failed_gates": [
    "future_up",
    "without_history_up",
    "confidence",
    "bottom_timing",
    "alignment",
    "liquidity",
    "meta_check"
  ],
  "falsifiers": [
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    }
  ],
  "missing_coverage": [
    "hard_missing:samsung_preferred_price",
    "coverage:price_regime"
  ],
  "missing_strong": [
    "foreign_net_buy",
    "institution_net_buy",
    "preferred_rsi_14",
    "preferred_trend_alignment",
    "preferred_volume_z",
    "usdkrw"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1m
Eligibility: False; reasons: ['hard_missing:samsung_preferred_price', 'coverage:price_regime']
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8699aa613a3407fa044ba6793c914afb057a53555cd36f75b920d0937c230757'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-28T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1m/technical",
  "bearish_alignment": null,
  "bullish_alignment": null,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:1d",
    "bars:1w"
  ],
  "flow_effect": 0.0,
  "higher": "1w",
  "higher_wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[]
```

negative_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "52728faa-eb7f-5095-8436-efcf348b1265",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  }
]
```

### Probability contribution reconstruction
Probability withheld. No prior is relabeled as a forecast; no numeric feedback delta exists.

### What Would Change My Mind
```json
{
  "failed_gates": [
    "future_up",
    "without_history_up",
    "confidence",
    "bottom_timing",
    "alignment",
    "liquidity",
    "meta_check"
  ],
  "falsifiers": [
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    }
  ],
  "missing_coverage": [
    "hard_missing:samsung_preferred_price",
    "coverage:price_regime"
  ],
  "missing_strong": [
    "dram_contract_asp",
    "foreign_net_buy",
    "hbm_demand",
    "hbm_price",
    "institution_net_buy",
    "samsung_eps",
    "samsung_eps_revision",
    "usdkrw"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1y
Eligibility: False; reasons: ['hard_missing:samsung_preferred_price', 'coverage:memory', 'coverage:price_regime', 'memory_family_quorum']
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.0, 'price_regime': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '23f849448824c7887c149f8be2c2b7e1fc50786b6533c3aff8ef6ef3b9a59f7d'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8699aa613a3407fa044ba6793c914afb057a53555cd36f75b920d0937c230757'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:cae4505fcc31eaeff9e91ff1a6b8597ab5fd6ac1b0b38d4c41097da918f98251#us_10y_yield@2026-09-28T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1y/technical",
  "bearish_alignment": null,
  "bullish_alignment": null,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:1w",
    "bars:1mo"
  ],
  "flow_effect": 0.0,
  "higher": "1mo",
  "higher_wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  },
  "primary": "1w",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '7325b1d1-bbc8-5db3-a48c-57dbc98de18d/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[]
```

negative_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "73e06ea0-65d6-5442-9aee-22834b27e3d0",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  }
]
```

### Probability contribution reconstruction
Probability withheld. No prior is relabeled as a forecast; no numeric feedback delta exists.

### What Would Change My Mind
```json
{
  "failed_gates": [
    "future_up",
    "without_history_up",
    "confidence",
    "bottom_timing",
    "alignment",
    "liquidity",
    "meta_check"
  ],
  "falsifiers": [
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    }
  ],
  "missing_coverage": [
    "hard_missing:samsung_preferred_price",
    "coverage:memory",
    "coverage:price_regime",
    "memory_family_quorum"
  ],
  "missing_strong": [
    "bit_supply",
    "cxmt_memory_capacity",
    "dram_contract_asp",
    "equity_discount_rate",
    "fab_capacity",
    "gpu_demand_growth",
    "hbm_demand",
    "hbm_price",
    "hyperscaler_capex",
    "memory_bit_shipment",
    "memory_inventory",
    "new_capacity",
    "samsung_eps",
    "samsung_eps_revision",
    "samsung_forward_per",
    "samsung_free_cash_flow",
    "usdkrw",
    "yield_rate"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## Findings for the next PDCA
- Data timing bug fix; model/graph/weights/thresholds unchanged.
- Treasury effective time is approximate 15:30 ET with date precision; release time unknown.
- Unverified FX/DXY daily close unavailable; new US equity and oil diagnostics do not enter reasoning.
- Calibration remains unvalidated; reversal scores are not calibrated probabilities.
- OP-F02: prior-close intraday bars remain subject to frozen freshness, including midday exceptions.
