# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: a590557f-d671-5a7f-afec-0c2906e05b6e
Cutoff / prediction: 2026-10-17T22:00:11.370240+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-16T06:30:00+00:00', 'source_refs': ['raw:e7c427d9bb9661f265714246cc0946ca365b393ee5b159c738dcc934490913f1'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 167200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 37.6846% | 40.6814% | 21.6340% | 6.3210% | 10.0000% | 10.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 37.5688% | 40.3414% | 22.0898% | 3.2044% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 37.6846% / 40.6814% / 21.6340% | 37.6846% / 40.6814% / 21.6340% | [0.0, 0.0, 0.0] |
| 1m | 38.7546% / 39.0881% / 22.1572% | 37.5688% / 40.3414% / 22.0898% | [-1.185801600719083, 1.2532389763513396, -0.06743737563226493] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 39.5031584,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:10.480336Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e7c427d9bb9661f265714246cc0946ca365b393ee5b159c738dcc934490913f1",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.5031584,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:11.011158Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.5031584,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:10.866575Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 26.5031584,
    "authority": "official_original",
    "collected_at": "2026-10-17T22:00:10.425382Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-16T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633",
    "reason": null,
    "released_at": null,
    "rows": 199,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:10.920443Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "ccc9463054ec4ba07c6600620d9f260bbdf19f6d41790322f020d139de9aaff8",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.5031584,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:10.930715Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "83e1d3d8b462add4c108acfd653afed461625c5c5266737018dd573d529c111e",
    "reason": null,
    "released_at": null,
    "rows": 245,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-17T22:00:11.369242Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "23c6f449da4348cb26e4f65cba04aafc900a509b0e3d4d5b3833fb3956d9628b",
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
    "collected_at": "2026-10-17T22:00:10.920443Z",
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
    "collected_at": "2026-10-17T22:00:10.920443Z",
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
    "collected_at": "2026-10-17T22:00:10.920443Z",
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
    "collected_at": "2026-10-17T22:00:10.920443Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-16T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-16T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-16T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:83e1d3d8b462add4c108acfd653afed461625c5c5266737018dd573d529c111e'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "a590557f-d671-5a7f-afec-0c2906e05b6e/1w/technical",
  "bearish_alignment": 0.4,
  "bullish_alignment": 0.0,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 10635.428026631338,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      4913,
      4923
    ],
    "bottom_score": 0.0,
    "rsi": 37.3559943028347,
    "sma": [
      193675.0,
      187461.66666666666,
      190230.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 183400.0,
    "top_pivots": [
      4910,
      4919
    ],
    "top_score": 0.35,
    "volume_ratio": 1.050487717885096
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 2717.7238324213176,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 168000.0,
    "bottom_pivots": [
      203,
      211
    ],
    "bottom_score": 0.1,
    "rsi": 50.518477044209696,
    "sma": [
      163565.0,
      172988.33333333334,
      186084.16666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 164900.0,
    "top_pivots": [
      206,
      213
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a590557f-d671-5a7f-afec-0c2906e05b6e/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5a261411-faef-51b0-9f9a-55106a8d03ab",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5a261411-faef-51b0-9f9a-55106a8d03ab",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5a261411-faef-51b0-9f9a-55106a8d03ab",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.03457062857794447
  }
]
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
    "hypothesis_id": "0ef8883a-f85a-50bc-bd6d-8843884adb45",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0ef8883a-f85a-50bc-bd6d-8843884adb45",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.25604111536759727
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.3755972129472105, 1.728045252082011, -0.35244803913480893] | {'down': 0.3672804525208201, 'flat': 0.2464755196086519, 'up': 0.3862440278705279} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3672804525208201, 'flat': 0.2464755196086519, 'up': 0.3862440278705279} | [0.239784270535498, -0.1847563957585896, -0.055027874776913954] | {'down': 0.3654328885632342, 'flat': 0.24592524086088277, 'up': 0.3886418705758829} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3654328885632342, 'flat': 0.24592524086088277, 'up': 0.3886418705758829} | [3.562322110347976, -2.70079841506114, -0.8615236952868172] | {'down': 0.3384249044126228, 'flat': 0.2373100039080146, 'up': 0.42426509167936266} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3384249044126228, 'flat': 0.2373100039080146, 'up': 0.42426509167936266} | [3.6326142333966582, -2.6745822740266547, -0.9580319593699954] | {'down': 0.31167908167235625, 'flat': 0.22772968431431465, 'up': 0.46059123401332924} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.31167908167235625, 'flat': 0.22772968431431465, 'up': 0.46059123401332924} | [-7.612103865888842, 9.1727277422678, -1.5606238763789775] | {'down': 0.40340635909503425, 'flat': 0.21212344555052487, 'up': 0.3844701953544408} |
| 5 | E10/causal | ['a590557f-d671-5a7f-afec-0c2906e05b6e/1w/technical'] | {'down': 0.40340635909503425, 'flat': 0.21212344555052487, 'up': 0.3844701953544408} | [-0.35663494666068885, 0.36098915071461346, -0.004354204053924615] | {'down': 0.4070162506021804, 'flat': 0.21207990350998562, 'up': 0.38090384588783394} |
| 6 | E17/scenario | ['1cb1ebfd-cf28-5a5b-a2ba-0c3fd56b8d16', '38a981cb-64e8-5050-aabb-c75068d0a813', '3dfdd0ed-8c11-5419-8f2b-976627592cb8', '89857f8b-79b0-5e08-8112-a349686ba87c'] | {'down': 0.4070162506021804, 'flat': 0.21207990350998562, 'up': 0.38090384588783394} | [0.7748004879554016, 2.1829135448939105, -2.957714032849296] | {'down': 0.4288453860511195, 'flat': 0.18250276318149267, 'up': 0.38865185076738795} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4288453860511195, 'flat': 0.18250276318149267, 'up': 0.38865185076738795} | [-0.7002702316829368, -1.2090751955695478, 1.909345427252482] | {'down': 0.416754634095424, 'flat': 0.20159621745401748, 'up': 0.3816491484505586} |
| 8 | E13/history | [] | {'down': 0.416754634095424, 'flat': 0.20159621745401748, 'up': 0.3816491484505586} | [0.0, 0.0, 0.0] | {'down': 0.416754634095424, 'flat': 0.20159621745401748, 'up': 0.3816491484505586} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.416754634095424, 'flat': 0.20159621745401748, 'up': 0.3816491484505586} | [-0.48028268601350566, -0.9940806175833983, 1.4743633035968984] | {'down': 0.40681382791959003, 'flat': 0.21633985048998647, 'up': 0.3768463215904235} |
E09 duplicate-root interaction adjustment precedes these causal steps. E10 reflexivity, E17 scenario, E14 challenger, E13 historical and E18 calibration steps are explicit; no additional hidden adjustment.

