# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: a30b0300-98d8-5236-9907-eeeee6965413
Cutoff / prediction: 2026-09-30T22:00:15.648623+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-30T06:30:00+00:00', 'source_refs': ['raw:2d69aee7b75d4c8c2da4dc55b2e445bb08e3e6a1f7529284588b31aadc87beb4'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 195200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 41.2655% | 37.2655% | 21.4690% | 6.8455% | 20.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1m | 41.8868% | 36.1473% | 21.9660% | 5.5030% | 30.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 42.0061% / 36.5849% / 21.4090% | 41.2655% / 37.2655% / 21.4690% | [-0.7406372789713289, 0.6805895132722006, 0.06004776569913661] |
| 1m | 40.8101% / 37.1741% / 22.0159% | 41.8868% / 36.1473% / 21.9660% | [1.0767105207122596, -1.0268003523280111, -0.04991016838425677] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504346839722222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:14.600615Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2d69aee7b75d4c8c2da4dc55b2e445bb08e3e6a1f7529284588b31aadc87beb4",
    "reason": null,
    "released_at": null,
    "rows": 253,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504346839722222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:15.031683Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a",
    "reason": null,
    "released_at": null,
    "rows": 4930,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504346839722222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:15.074193Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.504346839722222,
    "authority": "official_original",
    "collected_at": "2026-09-30T22:00:14.717427Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-30T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec",
    "reason": null,
    "released_at": null,
    "rows": 188,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:15.115849Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "3e8dd456d0c644349d5c4c69b37e87b02d2d564aefb82a761246a5571c8ddaf6",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50434683972222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:15.290966Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-29T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "23783d73972e0a2afa9c363615e007b86af22ff1755d0b669b8dc3d21214aaf2",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-30T22:00:15.648623Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "30a129bb413223bf20d4b32944e53d7fdb7201f134c8df0e805052ea88beb9d8",
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
    "collected_at": "2026-09-30T22:00:15.075199Z",
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
    "collected_at": "2026-09-30T22:00:15.075199Z",
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
    "collected_at": "2026-09-30T22:00:15.075199Z",
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
    "collected_at": "2026-09-30T22:00:15.075199Z",
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
Document statuses: {'dram_spot': 'available_unmapped', 'exports_10': 'stale', 'exports_20': 'available_unmapped', 'exports_month': 'available_unmapped', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 4930, 'last': '2026-09-30T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-25T06:30:00+00:00'}, '30m': {'count': 253, 'last': '2026-09-30T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:23783d73972e0a2afa9c363615e007b86af22ff1755d0b669b8dc3d21214aaf2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "a30b0300-98d8-5236-9907-eeeee6965413/1w/technical",
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
    "atr": 9929.909592356807,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4912,
      4920
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 49.172737038459545,
    "sma": [
      197175.0,
      188345.0,
      186406.66666666666
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
      4917,
      4926
    ],
    "top_score": 0.0,
    "volume_ratio": 1.3975415660063046
  },
  "primary": "30m",
  "reflexivity_effect": -0.014999999999999998,
  "regime_effect": -0.022499999999999996,
  "sell_liquidity": null,
  "wave": {
    "atr": 1831.017602070501,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 198000.0,
    "bottom_pivots": [
      245,
      250
    ],
    "bottom_score": 0.2,
    "rsi": 25.603029872830575,
    "sma": [
      199252.5,
      207988.33333333334,
      202206.66666666666
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
    "top_neckline": 199900.0,
    "top_pivots": [
      231,
      240
    ],
    "top_score": 0.35,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a30b0300-98d8-5236-9907-eeeee6965413/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.014999999999999998, 'regime_effect': -0.022499999999999996}
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
    "hypothesis_id": "f0d8967d-d3d6-533e-bf21-a5358dc94879",
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
    "hypothesis_id": "f0d8967d-d3d6-533e-bf21-a5358dc94879",
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
    "hypothesis_id": "f0d8967d-d3d6-533e-bf21-a5358dc94879",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.31092960053433155
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "f0d8967d-d3d6-533e-bf21-a5358dc94879",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.184275
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
    "hypothesis_id": "4ac83608-8b66-5813-9f48-1a7108b539fc",
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
    "hypothesis_id": "4ac83608-8b66-5813-9f48-1a7108b539fc",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.03497707497119422
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.1875709575663409, 0.2340100263929501, -0.0464390688266092] | {'down': 0.3523401002639295, 'flat': 0.2495356093117339, 'up': 0.3981242904243366} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3523401002639295, 'flat': 0.2495356093117339, 'up': 0.3981242904243366} | [1.2920353706682486, -0.9705853136610598, -0.32145005700717766] | {'down': 0.3426342471273189, 'flat': 0.24632110874166213, 'up': 0.4110446441310191} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3426342471273189, 'flat': 0.24632110874166213, 'up': 0.4110446441310191} | [2.204220598270007, -1.631409218074542, -0.5728113801954843] | {'down': 0.32632015494657346, 'flat': 0.2405929949397073, 'up': 0.43308685011371917} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.32632015494657346, 'flat': 0.2405929949397073, 'up': 0.43308685011371917} | [3.634004293701093, -2.6263101871464856, -1.0076941065545963] | {'down': 0.3000570530751086, 'flat': 0.23051605387416133, 'up': 0.4694268930507301} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3000570530751086, 'flat': 0.23051605387416133, 'up': 0.4694268930507301} | [3.656333041034671, -2.5681779147691874, -1.088155126265486] | {'down': 0.27437527392741673, 'flat': 0.21963450261150647, 'up': 0.5059902234610768} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.27437527392741673, 'flat': 0.21963450261150647, 'up': 0.5059902234610768} | [-7.591416887455887, 8.723118791551565, -1.1317019040956722] | {'down': 0.3616064618429324, 'flat': 0.20831748357054974, 'up': 0.43007605458651793} |
| 6 | E10/causal | ['a30b0300-98d8-5236-9907-eeeee6965413/1w/technical'] | {'down': 0.3616064618429324, 'flat': 0.20831748357054974, 'up': 0.43007605458651793} | [0.15785031209524236, -0.15210497724365557, -0.005745334851603445] | {'down': 0.3600854120704958, 'flat': 0.2082600302220337, 'up': 0.43165455770747035} |
| 7 | E17/scenario | ['a5d20d0d-fec2-5abd-b946-a75d5465acd5', 'fc89eb32-efca-5671-b8f3-9070e5e032bf', '669d164a-a438-5eee-aac6-7598f80b2bce', '1476b967-f811-59f1-bce0-0bfd164c5302'] | {'down': 0.3600854120704958, 'flat': 0.2082600302220337, 'up': 0.43165455770747035} | [0.4730350265174932, 2.276626175850971, -2.749661202368445] | {'down': 0.38285167382900553, 'flat': 0.18076341819834926, 'up': 0.4363849079726453} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.38285167382900553, 'flat': 0.18076341819834926, 'up': 0.4363849079726453} | [-1.284501217002737, -0.6172284979950426, 1.901729714997788] | {'down': 0.3766793888490551, 'flat': 0.19978071534832714, 'up': 0.4235398958026179} |
| 9 | E13/history | [] | {'down': 0.3766793888490551, 'flat': 0.19978071534832714, 'up': 0.4235398958026179} | [0.0, 0.0, 0.0] | {'down': 0.3766793888490551, 'flat': 0.19978071534832714, 'up': 0.4235398958026179} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3766793888490551, 'flat': 0.19978071534832714, 'up': 0.4235398958026179} | [-1.0884954875822028, -0.40246551638511985, 1.4909610039673087] | {'down': 0.3726547336852039, 'flat': 0.21469032538800023, 'up': 0.4126549409267959} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.32805
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:23783d73972e0a2afa9c363615e007b86af22ff1755d0b669b8dc3d21214aaf2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "a30b0300-98d8-5236-9907-eeeee6965413/1m/technical",
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
    "atr": 24085.97942892576,
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
      1026,
      1033
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1028,
      1036
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  },
  "primary": "1d",
  "reflexivity_effect": 0.030000000000000006,
  "regime_effect": 0.045000000000000005,
  "sell_liquidity": null,
  "wave": {
    "atr": 9929.909592356807,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4912,
      4920
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 49.172737038459545,
    "sma": [
      197175.0,
      188345.0,
      186406.66666666666
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
      4917,
      4926
    ],
    "top_score": 0.0,
    "volume_ratio": 1.3975415660063046
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a30b0300-98d8-5236-9907-eeeee6965413/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.030000000000000006, 'regime_effect': 0.045000000000000005}
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
    "hypothesis_id": "9c445420-19e3-5447-ba0a-0b8e18c6219b",
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
    "hypothesis_id": "9c445420-19e3-5447-ba0a-0b8e18c6219b",
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
    "hypothesis_id": "9c445420-19e3-5447-ba0a-0b8e18c6219b",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.3656046005343315
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9c445420-19e3-5447-ba0a-0b8e18c6219b",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.23894999999999997
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9c445420-19e3-5447-ba0a-0b8e18c6219b",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.019697925028805782
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
    "hypothesis_id": "ab116da6-ea34-5dd0-9c70-d4e48d7f9700",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.05352068702286772, -0.04028664624940448, -0.013234040773454914] | {'down': 0.34959713353750593, 'flat': 0.24986765959226545, 'up': 0.4005352068702287} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34959713353750593, 'flat': 0.24986765959226545, 'up': 0.4005352068702287} | [0.6509195545915558, -0.48846397068822434, -0.1624555839033398] | {'down': 0.3447124938306237, 'flat': 0.24824310375323205, 'up': 0.40704440241614426} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3447124938306237, 'flat': 0.24824310375323205, 'up': 0.40704440241614426} | [1.001559512529876, -0.746252886139076, -0.2553066263907916] | {'down': 0.33724996496923293, 'flat': 0.24569003748932414, 'up': 0.417059997541443} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.33724996496923293, 'flat': 0.24569003748932414, 'up': 0.417059997541443} | [2.8836048461921115, -2.113826093144744, -0.7697787530473621] | {'down': 0.3161117040377855, 'flat': 0.23799224995885052, 'up': 0.44589604600336413} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3161117040377855, 'flat': 0.23799224995885052, 'up': 0.44589604600336413} | [2.9138754907283237, -2.0864387222447656, -0.8274367684835776] | {'down': 0.29524731681533783, 'flat': 0.22971788227401474, 'up': 0.47503480091064737} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.29524731681533783, 'flat': 0.22971788227401474, 'up': 0.47503480091064737} | [-5.639001849333303, 6.630593420164538, -0.9915915708312267] | {'down': 0.3615532510169832, 'flat': 0.21980196656570247, 'up': 0.41864478241731434} |
