# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 2b1c7460-99f6-5087-9aec-3cc33e29353f
Cutoff / prediction: 2026-09-11T22:00:10.532447+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-11T06:30:00+00:00', 'source_refs': ['raw:502658c79bec0e3996f9c4fba9520c259977eab8bb1d4d377753537024007a86'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 193300.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 46.5522% | 32.7697% | 20.6781% | 7.9619% | 10.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 44.1866% | 34.3055% | 21.5078% | 6.3104% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 46.0824% / 33.2121% / 20.7055% | 46.5522% / 32.7697% / 20.6781% | [0.4697357018573822, -0.44236620777883817, -0.027369494078549605] |
| 1m | 43.2702% / 35.1189% / 21.6109% | 44.1866% / 34.3055% / 21.5078% | [0.9164386833344973, -0.8133619299704797, -0.10307675336403421] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.502925679722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:09.747935Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "502658c79bec0e3996f9c4fba9520c259977eab8bb1d4d377753537024007a86",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.502925679722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:09.998632Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.502925679722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:10.059898Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e",
    "reason": null,
    "released_at": null,
    "rows": 4936,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.502925679722222,
    "authority": "official_original",
    "collected_at": "2026-09-11T22:00:09.871153Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-11T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98",
    "reason": null,
    "released_at": null,
    "rows": 175,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:10.317081Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "b50f688f4f66b9b8de15b1ce43e482fead082c062dbab9c84a55585ef808698a",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.502925679722225,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:10.423797Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-10T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2ef9645b369370b58fad831ccfb033f43081f67d34f2de873e0f6049fb1e721a",
    "reason": null,
    "released_at": null,
    "rows": 243,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-11T22:00:10.531155Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "a62a99d027cb9d0a99ac09291b4ee39130c6c64660c0a54110b950385ef1a67b",
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
    "collected_at": "2026-09-11T22:00:10.060897Z",
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
    "collected_at": "2026-09-11T22:00:10.060897Z",
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
    "collected_at": "2026-09-11T22:00:10.060897Z",
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
    "collected_at": "2026-09-11T22:00:10.060897Z",
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
Document statuses: {'dram_spot': 'available_unmapped', 'exports_10': 'available_unmapped', 'exports_20': 'available_unmapped', 'exports_month': 'available_unmapped', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 4934, 'last': '2026-09-11T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-09-11T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:2ef9645b369370b58fad831ccfb033f43081f67d34f2de873e0f6049fb1e721a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "2b1c7460-99f6-5087-9aec-3cc33e29353f/1w/technical",
  "bearish_alignment": 0.0,
  "bullish_alignment": 0.4,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 10868.827384868286,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4920,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
    "top_neckline": 172700.0,
    "top_pivots": [
      4915,
      4922
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  },
  "primary": "30m",
  "reflexivity_effect": 0.010000000000000002,
  "regime_effect": 0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1413.3919341041053,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 193300.0,
    "bottom_pivots": [
      254,
      259
    ],
    "bottom_score": 0.1,
    "rsi": 41.95290413339034,
    "sma": [
      195142.5,
      197382.5,
      192065.83333333334
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
    "top_neckline": 191000.0,
    "top_pivots": [
      251,
      261
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '2b1c7460-99f6-5087-9aec-3cc33e29353f/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.010000000000000002, 'regime_effect': 0.015}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': 1.0}, 'negative_families': [], 'positive_families': ['semiconductor_export_momentum'], 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}, 'score': 1.0, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "25a80c41-d873-5ad5-a800-866249ac1199",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.828225
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "25a80c41-d873-5ad5-a800-866249ac1199",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "25a80c41-d873-5ad5-a800-866249ac1199",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "25a80c41-d873-5ad5-a800-866249ac1199",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.059122338627238924
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
    "hypothesis_id": "82f8d234-fc69-5cf5-a8bf-e9c58ae00495",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.41362439089617786, -0.3108580781883197, -0.10276631270786374] | {'down': 0.3468914192181168, 'flat': 0.24897233687292136, 'up': 0.4041362439089618} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3468914192181168, 'flat': 0.24897233687292136, 'up': 0.4041362439089618} | [5.897320779878368, -4.316332326034028, -1.5809884538443453] | {'down': 0.3037280959577765, 'flat': 0.2331624523344779, 'up': 0.4631094517077455} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3037280959577765, 'flat': 0.2331624523344779, 'up': 0.4631094517077455} | [4.871239178492187, -3.415527550444236, -1.4557116280479399] | {'down': 0.26957282045333414, 'flat': 0.2186053360539985, 'up': 0.5118218434926673} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.26957282045333414, 'flat': 0.2186053360539985, 'up': 0.5118218434926673} | [4.830577177169704, -3.26536336052414, -1.5652138166455525] | {'down': 0.23691918684809274, 'flat': 0.20295319788754299, 'up': 0.5601276152643644} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.23691918684809274, 'flat': 0.20295319788754299, 'up': 0.5601276152643644} | [-7.160657581184015, 7.790281232438343, -0.6296236512543241] | {'down': 0.31482199917247616, 'flat': 0.19665696137499974, 'up': 0.48852103945252423} |
