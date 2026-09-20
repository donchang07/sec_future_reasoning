# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 598366af-eca8-50e2-b741-d987460e6659
Cutoff / prediction: 2026-09-20T22:00:10.610786+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-18T06:30:00+00:00', 'source_refs': ['raw:8738d703a3c2ddf0a63d22f8e6997a96c17dc54faa1b392d7532fa1ab733fae1'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 196100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 39.3618% | 38.7715% | 21.8667% | 4.6612% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 39.8446% | 37.8398% | 22.3156% | 3.8371% | 45.0000% | 30.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.8355% / 38.3036% / 21.8610% | 39.3618% / 38.7715% / 21.8667% | [-0.47366854111158263, 0.4679251356831393, 0.0057434054284377645] |
| 1m | 39.3221% / 38.3516% / 22.3263% | 39.8446% / 37.8398% / 22.3156% | [0.5225129061282807, -0.5118252141480262, -0.010687691980257319] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 63.50294744055556,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:09.752720Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "8738d703a3c2ddf0a63d22f8e6997a96c17dc54faa1b392d7532fa1ab733fae1",
    "reason": null,
    "released_at": null,
    "rows": 277,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.50294744055556,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:10.095555Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.50294744055556,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:10.096555Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8",
    "reason": null,
    "released_at": null,
    "rows": 4936,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 50.50294744055556,
    "authority": "official_original",
    "collected_at": "2026-09-20T22:00:09.796348Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-18T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec",
    "reason": null,
    "released_at": null,
    "rows": 180,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:10.266781Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "198d601e9e673f402b3b904dbae5b30592f6fa3b5c5426513de839df21658754",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 63.50294744055556,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:10.308478Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d8f3d7b24b0093ac63636ae4b7cf28352f05d33ea02208234077e79d2a990ebd",
    "reason": null,
    "released_at": null,
    "rows": 244,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-20T22:00:10.610329Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "7542447cae58178ab9bdaa28a9d387d945c0154bad64efa748bfb2890296fabf",
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
    "collected_at": "2026-09-20T22:00:10.097553Z",
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
    "collected_at": "2026-09-20T22:00:10.097553Z",
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
    "collected_at": "2026-09-20T22:00:10.097553Z",
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
    "collected_at": "2026-09-20T22:00:10.097553Z",
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
Bar boundaries: {'1d': {'count': 4934, 'last': '2026-09-18T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-18T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-18T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d8f3d7b24b0093ac63636ae4b7cf28352f05d33ea02208234077e79d2a990ebd'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "598366af-eca8-50e2-b741-d987460e6659/1w/technical",
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
    "atr": 9930.872601836101,
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
      4922,
      4930
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 53.29297186877112,
    "sma": [
      192300.0,
      188770.0,
      182125.0
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4917,
      4927
    ],
    "top_score": 0.30000000000000004,
    "volume_ratio": 0.9550670307608872
  },
  "primary": "30m",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1508.2996873843815,
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
    "bottom_neckline": 200000.0,
    "bottom_pivots": [
      256,
      267
    ],
    "bottom_score": 0.0,
    "rsi": 53.42764645960255,
    "sma": [
      195767.5,
      191830.83333333334,
      194546.66666666666
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
    "top_neckline": 195500.0,
    "top_pivots": [
      264,
      274
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '598366af-eca8-50e2-b741-d987460e6659/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "5cbf9d92-771c-5437-90e0-1ee58952b33b",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.386775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5cbf9d92-771c-5437-90e0-1ee58952b33b",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5cbf9d92-771c-5437-90e0-1ee58952b33b",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5cbf9d92-771c-5437-90e0-1ee58952b33b",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.026230120228410102
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
    "hypothesis_id": "cac2e016-e231-5006-bf86-21717fcd85c3",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.18335240818326826, -0.13793651013545571, -0.04541589804781532] | {'down': 0.3486206348986454, 'flat': 0.24954584101952185, 'up': 0.4018335240818327} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3486206348986454, 'flat': 0.24954584101952185, 'up': 0.4018335240818327} | [2.7298242687005425, -2.0281420497210654, -0.7016822189794603] | {'down': 0.32833921440143476, 'flat': 0.24252901882972724, 'up': 0.42913176676883813} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.32833921440143476, 'flat': 0.24252901882972724, 'up': 0.42913176676883813} | [2.4135291390510627, -1.75512236500307, -0.6584067740480065] | {'down': 0.31078799075140406, 'flat': 0.23594495108924718, 'up': 0.45326705815934876} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.31078799075140406, 'flat': 0.23594495108924718, 'up': 0.45326705815934876} | [2.431101448929507, -1.7339127488328332, -0.697188700096682] | {'down': 0.29344886326307573, 'flat': 0.22897306408828036, 'up': 0.4775780726486438} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.29344886326307573, 'flat': 0.22897306408828036, 'up': 0.4775780726486438} | [-7.560906102567644, 8.952461673027301, -1.391555570459646] | {'down': 0.38297347999334874, 'flat': 0.2150575083836839, 'up': 0.4019690116229674} |
