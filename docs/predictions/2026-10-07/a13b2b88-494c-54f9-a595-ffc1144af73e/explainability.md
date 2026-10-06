# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: a13b2b88-494c-54f9-a595-ffc1144af73e
Cutoff / prediction: 2026-10-06T22:00:12.948159+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-06T06:30:00+00:00', 'source_refs': ['raw:203a58620860d883d42e14e71d81c65c52d01f4d44bc369214b24a3b528ce1b8'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 198200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 34.8113% | 42.8569% | 22.3318% | 3.7019% | 10.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1m | 37.0210% | 40.3180% | 22.6610% | 1.8760% | 0.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 35.9286% / 41.6435% / 22.4280% | 34.8113% / 42.8569% / 22.3318% | [-1.1172789626534618, 1.213440850869113, -0.09616188821567617] |
| 1m | 37.0210% / 40.3180% / 22.6610% | 37.0210% / 40.3180% / 22.6610% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503596710833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T22:00:12.258388Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-06T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "203a58620860d883d42e14e71d81c65c52d01f4d44bc369214b24a3b528ce1b8",
    "reason": null,
    "released_at": null,
    "rows": 229,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503596710833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T22:00:12.456074Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-06T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503596710833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T22:00:12.586123Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-06T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503596710833333,
    "authority": "official_original",
    "collected_at": "2026-10-06T22:00:12.311897Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-06T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9",
    "reason": null,
    "released_at": null,
    "rows": 192,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T22:00:12.846603Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "e9fbad4ba1560054e52c03c37230281ebae18ea14d1f97bf02b824ffb9578be5",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 111.50359671083334,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-06T22:00:12.945125Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "895bf502aca90b036b26dd1f130417bc74ab5f9941803d6d8f61ff16d029351b",
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
    "collected_at": "2026-10-06T22:00:12.948159Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f41ad796b6f064871b55486d4997006147a47f7ba8f4ff32cdf35ce390d3b627",
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
    "collected_at": "2026-10-06T22:00:12.586123Z",
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
    "collected_at": "2026-10-06T22:00:12.586123Z",
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
    "collected_at": "2026-10-06T22:00:12.587123Z",
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
    "collected_at": "2026-10-06T22:00:12.587123Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-10-06T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-02T06:30:00+00:00'}, '30m': {'count': 229, 'last': '2026-10-06T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:895bf502aca90b036b26dd1f130417bc74ab5f9941803d6d8f61ff16d029351b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "a13b2b88-494c-54f9-a595-ffc1144af73e/1w/technical",
  "bearish_alignment": 0.13333333333333336,
  "bullish_alignment": 0.26666666666666666,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 9388.378780760899,
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
      4918,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 50.393392948800184,
    "sma": [
      199365.0,
      188076.66666666666,
      188107.5
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
    "top_neckline": 183400.0,
    "top_pivots": [
      4915,
      4924
    ],
    "top_score": 0.0,
    "volume_ratio": 0.6542269334090209
  },
  "primary": "30m",
  "reflexivity_effect": -0.024999999999999998,
  "regime_effect": -0.03749999999999999,
  "sell_liquidity": null,
  "wave": {
    "atr": 1261.9664583908673,
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
    "bottom_neckline": 202500.0,
    "bottom_pivots": [
      216,
      225
    ],
    "bottom_score": 0.1,
    "rsi": 39.926379087206065,
    "sma": [
      199230.0,
      199946.66666666666,
      204493.33333333334
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
    "top_neckline": 198900.0,
    "top_pivots": [
      203,
      217
    ],
    "top_score": 0.35,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a13b2b88-494c-54f9-a595-ffc1144af73e/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.024999999999999998, 'regime_effect': -0.03749999999999999}
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
    "hypothesis_id": "755a306e-f6fe-59ed-9af4-1b77f4a90197",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "755a306e-f6fe-59ed-9af4-1b77f4a90197",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "755a306e-f6fe-59ed-9af4-1b77f4a90197",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.0219375
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
    "hypothesis_id": "2df46534-e87a-52c2-8d59-0e3411c3cb60",
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
    "hypothesis_id": "2df46534-e87a-52c2-8d59-0e3411c3cb60",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.04290709759559875
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.2301145473478594, 0.28715802255578904, -0.057043475207932404] | {'down': 0.35287158022555787, 'flat': 0.24942956524792068, 'up': 0.39769885452652143} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35287158022555787, 'flat': 0.24942956524792068, 'up': 0.39769885452652143} | [0.15314259496108096, -0.11569897851979039, -0.03744361644127947] | {'down': 0.35171459044035996, 'flat': 0.24905512908350788, 'up': 0.39923028047613224} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.35171459044035996, 'flat': 0.24905512908350788, 'up': 0.39923028047613224} | [1.1837858098491305, -0.8891774300784805, -0.2946083797706639] | {'down': 0.34282281613957516, 'flat': 0.24610904528580124, 'up': 0.41106813857462354} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.34282281613957516, 'flat': 0.24610904528580124, 'up': 0.41106813857462354} | [1.1930563674944994, -0.887090943448765, -0.30596542404573435] | {'down': 0.3339519067050875, 'flat': 0.2430493910453439, 'up': 0.42299870224956854} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3339519067050875, 'flat': 0.2430493910453439, 'up': 0.42299870224956854} | [-7.3997748233524065, 9.327596804621264, -1.9278219812688513] | {'down': 0.42722787475130014, 'flat': 0.22377117123265539, 'up': 0.3490009540160445} |
| 5 | E10/causal | ['a13b2b88-494c-54f9-a595-ffc1144af73e/1w/technical'] | {'down': 0.42722787475130014, 'flat': 0.22377117123265539, 'up': 0.3490009540160445} | [-0.9685137378828368, 1.0194848942095547, -0.05097115632672622] | {'down': 0.4374227236933957, 'flat': 0.22326145966938812, 'up': 0.3393158166372161} |
| 6 | E17/scenario | ['1056fb1c-a793-525f-9eb4-a6e35e748a0e', '806723a6-7fc2-5ba9-9c64-38d6a3c45123', 'a8e552ff-2fa1-596f-b1ea-9ecfca9aad52', '4e75feeb-b6cc-5c10-a084-d76225b3fd8e'] | {'down': 0.4374227236933957, 'flat': 0.22326145966938812, 'up': 0.3393158166372161} | [1.1455379858677506, 2.2308526755560276, -3.376390661423778] | {'down': 0.45973125044895596, 'flat': 0.18949755305515034, 'up': 0.3507711964958936} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.45973125044895596, 'flat': 0.18949755305515034, 'up': 0.3507711964958936} | [-0.2376590609835083, -1.7226657883442242, 1.960324849327738] | {'down': 0.4425045925655137, 'flat': 0.20910080154842772, 'up': 0.34839460588605853} |
| 8 | E13/history | [] | {'down': 0.4425045925655137, 'flat': 0.20910080154842772, 'up': 0.34839460588605853} | [0.0, 0.0, 0.0] | {'down': 0.4425045925655137, 'flat': 0.20910080154842772, 'up': 0.34839460588605853} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4425045925655137, 'flat': 0.20910080154842772, 'up': 0.34839460588605853} | [-0.028187753225134005, -1.3935264868951247, 1.4217142401202505] | {'down': 0.4285693276965625, 'flat': 0.22331794394963023, 'up': 0.3481127283538072} |
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
    },
    {
      "evidence_refs": [
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:895bf502aca90b036b26dd1f130417bc74ab5f9941803d6d8f61ff16d029351b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "a13b2b88-494c-54f9-a595-ffc1144af73e/1m/technical",
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
    "atr": 24272.69518400249,
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
      1025,
      1032
    ],
    "bottom_score": 0.0,
    "rsi": 56.50121698277543,
    "sma": [
      197720.0,
      134290.83333333334,
      92659.58333333333
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
      1027,
      1035
    ],
    "top_score": 0.1,
    "volume_ratio": 0.97794445414138
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 9388.378780760899,
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
      4918,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 50.393392948800184,
    "sma": [
      199365.0,
      188076.66666666666,
      188107.5
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
    "top_neckline": 183400.0,
    "top_pivots": [
      4915,
      4924
    ],
    "top_score": 0.0,
    "volume_ratio": 0.6542269334090209
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a13b2b88-494c-54f9-a595-ffc1144af73e/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "4c4935ce-8df3-5253-a3d6-5595455995a7",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "4c4935ce-8df3-5253-a3d6-5595455995a7",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "4c4935ce-8df3-5253-a3d6-5595455995a7",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.06749999999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "4c4935ce-8df3-5253-a3d6-5595455995a7",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.00265540240440124
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
    "hypothesis_id": "fa1ab81f-d963-53c1-a57d-da29b68f9bbf",
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
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.007213663256239178, -0.00543104560055685, -0.0017826176556934303] | {'down': 0.3499456895439944, 'flat': 0.24998217382344307, 'up': 0.4000721366325624} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3499456895439944, 'flat': 0.24998217382344307, 'up': 0.4000721366325624} | [0.18350134567884924, -0.13803974961991705, -0.04546159605891276] | {'down': 0.34856529204779524, 'flat': 0.24952755786285394, 'up': 0.4019071500893509} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34856529204779524, 'flat': 0.24952755786285394, 'up': 0.4019071500893509} | [0.947541550786779, -0.7092989523639737, -0.23824259842282203] | {'down': 0.3414723025241555, 'flat': 0.24714513187862572, 'up': 0.4113825655972187} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3414723025241555, 'flat': 0.24714513187862572, 'up': 0.4113825655972187} | [0.9534450990075827, -0.7079226177464759, -0.24552248126109844] | {'down': 0.33439307634669074, 'flat': 0.24468990706601473, 'up': 0.4209170165872945} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.33439307634669074, 'flat': 0.24468990706601473, 'up': 0.4209170165872945} | [-5.529268759063838, 6.921693974275827, -1.3924252152119843] | {'down': 0.403610016089449, 'flat': 0.2307656549138949, 'up': 0.36562432899665614} |
| 5 | E10/causal | ['a13b2b88-494c-54f9-a595-ffc1144af73e/1m/technical'] | {'down': 0.403610016089449, 'flat': 0.2307656549138949, 'up': 0.36562432899665614} | [0.10961437020327036, -0.11207138718072329, 0.0024570169774529305] | {'down': 0.4024893022176418, 'flat': 0.23079022508366942, 'up': 0.36672047269868885} |
| 6 | E17/scenario | ['20bbccd6-020a-54fc-b6fb-984fbc433289', '0c6a9a85-a6f0-513d-82ea-f20d39a21bc5', '5b1a1618-d8d7-55e1-9c2a-250005c599bb', '809eae95-08a3-5cbc-afc7-70c14c0853db'] | {'down': 0.4024893022176418, 'flat': 0.23079022508366942, 'up': 0.36672047269868885} | [1.4037875987484905, 2.294852099614808, -3.6986396983633067] | {'down': 0.42543782321378987, 'flat': 0.19380382810003635, 'up': 0.38075834868617375} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42543782321378987, 'flat': 0.19380382810003635, 'up': 0.38075834868617375} | [-0.6471429238966597, -1.2568212881280405, 1.903964212024703] | {'down': 0.41286961033250946, 'flat': 0.21284347022028338, 'up': 0.37428691944720716} |
| 8 | E13/history | [] | {'down': 0.41286961033250946, 'flat': 0.21284347022028338, 'up': 0.37428691944720716} | [0.0, 0.0, 0.0] | {'down': 0.41286961033250946, 'flat': 0.21284347022028338, 'up': 0.37428691944720716} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.41286961033250946, 'flat': 0.21284347022028338, 'up': 0.37428691944720716} | [-0.40768816584672574, -0.9689724537352784, 1.376660619581993] | {'down': 0.4031798857951567, 'flat': 0.2266100764161033, 'up': 0.3702100377887399} |
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
    },
    {
      "evidence_refs": [
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'e73b20e965756dcc9a624741d2b1419af99e0b246e274fa88992f48b89a33beb'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:895bf502aca90b036b26dd1f130417bc74ab5f9941803d6d8f61ff16d029351b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:b5fc6fcd1097459296197512a43b463f9dd5e8a63fbddf8a1df233525934e02c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b74f862baea0c3674453fd7e1dd918f169805608e1f26454f6dcccfcaa7a1500#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d63bc28d428dcf4a25561b174349df857b7100d0feebde6307ff8d285bcdfce9#us_10y_yield@2026-09-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "a13b2b88-494c-54f9-a595-ffc1144af73e/1y/technical",
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
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 24272.69518400249,
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
      1025,
      1032
    ],
    "bottom_score": 0.0,
    "rsi": 56.50121698277543,
    "sma": [
      197720.0,
      134290.83333333334,
      92659.58333333333
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
      1027,
      1035
    ],
    "top_score": 0.1,
    "volume_ratio": 0.97794445414138
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'a13b2b88-494c-54f9-a595-ffc1144af73e/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "451810f6-4fe8-5463-ad70-6676cc725fb2",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "451810f6-4fe8-5463-ad70-6676cc725fb2",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "451810f6-4fe8-5463-ad70-6676cc725fb2",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.04927499999999999
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
    "hypothesis_id": "7da333d9-6da2-5d90-80b1-bbe5199c9b81",
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
    "hypothesis_id": "7da333d9-6da2-5d90-80b1-bbe5199c9b81",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.01556959759559876
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
    },
    {
      "evidence_refs": [
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