| 5 | E10/causal | ['2b1c7460-99f6-5087-9aec-3cc33e29353f/1w/technical'] | {'down': 0.31482199917247616, 'flat': 0.19665696137499974, 'up': 0.48852103945252423} | [1.8720186770242675, -1.6975325537375574, -0.17448612328671842] | {'down': 0.2978466736351006, 'flat': 0.19491210014213256, 'up': 0.5072412262227669} |
| 6 | E17/scenario | ['0de4cf1d-2971-5457-8014-282862565b85', '6b0617e0-cbf9-5259-97a2-479005cabfbe', '01a90855-ffc1-5f9b-9242-5c0a9a06bf47', '3c9be4ff-627f-5ffe-ba60-c05db615f295'] | {'down': 0.2978466736351006, 'flat': 0.19491210014213256, 'up': 0.5072412262227669} | [-0.12595512860813507, 2.488837724242565, -2.3628825956344386] | {'down': 0.32273505087752624, 'flat': 0.17128327418578818, 'up': 0.5059816749366856} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.32273505087752624, 'flat': 0.17128327418578818, 'up': 0.5059816749366856} | [-2.080611133525162, 0.12772149601331106, 1.952889637511862] | {'down': 0.32401226583765935, 'flat': 0.1908121705609068, 'up': 0.48517556360143393} |
| 8 | E13/history | [] | {'down': 0.32401226583765935, 'flat': 0.1908121705609068, 'up': 0.48517556360143393} | [0.0, 0.0, 0.0] | {'down': 0.32401226583765935, 'flat': 0.1908121705609068, 'up': 0.48517556360143393} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.32401226583765935, 'flat': 0.1908121705609068, 'up': 0.48517556360143393} | [-1.9653922689619185, 0.36847690108581244, 1.5969153678761006] | {'down': 0.3276970348485175, 'flat': 0.2067813242396678, 'up': 0.46552164091181475} |
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "score"
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.32805
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:2ef9645b369370b58fad831ccfb033f43081f67d34f2de873e0f6049fb1e721a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "2b1c7460-99f6-5087-9aec-3cc33e29353f/1m/technical",
  "bearish_alignment": 0.0,
  "bullish_alignment": 0.4,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:1d",
    "bars:1w"
  ],
  "flow_effect": 0.0,
  "higher": "1w",
  "higher_wave": {
    "atr": 24677.23058029259,
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
      1029,
      1036
    ],
    "bottom_score": 0.0,
    "rsi": 56.527044746782224,
    "sma": [
      192885.0,
      126817.5,
      89079.58333333333
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
    "top_neckline": 139600.0,
    "top_pivots": [
      1031,
      1039
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  },
  "primary": "1d",
  "reflexivity_effect": 0.02500000000000001,
  "regime_effect": 0.037500000000000006,
  "sell_liquidity": null,
  "wave": {
    "atr": 10868.827384868286,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4920,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
    "top_neckline": 172700.0,
    "top_pivots": [
      4915,
      4922
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '2b1c7460-99f6-5087-9aec-3cc33e29353f/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'regime_effect': 0.037500000000000006}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': 1.0}, 'negative_families': [], 'positive_families': ['semiconductor_export_momentum'], 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}, 'score': 1.0, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment']}

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
    "hypothesis_id": "9710854c-a94d-5871-ba03-7db5ad335382",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9710854c-a94d-5871-ba03-7db5ad335382",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9710854c-a94d-5871-ba03-7db5ad335382",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.8555625
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9710854c-a94d-5871-ba03-7db5ad335382",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.08645983862723894
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
    "hypothesis_id": "14f12aae-9a9b-56ec-92bb-abff6dec4dcd",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.23507671064584845, -0.1768088589272243, -0.05826785171862969] | {'down': 0.34823191141072773, 'flat': 0.2494173214828137, 'up': 0.4023507671064585} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34823191141072773, 'flat': 0.2494173214828137, 'up': 0.4023507671064585} | [2.346421156739409, -1.7453395742118571, -0.6010815825275517] | {'down': 0.33077851566860916, 'flat': 0.24340650565753819, 'up': 0.4258149786738526} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33077851566860916, 'flat': 0.24340650565753819, 'up': 0.4258149786738526} | [3.866252306326584, -2.8027357921504903, -1.0635165141760883] | {'down': 0.30275115774710426, 'flat': 0.2327713405157773, 'up': 0.46447750173711844} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.30275115774710426, 'flat': 0.2327713405157773, 'up': 0.46447750173711844} | [3.897606354730554, -2.7401005417090616, -1.157505813021484] | {'down': 0.27535015233001364, 'flat': 0.22119628238556246, 'up': 0.503453565284424} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.27535015233001364, 'flat': 0.22119628238556246, 'up': 0.503453565284424} | [-5.411214937528758, 6.166836468017866, -0.7556215304891034] | {'down': 0.3370185170101923, 'flat': 0.21364006708067143, 'up': 0.4493414159091364} |