| 5 | E10/causal | ['598366af-eca8-50e2-b741-d987460e6659/1w/technical'] | {'down': 0.38297347999334874, 'flat': 0.2150575083836839, 'up': 0.4019690116229674} | [0.27605122953096584, -0.2727805870667288, -0.0032706424642398035] | {'down': 0.38024567412268145, 'flat': 0.2150248019590415, 'up': 0.40472952391827705} |
| 6 | E17/scenario | ['1acabee8-3e9e-5433-8eaa-fb398820550b', '54ba04e9-a200-5f46-8a6e-072daf4c5161', 'a3721986-f923-5e6d-9ce0-a7f0b1d65336', '9639ef55-1f11-5d65-b16f-0e4088d27956'] | {'down': 0.38024567412268145, 'flat': 0.2150248019590415, 'up': 0.40472952391827705} | [0.7062911558720797, 2.357351641912353, -3.063642797784427] | {'down': 0.403819190541805, 'flat': 0.18438837398119723, 'up': 0.41179243547699784} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.403819190541805, 'flat': 0.18438837398119723, 'up': 0.41179243547699784} | [-1.0414372310563913, -0.935603313754646, 1.9770405448110346] | {'down': 0.3944631574042585, 'flat': 0.20415877942930757, 'up': 0.40137806316643393} |
| 8 | E13/history | [] | {'down': 0.3944631574042585, 'flat': 0.20415877942930757, 'up': 0.40137806316643393} | [0.0, 0.0, 0.0] | {'down': 0.3944631574042585, 'flat': 0.20415877942930757, 'up': 0.40137806316643393} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3944631574042585, 'flat': 0.20415877942930757, 'up': 0.40137806316643393} | [-0.7759894739509443, -0.6748369850657465, 1.4508264590166826] | {'down': 0.38771478755360106, 'flat': 0.2186670440194744, 'up': 0.3936181684269245} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d8f3d7b24b0093ac63636ae4b7cf28352f05d33ea02208234077e79d2a990ebd'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "598366af-eca8-50e2-b741-d987460e6659/1m/technical",
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
    "atr": 24100.285538843124,
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
      1028,
      1035
    ],
    "bottom_score": 0.0,
    "rsi": 57.37291906744898,
    "sma": [
      194775.0,
      129179.16666666667,
      90211.25
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  },
  "primary": "1d",
  "reflexivity_effect": 0.015000000000000003,
  "regime_effect": 0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 9930.872601836101,
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
      4922,
      4930
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 53.29297186877112,
    "sma": [
      192300.0,
      188770.0,
      182125.0
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4917,
      4927
    ],
    "top_score": 0.30000000000000004,
    "volume_ratio": 0.9550670307608872
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '598366af-eca8-50e2-b741-d987460e6659/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015000000000000003, 'regime_effect': 0.022500000000000003}
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
    "hypothesis_id": "3d473f16-341d-55bf-8e17-5844c5637ef9",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "3d473f16-341d-55bf-8e17-5844c5637ef9",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "3d473f16-341d-55bf-8e17-5844c5637ef9",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.4323375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "3d473f16-341d-55bf-8e17-5844c5637ef9",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.0717926202284101
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
    "hypothesis_id": "f0689bbc-2eab-5742-acab-a62e15b398c8",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.19516895655166677, -0.14681854479088874, -0.04835041176076693] | {'down': 0.3485318145520911, 'flat': 0.24951649588239233, 'up': 0.4019516895655167} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3485318145520911, 'flat': 0.24951649588239233, 'up': 0.4019516895655167} | [1.1810485601783383, -0.8831731610036142, -0.2978753991747435] | {'down': 0.33970008294205495, 'flat': 0.2465377418906449, 'up': 0.4137621751673001} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33970008294205495, 'flat': 0.2465377418906449, 'up': 0.4137621751673001} | [1.914671858277417, -1.4130547460632803, -0.5016171122141339] | {'down': 0.32556953548142215, 'flat': 0.24152157076850356, 'up': 0.43290889375007424} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32556953548142215, 'flat': 0.24152157076850356, 'up': 0.43290889375007424} | [1.9320077565498806, -1.4033694182350231, -0.5286383383148519] | {'down': 0.3115358412990719, 'flat': 0.23623518738535504, 'up': 0.45222897131557305} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3115358412990719, 'flat': 0.23623518738535504, 'up': 0.45222897131557305} | [-5.6092867743745884, 6.765698976395463, -1.1564122020208818] | {'down': 0.37919283106302654, 'flat': 0.22467106536514622, 'up': 0.39613610357182716} |