| 6 | E10/causal | ['a30b0300-98d8-5236-9907-eeeee6965413/1m/technical'] | {'down': 0.3615532510169832, 'flat': 0.21980196656570247, 'up': 0.41864478241731434} | [2.2040350219425022, -2.1079382714940587, -0.0960967504484378] | {'down': 0.3404738683020426, 'flat': 0.2188409990612181, 'up': 0.44068513263673936} |
| 7 | E17/scenario | ['dde518d4-d2b7-55b9-bcc3-bb37a8eb52b3', 'e74d4ef5-759d-5464-8f95-3d2562378839', '27545d7a-fe33-5c05-8a5d-8264909ad0a9', '1376824e-8d02-51b3-8a1d-d8abf72693dc'] | {'down': 0.3404738683020426, 'flat': 0.2188409990612181, 'up': 0.44068513263673936} | [0.42587152594366073, 2.7694665967362475, -3.195338122679911] | {'down': 0.3681685342694051, 'flat': 0.18688761783441898, 'up': 0.44494384789617597} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3681685342694051, 'flat': 0.18688761783441898, 'up': 0.44494384789617597} | [-1.3933181121719984, -0.4348740492370995, 1.8281921614091035] | {'down': 0.3638197937770341, 'flat': 0.20516953944851002, 'up': 0.431010666774456} |
| 9 | E13/history | [] | {'down': 0.3638197937770341, 'flat': 0.20516953944851002, 'up': 0.431010666774456} | [0.0, 0.0, 0.0] | {'down': 0.3638197937770341, 'flat': 0.20516953944851002, 'up': 0.431010666774456} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3638197937770341, 'flat': 0.20516953944851002, 'up': 0.431010666774456} | [-1.2143031789392411, -0.2347237190128748, 1.449026897952102] | {'down': 0.36147255658690536, 'flat': 0.21965980842803104, 'up': 0.4188676349850636} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.26666666666666666, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.1417176
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '03bc2e06591f7cdf6fb33f75d57a0bdf9537a7a86b5a82c3b909e834ffa067f2'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:23783d73972e0a2afa9c363615e007b86af22ff1755d0b669b8dc3d21214aaf2'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e10c3375ac4d254c234eed1f4201f4c56dcfc3a8661387a03e2c64dd43c861df#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:0b15de5d8557329fbafe524c60f66049bf91552fffafb603476871a24d311e5a#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9275ebb7246846314fd0e12ca66588290cbf9a92534e6989b5bf7b1850951dec#us_10y_yield@2026-09-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "a30b0300-98d8-5236-9907-eeeee6965413/1y/technical",
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
    "atr": 24085.97942892576,
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
      1026,
      1033
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1028,
      1036
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'a30b0300-98d8-5236-9907-eeeee6965413/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "87dcd091-edc6-5991-8739-e882a2787cb1",
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
    "hypothesis_id": "87dcd091-edc6-5991-8739-e882a2787cb1",
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
    "hypothesis_id": "87dcd091-edc6-5991-8739-e882a2787cb1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.3170046005343315
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "87dcd091-edc6-5991-8739-e882a2787cb1",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.19034999999999996
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
    "hypothesis_id": "57623d2b-8a06-5935-ac35-75d00fbd0a1a",
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
    "hypothesis_id": "57623d2b-8a06-5935-ac35-75d00fbd0a1a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.028902074971194222
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