| 5 | E10/causal | ['2b1c7460-99f6-5087-9aec-3cc33e29353f/1m/technical'] | {'down': 0.3370185170101923, 'flat': 0.21364006708067143, 'up': 0.4493414159091364} | [2.5424084655276955, -2.356747525329789, -0.1856609401979209] | {'down': 0.3134510417568944, 'flat': 0.21178345767869222, 'up': 0.47476550056441336} |
| 6 | E17/scenario | ['7b40914c-1082-55b2-9ec3-379fe6ec15e0', 'df491332-7563-50ee-b7e5-fe40eb17942c', 'be6905f8-fdf2-59b9-8c7e-b0337a09a55f', '6064af86-750b-547a-bb49-473fbbc38b13'] | {'down': 0.3134510417568944, 'flat': 0.21178345767869222, 'up': 0.47476550056441336} | [0.018823879117357833, 2.995098729502943, -3.0139226086203177] | {'down': 0.34340202905192385, 'flat': 0.18164423159248905, 'up': 0.47495373935558693} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.34340202905192385, 'flat': 0.18164423159248905, 'up': 0.47495373935558693} | [-1.7156735357441277, -0.12197814756392811, 1.8376516833080558] | {'down': 0.34218224757628457, 'flat': 0.2000207484255696, 'up': 0.45779700399814566} |
| 8 | E13/history | [] | {'down': 0.34218224757628457, 'flat': 0.2000207484255696, 'up': 0.45779700399814566} | [0.0, 0.0, 0.0] | {'down': 0.34218224757628457, 'flat': 0.2000207484255696, 'up': 0.45779700399814566} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.34218224757628457, 'flat': 0.2000207484255696, 'up': 0.45779700399814566} | [-1.5930847873594889, 0.08731381857784437, 1.5057709687816556] | {'down': 0.343055385762063, 'flat': 0.21507845811338616, 'up': 0.44186615612455077} |
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "score"
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.26666666666666666, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.1417176
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'bd8f7f124dbb49e157bdbe25686648a4c8c3d77441fc8fc7ceeb0c8f236f94ec'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:2ef9645b369370b58fad831ccfb033f43081f67d34f2de873e0f6049fb1e721a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:791bc4b0536bbfc8a23fe359d25b89f6273a026a042ff0555de4f21ac8c6886e#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:730e2fedc2dfbb7228b562c404d3264fd0d691c5787807c3e924c071f396cf1b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b39bbbba730d42597837cd38996bed632bb8b6373e2741d9de09ab5fe2f7ed98#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "2b1c7460-99f6-5087-9aec-3cc33e29353f/1y/technical",
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
    "atr": 27674.688508125186,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 70300.0,
    "bottom_pivots": [
      211,
      220
    ],
    "bottom_score": 0.35,
    "rsi": 70.98329445029191,
    "sma": [
      101602.5,
      72593.33333333333,
      58419.666666666664
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
      221,
      236
    ],
    "top_score": 0.1,
    "volume_ratio": 1.4227117714965445
  },
  "primary": "1w",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 24677.23058029259,
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
      1029,
      1036
    ],
    "bottom_score": 0.0,
    "rsi": 56.527044746782224,
    "sma": [
      192885.0,
      126817.5,
      89079.58333333333
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
    "top_neckline": 139600.0,
    "top_pivots": [
      1031,
      1039
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '2b1c7460-99f6-5087-9aec-3cc33e29353f/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': 1.0}, 'negative_families': [], 'positive_families': ['semiconductor_export_momentum'], 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}, 'score': 1.0, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment']}

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
    "hypothesis_id": "507f523f-7bda-570b-97e8-bdda72659b62",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "507f523f-7bda-570b-97e8-bdda72659b62",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "507f523f-7bda-570b-97e8-bdda72659b62",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.791775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "507f523f-7bda-570b-97e8-bdda72659b62",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.02267233862723892
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
    "hypothesis_id": "b3ad1433-7911-5247-9181-aa43d23c7884",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 0.0,
      "unit": "score"
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