### What Would Change My Mind
```json
{
  "failed_gates": [
    "future_up",
    "without_history_up",
    "confidence",
    "bottom_timing",
    "alignment",
    "liquidity"
  ],
  "falsifiers": [
    {
      "evidence_refs": [
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "z_score"
    },
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    },
    {
      "evidence_refs": [
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
    }
  ],
  "missing_coverage": [],
  "missing_strong": [
    "foreign_net_buy",
    "institution_net_buy",
    "usdkrw"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1m
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.207765
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:83e1d3d8b462add4c108acfd653afed461625c5c5266737018dd573d529c111e'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "a590557f-d671-5a7f-afec-0c2906e05b6e/1m/technical",
  "bearish_alignment": 0.13333333333333336,
  "bullish_alignment": 0.26666666666666666,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:1d",
    "bars:1w"
  ],
  "flow_effect": 0.0,
  "higher": "1w",
  "higher_wave": {
    "atr": 24540.23207192051,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 240500.0,
    "bottom_pivots": [
      1024,
      1031
    ],
    "bottom_score": 0.0,
    "rsi": 45.79911672763005,
    "sma": [
      196280.0,
      138369.16666666666,
      94608.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 10635.428026631338,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      4913,
      4923
    ],
    "bottom_score": 0.0,
    "rsi": 37.3559943028347,
    "sma": [
      193675.0,
      187461.66666666666,
      190230.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 183400.0,
    "top_pivots": [
      4910,
      4919
    ],
    "top_score": 0.35,
    "volume_ratio": 1.050487717885096
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a590557f-d671-5a7f-afec-0c2906e05b6e/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "f09477d3-1a29-5d0e-a568-2420f2e5572b",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "f09477d3-1a29-5d0e-a568-2420f2e5572b",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
  }
]
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
    "hypothesis_id": "2375158a-61e9-5447-87a4-cdb007263701",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2375158a-61e9-5447-87a4-cdb007263701",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.3198286153675973
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2375158a-61e9-5447-87a4-cdb007263701",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.029216871422055528
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.6675399440494278, 0.8351439518141213, -0.16760400776469897] | {'down': 0.3583514395181412, 'flat': 0.248323959922353, 'up': 0.39332460055950574} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3583514395181412, 'flat': 0.248323959922353, 'up': 0.39332460055950574} | [-0.06105127592376802, 0.0767032538352419, -0.015651977911465553] | {'down': 0.3591184720564936, 'flat': 0.24816744014323835, 'up': 0.39271408780026806} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3591184720564936, 'flat': 0.24816744014323835, 'up': 0.39271408780026806} | [2.8471730803411255, -2.1451501587045785, -0.7020229216365415] | {'down': 0.3376669704694478, 'flat': 0.24114721092687294, 'up': 0.4211858186036793} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3376669704694478, 'flat': 0.24114721092687294, 'up': 0.4211858186036793} | [2.8940605185974686, -2.1291410223094998, -0.7649194962879663] | {'down': 0.3163755602463528, 'flat': 0.23349801596399328, 'up': 0.450126423789654} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3163755602463528, 'flat': 0.23349801596399328, 'up': 0.450126423789654} | [-5.640133684610654, 6.815207959494285, -1.17507427488365] | {'down': 0.3845276398412957, 'flat': 0.22174727321515678, 'up': 0.39372508694354746} |
| 5 | E10/causal | ['a590557f-d671-5a7f-afec-0c2906e05b6e/1m/technical'] | {'down': 0.3845276398412957, 'flat': 0.22174727321515678, 'up': 0.39372508694354746} | [-1.9149050626444175, 1.9258586343514739, -0.0109535717070397] | {'down': 0.4037862261848104, 'flat': 0.22163773749808638, 'up': 0.3745760363171033} |
| 6 | E17/scenario | ['4ed0ac62-18c0-5d38-b77e-7ca5fc415c9e', 'afed2b26-6225-57ec-bc9b-de87a86e810b', '86b305ba-da58-501f-942c-e4d887967827', '41da0a6b-0ad1-54eb-8964-6be7f4a6e3ac'] | {'down': 0.4037862261848104, 'flat': 0.22163773749808638, 'up': 0.3745760363171033} | [1.274915229937723, 2.072178950755882, -3.347094180693605] | {'down': 0.42450801569236923, 'flat': 0.18816679569115033, 'up': 0.3873251886164805} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42450801569236923, 'flat': 0.18816679569115033, 'up': 0.3873251886164805} | [-0.6849705659681515, -1.1566924946349866, 1.8416630606031381] | {'down': 0.41294109074601937, 'flat': 0.2065834262971817, 'up': 0.380475482956799} |
| 8 | E13/history | [] | {'down': 0.41294109074601937, 'flat': 0.2065834262971817, 'up': 0.380475482956799} | [0.0, 0.0, 0.0] | {'down': 0.41294109074601937, 'flat': 0.2065834262971817, 'up': 0.380475482956799} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.41294109074601937, 'flat': 0.2065834262971817, 'up': 0.380475482956799} | [-0.4787195834424607, -0.9527400559613652, 1.4314596394038093] | {'down': 0.4034136901864057, 'flat': 0.2208980226912198, 'up': 0.3756882871223744} |
E09 duplicate-root interaction adjustment precedes these causal steps. E10 reflexivity, E17 scenario, E14 challenger, E13 historical and E18 calibration steps are explicit; no additional hidden adjustment.

### What Would Change My Mind
```json
{
  "failed_gates": [
    "future_up",
    "without_history_up",
    "confidence",
    "bottom_timing",
    "alignment",
    "liquidity"
  ],
  "falsifiers": [
    {
      "evidence_refs": [
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "z_score"
    },
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    },
    {
      "evidence_refs": [
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
    }
  ],
  "missing_coverage": [],
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
Eligibility: False; reasons: ['coverage:memory', 'memory_family_quorum']
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.0, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '11872a723c9e2c53719dd4c708bb4c09daee62198064fd51d9e6d309494d09b5'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:83e1d3d8b462add4c108acfd653afed461625c5c5266737018dd573d529c111e'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:67e9de6cf4c8da6c068cd626571c89e70461b8eb5581b0474928f3604280f522#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e53b7e97e959976a947735524e95e31f9f8264e9ee8956a378f88fc00a8c10c5#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:0f4f9fb7b9b55698fca675ffbd37b03853ee8596186e1429274464b32b8ac633#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "a590557f-d671-5a7f-afec-0c2906e05b6e/1y/technical",
  "bearish_alignment": 0.0,
  "bullish_alignment": 0.4,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:1w",
    "bars:1mo"
  ],
  "flow_effect": 0.0,
  "higher": "1mo",
  "higher_wave": {
    "atr": 28576.496471725204,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 243500.0,
    "bottom_pivots": [
      219,
      236
    ],
    "bottom_score": 0.0,
    "rsi": 72.29598630253719,
    "sma": [
      109212.5,
      74686.66666666667,
      59831.333333333336
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 44000.0,
    "top_pivots": [
      220,
      235
    ],
    "top_score": 0.1,
    "volume_ratio": 1.2268460026612227
  },
  "primary": "1w",
  "reflexivity_effect": -0.020000000000000004,
  "regime_effect": -0.03,
  "sell_liquidity": null,
  "wave": {
    "atr": 24540.23207192051,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 240500.0,
    "bottom_pivots": [
      1024,
      1031
    ],
    "bottom_score": 0.0,
    "rsi": 45.79911672763005,
    "sma": [
      196280.0,
      138369.16666666666,
      94608.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'a590557f-d671-5a7f-afec-0c2906e05b6e/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "24abca98-25b1-5da3-b927-5366fa2ad924",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "24abca98-25b1-5da3-b927-5366fa2ad924",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
  }
]
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
    "hypothesis_id": "0a0a7deb-1c23-5dfe-b6aa-6de71b1d371e",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0a0a7deb-1c23-5dfe-b6aa-6de71b1d371e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2924911153675973
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0a0a7deb-1c23-5dfe-b6aa-6de71b1d371e",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.0018793714220555289
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
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "z_score"
    },
    {
      "evidence_refs": [
        "us_10y_yield"
      ],
      "factor_id": "us_10y_yield",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent"
    },
    {
      "evidence_refs": [
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
    }
  ],
  "missing_coverage": [
    "coverage:memory",
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
