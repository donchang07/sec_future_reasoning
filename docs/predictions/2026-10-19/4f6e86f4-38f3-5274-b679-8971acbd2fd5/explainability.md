# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 4f6e86f4-38f3-5274-b679-8971acbd2fd5
Cutoff / prediction: 2026-10-18T22:00:13.834305+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-16T06:30:00+00:00', 'source_refs': ['raw:c5a6fe486ee824ce2f4888f90e1860189482345cb698753d2d38133024cd4d5f'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 167200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 36.3969% | 41.5633% | 22.0398% | 5.0562% | 10.0000% | 10.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 36.4998% | 41.1339% | 22.3663% | 2.5772% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 36.3969% / 41.5633% / 22.0398% | 36.3969% / 41.5633% / 22.0398% | [0.0, 0.0, 0.0] |
| 1m | 37.6982% / 39.9163% / 22.3855% | 36.4998% / 41.1339% / 22.3663% | [-1.1984373761651623, 1.2176167695211904, -0.019179393356011376] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 63.5038428625,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-18T22:00:12.975602Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c5a6fe486ee824ce2f4888f90e1860189482345cb698753d2d38133024cd4d5f",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.5038428625,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-18T22:00:13.323018Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.5038428625,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-18T22:00:13.381325Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 50.5038428625,
    "authority": "official_original",
    "collected_at": "2026-10-18T22:00:13.058546Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-16T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a",
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
    "collected_at": "2026-10-18T22:00:13.450162Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "d2c4c327bfa6a397cdfc87d6b9093fc9e03627e682463c26eed875c41525b545",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 63.5038428625,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-18T22:00:13.537654Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "fbc4e796a6971dffacccb67274ca3fa192ba790ed051eceb2150707310067cc0",
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
    "collected_at": "2026-10-18T22:00:13.834305Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f96b05a4841757f8b911cf76aa4114ebff1d07d5c84c50da116d61b73999c052",
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
    "collected_at": "2026-10-18T22:00:13.382324Z",
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
    "collected_at": "2026-10-18T22:00:13.382324Z",
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
    "collected_at": "2026-10-18T22:00:13.382324Z",
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
    "collected_at": "2026-10-18T22:00:13.382324Z",
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:fbc4e796a6971dffacccb67274ca3fa192ba790ed051eceb2150707310067cc0'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "4f6e86f4-38f3-5274-b679-8971acbd2fd5/1w/technical",
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
Feedback applied once: {'batch_id': '4f6e86f4-38f3-5274-b679-8971acbd2fd5/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "717df8b6-3066-5274-8a3a-1ee5002fd9ab",
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
    "hypothesis_id": "717df8b6-3066-5274-8a3a-1ee5002fd9ab",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "717df8b6-3066-5274-8a3a-1ee5002fd9ab",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.023047085718629644
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
    "hypothesis_id": "feda1929-eb67-5c3c-8461-e53b5cc02ce6",
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
    "hypothesis_id": "feda1929-eb67-5c3c-8461-e53b5cc02ce6",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.1706940769117315
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.9164735570842797, 1.148236789716689, -0.23176323263239818] | {'down': 0.36148236789716687, 'flat': 0.24768236767367602, 'up': 0.3908352644291572} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.36148236789716687, 'flat': 0.24768236767367602, 'up': 0.3908352644291572} | [0.16026204191608717, -0.12254692346342355, -0.0377151184526775] | {'down': 0.36025689866253263, 'flat': 0.24730521648914924, 'up': 0.3924378848483181} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36025689866253263, 'flat': 0.24730521648914924, 'up': 0.3924378848483181} | [2.369427691598908, -1.7922418541804097, -0.5771858374185007] | {'down': 0.34233448012072853, 'flat': 0.24153335811496424, 'up': 0.4161321617643072} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.34233448012072853, 'flat': 0.24153335811496424, 'up': 0.4161321617643072} | [2.404339151474294, -1.7828083924459726, -0.6215307590283242] | {'down': 0.3245063961962688, 'flat': 0.235318050524681, 'up': 0.4401755532790501} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3245063961962688, 'flat': 0.235318050524681, 'up': 0.4401755532790501} | [-7.516666426636237, 9.273641006581373, -1.7569745799451226] | {'down': 0.41724280626208254, 'flat': 0.21774830472522977, 'up': 0.36500888901268774} |
| 5 | E10/causal | ['4f6e86f4-38f3-5274-b679-8971acbd2fd5/1w/technical'] | {'down': 0.41724280626208254, 'flat': 0.21774830472522977, 'up': 0.36500888901268774} | [-0.23314147383320383, 0.24036429742447796, -0.007222823591276906] | {'down': 0.4196464492363273, 'flat': 0.217676076489317, 'up': 0.3626774742743557} |
| 6 | E17/scenario | ['a800223b-a786-5622-8a61-890455f09f4d', 'a5d984e1-0eac-5330-ab55-ac958cb187d7', '2b5a9ad6-32af-5722-b0a8-cc0b6bc51cec', '4bf94036-2c47-535a-828e-190db67230a4'] | {'down': 0.4196464492363273, 'flat': 0.217676076489317, 'up': 0.3626774742743557} | [0.9136174668091301, 2.179034065825819, -3.092651532634955] | {'down': 0.4414367898945855, 'flat': 0.18674956116296745, 'up': 0.371813648942447} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4414367898945855, 'flat': 0.18674956116296745, 'up': 0.371813648942447} | [-0.5051445293878742, -1.4191117932749686, 1.9242563226628513] | {'down': 0.4272456719618358, 'flat': 0.20599212438959597, 'up': 0.36676220364856826} |
| 8 | E13/history | [] | {'down': 0.4272456719618358, 'flat': 0.20599212438959597, 'up': 0.36676220364856826} | [0.0, 0.0, 0.0] | {'down': 0.4272456719618358, 'flat': 0.20599212438959597, 'up': 0.36676220364856826} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4272456719618358, 'flat': 0.20599212438959597, 'up': 0.36676220364856826} | [-0.2793602882670776, -1.1612605189799396, 1.4406208072470035] | {'down': 0.41563306677203643, 'flat': 0.220398332462066, 'up': 0.3639686007658975} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:fbc4e796a6971dffacccb67274ca3fa192ba790ed051eceb2150707310067cc0'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "4f6e86f4-38f3-5274-b679-8971acbd2fd5/1m/technical",
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
Feedback applied once: {'batch_id': '4f6e86f4-38f3-5274-b679-8971acbd2fd5/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "72216507-dbdc-5538-abf4-fd6bb87bf5fb",
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
    "hypothesis_id": "72216507-dbdc-5538-abf4-fd6bb87bf5fb",
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
    "hypothesis_id": "5cac0e15-f998-53ea-b420-c47d66ffaf21",
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
    "hypothesis_id": "5cac0e15-f998-53ea-b420-c47d66ffaf21",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2344815769117315
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5cac0e15-f998-53ea-b420-c47d66ffaf21",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.04074041428137035
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.4892630770549522, 0.6114711910601867, -0.12220811400525111] | {'down': 0.35611471191060184, 'flat': 0.2487779188599475, 'up': 0.3951073692294505} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35611471191060184, 'flat': 0.2487779188599475, 'up': 0.3951073692294505} | [-0.08508844521326053, 0.1066975292451866, -0.02160908403191497] | {'down': 0.3571816872030537, 'flat': 0.24856182801962834, 'up': 0.3942564847773179} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3571816872030537, 'flat': 0.24856182801962834, 'up': 0.3942564847773179} | [1.8934535685971698, -1.4284755524573867, -0.4649780161397804] | {'down': 0.34289693167847984, 'flat': 0.24391204785823054, 'up': 0.4131910204632896} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.34289693167847984, 'flat': 0.24391204785823054, 'up': 0.4131910204632896} | [1.9166112438730953, -1.4228692903557438, -0.49374195351735983] | {'down': 0.3286682387749224, 'flat': 0.23897462832305694, 'up': 0.43235713290202055} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3286682387749224, 'flat': 0.23897462832305694, 'up': 0.43235713290202055} | [-5.590609749243586, 6.897139116884265, -1.3065293676406657] | {'down': 0.39763962994376506, 'flat': 0.22590933464665028, 'up': 0.3764510354095847} |
| 5 | E10/causal | ['4f6e86f4-38f3-5274-b679-8971acbd2fd5/1m/technical'] | {'down': 0.39763962994376506, 'flat': 0.22590933464665028, 'up': 0.3764510354095847} | [-1.7692019010030868, 1.8100788461547168, -0.040876945151635535] | {'down': 0.41574041840531223, 'flat': 0.22550056519513392, 'up': 0.3587590163995538} |
| 6 | E17/scenario | ['db9b0b42-d21c-59b1-9097-1ecd38f76937', '311adb83-3af8-5865-9f8a-991b4f978174', 'd9cd4e9a-e2c2-558f-b51a-0613429f7ba8', 'c6042043-3e9c-5587-adb6-9ee84cace2ed'] | {'down': 0.41574041840531223, 'flat': 0.22550056519513392, 'up': 0.3587590163995538} | [1.4588876775053383, 2.004964181520408, -3.4638518590257488] | {'down': 0.4357900602205163, 'flat': 0.19086204660487643, 'up': 0.3733478931746072} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4357900602205163, 'flat': 0.19086204660487643, 'up': 0.3733478931746072} | [-0.5257643368275111, -1.346212310694822, 1.8719766475223416] | {'down': 0.4223279371135681, 'flat': 0.20958181308009985, 'up': 0.3680902498063321} |
| 8 | E13/history | [] | {'down': 0.4223279371135681, 'flat': 0.20958181308009985, 'up': 0.3680902498063321} | [0.0, 0.0, 0.0] | {'down': 0.4223279371135681, 'flat': 0.20958181308009985, 'up': 0.3680902498063321} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4223279371135681, 'flat': 0.20958181308009985, 'up': 0.3680902498063321} | [-0.3092166018279163, -1.0989103204572304, 1.4081269222851494] | {'down': 0.4113388339089958, 'flat': 0.22366308230295134, 'up': 0.36499808378805293} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '4db9fed4b52f910f87ae3e135ce8e62040c20cc334e3af0be564747609f3f842'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:fbc4e796a6971dffacccb67274ca3fa192ba790ed051eceb2150707310067cc0'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:abed0e06b183579a5bbd08123509abcf25180339290f0c2d01ebb4d493f4ca0b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ba449f77d7d91f3d1fc2039ec79d21f838043692f45db1a7aeb567063881d86e#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:036bd0a7c8ea02eb10a74051605ea988515192e698447adb8c9f5a06960c359a#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "4f6e86f4-38f3-5274-b679-8971acbd2fd5/1y/technical",
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
Feedback applied once: {'batch_id': '4f6e86f4-38f3-5274-b679-8971acbd2fd5/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "db73137c-8c94-5641-b33d-e0b095aff3ed",
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
    "hypothesis_id": "db73137c-8c94-5641-b33d-e0b095aff3ed",
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
    "hypothesis_id": "dcc040f4-0931-5f5b-867f-fc423aa4deb1",
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
    "hypothesis_id": "dcc040f4-0931-5f5b-867f-fc423aa4deb1",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2071440769117315
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "dcc040f4-0931-5f5b-867f-fc423aa4deb1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.013402914281370356
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