| 5 | E10/causal | ['598366af-eca8-50e2-b741-d987460e6659/1m/technical'] | {'down': 0.37919283106302654, 'flat': 0.22467106536514622, 'up': 0.39613610357182716} | [1.396485125133795, -1.3717718136329549, -0.024713311500834667] | {'down': 0.365475112926697, 'flat': 0.22442393225013788, 'up': 0.4101009548231651} |
| 6 | E17/scenario | ['494a5a6b-716f-5919-952d-680ba8497a78', '195b70e0-f84c-5ddc-b0f5-25e97becb103', '9f6fa1d4-7169-5f88-86c0-e4fd848ab56d', 'd9f51dd7-21b9-5d81-9771-52b6f1a83e7f'] | {'down': 0.365475112926697, 'flat': 0.22442393225013788, 'up': 0.4101009548231651} | [0.8379474985410251, 2.5950235879804717, -3.4329710865214915] | {'down': 0.3914253488065017, 'flat': 0.19009422138492296, 'up': 0.41848042980857536} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3914253488065017, 'flat': 0.19009422138492296, 'up': 0.41848042980857536} | [-1.1278157703924707, -0.7694577254736212, 1.8972734958660864] | {'down': 0.3837307715517655, 'flat': 0.20906695634358383, 'up': 0.40720227210465065} |
| 8 | E13/history | [] | {'down': 0.3837307715517655, 'flat': 0.20906695634358383, 'up': 0.40720227210465065} | [0.0, 0.0, 0.0] | {'down': 0.3837307715517655, 'flat': 0.20906695634358383, 'up': 0.40720227210465065} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3837307715517655, 'flat': 0.20906695634358383, 'up': 0.40720227210465065} | [-0.8756366355096579, -0.5332732928707506, 1.4089099283804] | {'down': 0.378398038623058, 'flat': 0.22315605562738783, 'up': 0.3984459057495541} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'a23ef61d5d511b05999c6cb830d124118f51f0ea72fdf38dd807b232123a0d1e'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d8f3d7b24b0093ac63636ae4b7cf28352f05d33ea02208234077e79d2a990ebd'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:7658225f0f870ba43d7b530fb09b35dac20f35a42d750662792db16ea249a4d8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3fbe66642ec481defac9531b5799766b914bbaa637d5d8cf538997ee8068a718#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19d6b127616edac1ab38acf36be6faaa76ff70ea0b03b917297a0703214765ec#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "598366af-eca8-50e2-b741-d987460e6659/1y/technical",
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
    "atr": 24100.285538843124,
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
      1028,
      1035
    ],
    "bottom_score": 0.0,
    "rsi": 57.37291906744898,
    "sma": [
      194775.0,
      129179.16666666667,
      90211.25
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '598366af-eca8-50e2-b741-d987460e6659/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "da2cc0af-4dbd-5cf6-90b9-a44dd14f20d9",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "da2cc0af-4dbd-5cf6-90b9-a44dd14f20d9",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "da2cc0af-4dbd-5cf6-90b9-a44dd14f20d9",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.386775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "da2cc0af-4dbd-5cf6-90b9-a44dd14f20d9",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.026230120228410102
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
    "hypothesis_id": "19e042cf-7365-565f-8137-5d31d3eb96b8",
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
