# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 80caf973-64f3-5903-9e2b-788d6ac85022
Cutoff / prediction: 2026-11-02T22:00:14.798082+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-11-02T06:30:00+00:00', 'source_refs': ['raw:1279dc6815caacb26dc7bf200fac371784a86391f452eff770ee4c7690289bb6'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 177000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 38.2389% | 39.5497% | 22.2114% | 4.9390% | 25.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 39.3219% | 38.1458% | 22.5322% | 2.5030% | 35.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 10.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 37.0875% / 40.7225% / 22.1900% | 38.2389% / 39.5497% / 22.2114% | [1.1513809508333916, -1.172774935073967, 0.021393984240569708] |
| 1m | 38.1293% / 39.3793% / 22.4915% | 39.3219% / 38.1458% / 22.5322% | [1.192652821640966, -1.2334127999508504, 0.04075997830988165] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504110578333334,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-02T22:00:13.850800Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1279dc6815caacb26dc7bf200fac371784a86391f452eff770ee4c7690289bb6",
    "reason": null,
    "released_at": null,
    "rows": 229,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504110578333334,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-02T22:00:14.247155Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504110578333334,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-02T22:00:14.288138Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-11-02T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 1.5041105783333335,
    "authority": "official_original",
    "collected_at": "2026-11-02T22:00:13.981188Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-11-02T20:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e",
    "reason": null,
    "released_at": null,
    "rows": 210,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-02T22:00:14.436681Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "d487d9a2ad2fce7047d5f5cdbd9bce9b0508e4302fe9ebd9d2b1a9709c32ab07",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50411057833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-02T22:00:14.473235Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "ddc7c8a469fc8bb3873d77503c89a6b4d5190c7dea2892f46af405a7c987ceb2",
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
    "collected_at": "2026-11-02T22:00:14.798082Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "87c5e28e297e0416a7a6003e263e3cc438f4129264362a1448fcac93c6e8f262",
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
    "collected_at": "2026-11-02T22:00:14.289138Z",
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
    "collected_at": "2026-11-02T22:00:14.289138Z",
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
    "collected_at": "2026-11-02T22:00:14.289138Z",
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
    "collected_at": "2026-11-02T22:00:14.289138Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-11-02T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-30T06:30:00+00:00'}, '30m': {'count': 229, 'last': '2026-11-02T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:ddc7c8a469fc8bb3873d77503c89a6b4d5190c7dea2892f46af405a7c987ceb2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-26T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "80caf973-64f3-5903-9e2b-788d6ac85022/1w/technical",
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
    "atr": 11384.89578217031,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4918,
      4924
    ],
    "bottom_score": 0.35,
    "rsi": 47.78404695848605,
    "sma": [
      177830.0,
      187286.66666666666,
      191444.16666666666
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
    "top_neckline": 159000.0,
    "top_pivots": [
      4922,
      4928
    ],
    "top_score": 0.0,
    "volume_ratio": 0.8297584639644963
  },
  "primary": "30m",
  "reflexivity_effect": 0.025,
  "regime_effect": 0.0375,
  "sell_liquidity": null,
  "wave": {
    "atr": 2567.834172809172,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 177100.0,
    "bottom_pivots": [
      208,
      219
    ],
    "bottom_score": 0.25,
    "rsi": 52.62104227678699,
    "sma": [
      174450.0,
      178472.5,
      173059.58333333334
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
    "top_neckline": 169500.0,
    "top_pivots": [
      213,
      218
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '80caf973-64f3-5903-9e2b-788d6ac85022/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "2ecf3c64-4d4a-55e5-a0a4-99f28c436e88",
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
    "hypothesis_id": "2ecf3c64-4d4a-55e5-a0a4-99f28c436e88",
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
    "hypothesis_id": "2ecf3c64-4d4a-55e5-a0a4-99f28c436e88",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.015647133939561696
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
    "hypothesis_id": "e3b58170-b4b2-5ce6-9380-44064b62ae18",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7371000000000002
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e3b58170-b4b2-5ce6-9380-44064b62ae18",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.033753067100725107
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.10934560249536984, -0.08228763326929012, -0.02705796922607695] | {'down': 0.3491771236673071, 'flat': 0.24972942030773923, 'up': 0.4010934560249537} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3491771236673071, 'flat': 0.24972942030773923, 'up': 0.4010934560249537} | [-0.18110948997083764, 0.22562215254785523, -0.04451266257702313] | {'down': 0.35143334519278563, 'flat': 0.249284293681969, 'up': 0.39928236112524534} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.35143334519278563, 'flat': 0.249284293681969, 'up': 0.39928236112524534} | [2.376653962184566, -1.7752410173906774, -0.6014129447938998] | {'down': 0.33368093501887885, 'flat': 0.24327016423403, 'up': 0.423048900747091} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33368093501887885, 'flat': 0.24327016423403, 'up': 0.423048900747091} | [2.4082817792999753, -1.7632034966845789, -0.6450782826153745] | {'down': 0.31604890005203307, 'flat': 0.23681938140787626, 'up': 0.44713171854009076} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.31604890005203307, 'flat': 0.23681938140787626, 'up': 0.44713171854009076} | [-6.816973129898657, 8.321367272798701, -1.5043941429000618] | {'down': 0.3992625727800201, 'flat': 0.22177543997887564, 'up': 0.3789619872411042} |
| 5 | E10/causal | ['80caf973-64f3-5903-9e2b-788d6ac85022/1w/technical'] | {'down': 0.3992625727800201, 'flat': 0.22177543997887564, 'up': 0.3789619872411042} | [0.9406402798693203, -0.9464858449807989, 0.005845565111481377] | {'down': 0.3897977143302121, 'flat': 0.22183389562999045, 'up': 0.3883683900397974} |
| 6 | E17/scenario | ['51e355ae-a736-5ba5-afa7-8f6e5a044e6f', '2fdd9192-e396-5814-b2d4-46f00bdcc5d8', '9b211318-a802-5072-8e15-90ff50969d6c', '8f9519c4-18ec-5a3e-98bf-a0bf4da1d806'] | {'down': 0.3897977143302121, 'flat': 0.22183389562999045, 'up': 0.3883683900397974} | [0.8339118050128713, 2.458661314029614, -3.2925731190424745] | {'down': 0.41438432747050824, 'flat': 0.1889081644395657, 'up': 0.3967075080899261} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.41438432747050824, 'flat': 0.1889081644395657, 'up': 0.3967075080899261} | [-0.83468379521075, -1.0675003130511507, 1.9021841082618896] | {'down': 0.40370932433999673, 'flat': 0.2079300055221846, 'up': 0.3883606701378186} |
| 8 | E13/history | [] | {'down': 0.40370932433999673, 'flat': 0.2079300055221846, 'up': 0.3883606701378186} | [0.0, 0.0, 0.0] | {'down': 0.40370932433999673, 'flat': 0.2079300055221846, 'up': 0.3883606701378186} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.40370932433999673, 'flat': 0.2079300055221846, 'up': 0.3883606701378186} | [-0.5971825774434891, -0.8212433743091829, 1.418425951752675] | {'down': 0.3954968905969049, 'flat': 0.22211426503971135, 'up': 0.3823888443633837} |
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:ddc7c8a469fc8bb3873d77503c89a6b4d5190c7dea2892f46af405a7c987ceb2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-26T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "80caf973-64f3-5903-9e2b-788d6ac85022/1m/technical",
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
      1028,
      1039
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
      1031,
      1036
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  },
  "primary": "1d",
  "reflexivity_effect": 0.034999999999999996,
  "regime_effect": 0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 11384.89578217031,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4918,
      4924
    ],
    "bottom_score": 0.35,
    "rsi": 47.78404695848605,
    "sma": [
      177830.0,
      187286.66666666666,
      191444.16666666666
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
    "top_neckline": 159000.0,
    "top_pivots": [
      4922,
      4928
    ],
    "top_score": 0.0,
    "volume_ratio": 0.8297584639644963
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '80caf973-64f3-5903-9e2b-788d6ac85022/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.034999999999999996, 'regime_effect': 0.0525}
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
    "hypothesis_id": "e6277281-1266-5f20-a48d-ac4167b22ed4",
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
    "hypothesis_id": "e6277281-1266-5f20-a48d-ac4167b22ed4",
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
    "hypothesis_id": "e6277281-1266-5f20-a48d-ac4167b22ed4",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.0338721339395617
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
    "hypothesis_id": "e8e84f5c-c193-553b-a3d9-666e2eefcae1",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7371000000000002
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e8e84f5c-c193-553b-a3d9-666e2eefcae1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.015528067100725105
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.09204633552657993, -0.06927438020666865, -0.0227719553199196] | {'down': 0.3493072561979333, 'flat': 0.2497722804468008, 'up': 0.4009204633552658} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3493072561979333, 'flat': 0.2497722804468008, 'up': 0.4009204633552658} | [-0.03239003896611248, 0.040324682845305215, -0.007934643879181635] | {'down': 0.34971050302638634, 'flat': 0.249692934008009, 'up': 0.4005965629656047} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34971050302638634, 'flat': 0.249692934008009, 'up': 0.4005965629656047} | [1.8994769800795008, -1.418128021217152, -0.48134895886235984] | {'down': 0.3355292228142148, 'flat': 0.2448794444193854, 'up': 0.4195913327663997} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3355292228142148, 'flat': 0.2448794444193854, 'up': 0.4195913327663997} | [1.9207163503781877, -1.4110361638365543, -0.5096801865416334] | {'down': 0.3214188611758493, 'flat': 0.23978264255396906, 'up': 0.4387984962701816} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3214188611758493, 'flat': 0.23978264255396906, 'up': 0.4387984962701816} | [-5.075765414052752, 6.201615968994095, -1.1258505549413267] | {'down': 0.38343502086579023, 'flat': 0.2285241370045558, 'up': 0.38804084212965406} |
| 5 | E10/causal | ['80caf973-64f3-5903-9e2b-788d6ac85022/1m/technical'] | {'down': 0.38343502086579023, 'flat': 0.2285241370045558, 'up': 0.38804084212965406} | [1.3860971006199208, -1.3710723677908099, -0.015024732829113652] | {'down': 0.36972429718788213, 'flat': 0.22837388967626465, 'up': 0.40190181313585327} |
| 6 | E17/scenario | ['93acc06d-9662-57b7-9fa2-d39f052d8cb4', '84c08296-1469-5db2-845f-ce27c25d0dd7', 'e9e003a7-aff5-557c-8471-4c6aca4771ec', '18b6d543-ca6e-55fd-8702-aaf68ac589be'] | {'down': 0.36972429718788213, 'flat': 0.22837388967626465, 'up': 0.40190181313585327} | [0.9563989141723794, 2.5882376303897168, -3.544636544562116] | {'down': 0.3956066734917793, 'flat': 0.1929275242306435, 'up': 0.41146580227757706} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3956066734917793, 'flat': 0.1929275242306435, 'up': 0.41146580227757706} | [-1.0307944763609023, -0.8215664489711394, 1.8523609253320417] | {'down': 0.3873910090020679, 'flat': 0.2114511334839639, 'up': 0.40115785751396804} |
| 8 | E13/history | [] | {'down': 0.3873910090020679, 'flat': 0.2114511334839639, 'up': 0.40115785751396804} | [0.0, 0.0, 0.0] | {'down': 0.3873910090020679, 'flat': 0.2114511334839639, 'up': 0.40115785751396804} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3873910090020679, 'flat': 0.2114511334839639, 'up': 0.40115785751396804} | [-0.7938557683662029, -0.5932591542727683, 1.3871149226389878] | {'down': 0.3814584174593402, 'flat': 0.2253222827103538, 'up': 0.393219299830306} |
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'e58bf6ba641207c1c2eccf3747600640ac56ad94f861ac0cac6375d21bb060ad'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:ddc7c8a469fc8bb3873d77503c89a6b4d5190c7dea2892f46af405a7c987ceb2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_rsi_14@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_trend_alignment@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#preferred_volume_z@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:5b44e2125ad9ac386e30c0f911c70f5a9235192270cf3480128d13b0152d5e4b#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79c0f3c7e43704d27d2f440fbe2c09febe4a38c319185ada04adfc283a0d9b72#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:3d43bbdccefc1b7adba40babb0848afa68b525a5066424750adb6b189f2b520e#us_10y_yield@2026-10-26T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "80caf973-64f3-5903-9e2b-788d6ac85022/1y/technical",
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
    "atr": 30149.60386604615,
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
      218,
      235
    ],
    "bottom_score": 0.0,
    "rsi": 64.65633306538288,
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
      219,
      234
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
      1028,
      1039
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
      1031,
      1036
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '80caf973-64f3-5903-9e2b-788d6ac85022/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.030000000000000006, 'regime_effect': -0.045000000000000005}
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
    "hypothesis_id": "0fb7a40c-597e-56b4-9d34-779998b4dd64",
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
    "hypothesis_id": "0fb7a40c-597e-56b4-9d34-779998b4dd64",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
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
    "hypothesis_id": "57854a9a-b46b-52ed-96a0-913fed9392af",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7371000000000002
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "57854a9a-b46b-52ed-96a0-913fed9392af",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.1339905671007251
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "57854a9a-b46b-52ed-96a0-913fed9392af",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.08459036606043832
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
