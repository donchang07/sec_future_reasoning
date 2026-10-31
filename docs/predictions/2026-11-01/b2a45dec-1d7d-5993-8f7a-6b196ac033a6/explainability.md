# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: b2a45dec-1d7d-5993-8f7a-6b196ac033a6
Cutoff / prediction: 2026-10-31T22:00:18.054599+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-30T06:30:00+00:00', 'source_refs': ['raw:13e1b49f6de7f03d46fc79e1affc2d8bb32989d24bb29fb12c7eeba024a3f67c'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 174100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 40.1920% | 38.0898% | 21.7182% | 5.9790% | 0.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 41.2746% | 36.5998% | 22.1256% | 3.0458% | 45.0000% | 10.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 10.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 40.1920% / 38.0898% / 21.7182% | 40.1920% / 38.0898% / 21.7182% | [0.0, 0.0, 0.0] |
| 1m | 40.0383% / 37.7958% / 22.1660% | 41.2746% / 36.5998% / 22.1256% | [1.2363291678844535, -1.1959393730172851, -0.04038979486717109] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 39.50501516638889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-31T22:00:17.184805Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "13e1b49f6de7f03d46fc79e1affc2d8bb32989d24bb29fb12c7eeba024a3f67c",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.50501516638889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-31T22:00:17.617725Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.50501516638889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-31T22:00:17.570190Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 26.505015166388887,
    "authority": "official_original",
    "collected_at": "2026-10-31T22:00:17.129804Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-30T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c",
    "reason": null,
    "released_at": null,
    "rows": 209,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-31T22:00:17.622724Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "c082a98a5dae1e106ad9b47a58427374d19df865bb952e8c03e893d774abf9f0",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50501516638889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-31T22:00:17.653149Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "89c49508eb9d2d2620688a153768d625fa786e41d7e65e0c45ddf922800564d7",
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
    "collected_at": "2026-10-31T22:00:18.053600Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "017c79616417e56afe6785f822dd3ddff0dfb63a23c6d1c053a39bd36f674c21",
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
    "collected_at": "2026-10-31T22:00:17.617725Z",
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
    "collected_at": "2026-10-31T22:00:17.617725Z",
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
    "collected_at": "2026-10-31T22:00:17.617725Z",
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
    "collected_at": "2026-10-31T22:00:17.617725Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-30T06:30:00+00:00'}, '1mo': {'count': 240, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-30T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-10-30T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:89c49508eb9d2d2620688a153768d625fa786e41d7e65e0c45ddf922800564d7'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1w/technical",
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
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 3040.485586005412,
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
    "bottom_neckline": 187700.0,
    "bottom_pivots": [
      223,
      232
    ],
    "bottom_score": 0.0,
    "rsi": 43.55056764861911,
    "sma": [
      176947.5,
      176667.5,
      172580.41666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 168100.0,
    "top_pivots": [
      227,
      237
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "ffed68e2-ae5a-54fa-81df-ce35cc156ee6",
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
    "hypothesis_id": "ffed68e2-ae5a-54fa-81df-ce35cc156ee6",
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
    "hypothesis_id": "ffed68e2-ae5a-54fa-81df-ce35cc156ee6",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.23922865536215923
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
    "hypothesis_id": "52481f39-8b34-57b4-b290-3abefc121695",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "52481f39-8b34-57b4-b290-3abefc121695",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.07881259600890576
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.4228198525163318, 0.5282272053597159, -0.10540735284339242] | {'down': 0.35528227205359714, 'flat': 0.24894592647156608, 'up': 0.3957718014748367} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35528227205359714, 'flat': 0.24894592647156608, 'up': 0.3957718014748367} | [1.6776583338187545, -1.2634531112849956, -0.41420522253374226] | {'down': 0.3426477409407472, 'flat': 0.24480387424622865, 'up': 0.41254838481302425} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3426477409407472, 'flat': 0.24480387424622865, 'up': 0.41254838481302425} | [3.605841665707721, -2.6561342750840766, -0.949707390623647] | {'down': 0.3160863981899064, 'flat': 0.23530680033999218, 'up': 0.44860680147010146} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3160863981899064, 'flat': 0.23530680033999218, 'up': 0.44860680147010146} | [3.650360547002174, -2.6120104404927846, -1.038350106509403] | {'down': 0.28996629378497857, 'flat': 0.22492329927489815, 'up': 0.4851104069401232} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.28996629378497857, 'flat': 0.22492329927489815, 'up': 0.4851104069401232} | [-7.133001219826745, 8.357242550207477, -1.224241330380721] | {'down': 0.37353871928705334, 'flat': 0.21268088597109094, 'up': 0.41378039474185574} |
| 5 | E10/causal | ['b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1w/technical'] | {'down': 0.37353871928705334, 'flat': 0.21268088597109094, 'up': 0.41378039474185574} | [0.2622836736374812, -0.2562704974504504, -0.006013176187033564] | {'down': 0.37097601431254884, 'flat': 0.2126207542092206, 'up': 0.41640323147823055} |
| 6 | E17/scenario | ['3e896dd1-3f48-5b6b-84e4-d8a750d54229', 'cc98af16-ce52-5296-9a99-99035300267d', '651d0849-b3c3-5e3d-892c-7fde0f1151e3', 'd69ef472-3dc4-5a9a-b05e-94c674d5520b'] | {'down': 0.37097601431254884, 'flat': 0.2126207542092206, 'up': 0.41640323147823055} | [0.6039334640199068, 2.323076452351147, -2.9270099163710537] | {'down': 0.3942067788360603, 'flat': 0.18335065504551007, 'up': 0.4224425661184296} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3942067788360603, 'flat': 0.18335065504551007, 'up': 0.4224425661184296} | [-1.1393104288601574, -0.7783003975487868, 1.9176108264089469] | {'down': 0.38642377486057244, 'flat': 0.20252676330959954, 'up': 0.41104946182982804} |
| 8 | E13/history | [] | {'down': 0.38642377486057244, 'flat': 0.20252676330959954, 'up': 0.41104946182982804} | [0.0, 0.0, 0.0] | {'down': 0.38642377486057244, 'flat': 0.20252676330959954, 'up': 0.41104946182982804} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.38642377486057244, 'flat': 0.20252676330959954, 'up': 0.41104946182982804} | [-0.9129821092956569, -0.5525872054294112, 1.4655693147250655] | {'down': 0.38089790280627833, 'flat': 0.2171824564568502, 'up': 0.4019196407368715} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:89c49508eb9d2d2620688a153768d625fa786e41d7e65e0c45ddf922800564d7'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1m/technical",
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
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1029,
      1040
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  },
  "primary": "1d",
  "reflexivity_effect": 0.034999999999999996,
  "regime_effect": 0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.034999999999999996, 'regime_effect': 0.0525}
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
    "hypothesis_id": "13b2ff0f-0373-5f4c-9e26-9d9a0f2922a1",
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
    "hypothesis_id": "13b2ff0f-0373-5f4c-9e26-9d9a0f2922a1",
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
    "hypothesis_id": "13b2ff0f-0373-5f4c-9e26-9d9a0f2922a1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.30301615536215926
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
    "hypothesis_id": "0d929a05-e556-5f1c-97e1-9899e6736902",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0d929a05-e556-5f1c-97e1-9899e6736902",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.015025096008905767
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.03132576313215618, 0.03904571282538072, -0.007719949693218986] | {'down': 0.3503904571282538, 'flat': 0.2499228005030678, 'up': 0.39968674236867846} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3503904571282538, 'flat': 0.2499228005030678, 'up': 0.39968674236867846} | [0.8255066492084184, -0.619644886162174, -0.20586176304625559] | {'down': 0.34419400826663205, 'flat': 0.24786418287260525, 'up': 0.40794180886076264} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34419400826663205, 'flat': 0.24786418287260525, 'up': 0.40794180886076264} | [2.8700671944524467, -2.1207298691291845, -0.7493373253232571] | {'down': 0.3229867095753402, 'flat': 0.24037080961937268, 'up': 0.4366424808052871} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3229867095753402, 'flat': 0.24037080961937268, 'up': 0.4366424808052871} | [2.906550146566661, -2.097350890787064, -0.8091992557795968] | {'down': 0.30201320066746956, 'flat': 0.23227881706157671, 'up': 0.4657079822709537} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.30201320066746956, 'flat': 0.23227881706157671, 'up': 0.4657079822709537} | [-5.288597728893646, 6.271485809600364, -0.9828880807067258] | {'down': 0.3647280587634732, 'flat': 0.22244993625450946, 'up': 0.41282200498201727} |
| 5 | E10/causal | ['b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1m/technical'] | {'down': 0.3647280587634732, 'flat': 0.22244993625450946, 'up': 0.41282200498201727} | [1.8461295390760302, -1.777214305846203, -0.06891523322981874] | {'down': 0.34695591570501116, 'flat': 0.22176078392221127, 'up': 0.43128330037277757} |
| 6 | E17/scenario | ['6df07d83-69e3-5f2b-9c19-d89912586e5a', '4adb4fba-27d0-58c2-9369-040f5ab3a5ff', '562c5d78-f33d-5e25-81e4-cf1d34e2ce48', '865e6fde-4f9d-5d06-8f47-201715deb434'] | {'down': 0.34695591570501116, 'flat': 0.22176078392221127, 'up': 0.43128330037277757} | [0.5903092302574464, 2.746980878591204, -3.3372901088486424] | {'down': 0.3744257244909232, 'flat': 0.18838788283372485, 'up': 0.43718639267535203} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3744257244909232, 'flat': 0.18838788283372485, 'up': 0.43718639267535203} | [-1.3294223093837043, -0.5260234209462422, 1.8554457303299494] | {'down': 0.3691654902814608, 'flat': 0.20694234013702434, 'up': 0.423892169581515} |
| 8 | E13/history | [] | {'down': 0.3691654902814608, 'flat': 0.20694234013702434, 'up': 0.423892169581515} | [0.0, 0.0, 0.0] | {'down': 0.3691654902814608, 'flat': 0.20694234013702434, 'up': 0.423892169581515} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3691654902814608, 'flat': 0.20694234013702434, 'up': 0.423892169581515} | [-1.1146307944358502, -0.3167255902133792, 1.4313563846492239] | {'down': 0.365998234379327, 'flat': 0.22125590398351658, 'up': 0.4127458616371565} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '22834e8502acd650870c4efa81274740b2cd845e7ef47682ad792414e7861a7d'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:89c49508eb9d2d2620688a153768d625fa786e41d7e65e0c45ddf922800564d7'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7a25982855d0ce7499797b7c29393012a7e5072f5f1f79971e511ebc01566dc5#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:38e05b86256a6e2b3dce28df4bd0ef612f3fb46758f462a067435cc9c14a8077#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ae304d1376a213e7d176fbd46b12e547925a9d2b7e8cc978cef234794b52b26c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1y/technical",
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
    "atr": 30149.603866601974,
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
    "rsi": 64.65633306086202,
    "sma": [
      115682.5,
      76521.66666666667,
      61062.666666666664
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
    "volume_ratio": 1.1963416147691088
  },
  "primary": "1w",
  "reflexivity_effect": -0.030000000000000006,
  "regime_effect": -0.045000000000000005,
  "sell_liquidity": null,
  "wave": {
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1029,
      1040
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'b2a45dec-1d7d-5993-8f7a-6b196ac033a6/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.030000000000000006, 'regime_effect': -0.045000000000000005}
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
    "hypothesis_id": "ba7d2ff7-519f-5663-a4b4-59ac7344d7c7",
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
    "hypothesis_id": "ba7d2ff7-519f-5663-a4b4-59ac7344d7c7",
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
    "hypothesis_id": "ba7d2ff7-519f-5663-a4b4-59ac7344d7c7",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.18455365536215923
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
    "hypothesis_id": "72b0fad4-c250-5434-bba0-335c342c97fa",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "72b0fad4-c250-5434-bba0-335c342c97fa",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.13348759600890578
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
