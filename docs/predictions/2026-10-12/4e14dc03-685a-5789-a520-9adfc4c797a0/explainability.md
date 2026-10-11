# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 4e14dc03-685a-5789-a520-9adfc4c797a0
Cutoff / prediction: 2026-10-11T22:00:15.317976+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-08T06:30:00+00:00', 'source_refs': ['raw:c8faa34cdbc46da5550774e618a32440d0beea18d9bd870d4bcac25bf13db71b'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 194000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 36.5391% | 41.0624% | 22.3986% | 3.6137% | 15.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1m | 36.9775% | 40.3634% | 22.6591% | 1.8777% | 0.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 35.8403% / 41.7498% / 22.4099% | 36.5391% / 41.0624% / 22.3986% | [0.6987822898975038, -0.687470050231298, -0.011312239666202983] |
| 1m | 36.9775% / 40.3634% / 22.6591% | 36.9775% / 40.3634% / 22.6591% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 87.50425499333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-11T22:00:14.340129Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c8faa34cdbc46da5550774e618a32440d0beea18d9bd870d4bcac25bf13db71b",
    "reason": null,
    "released_at": null,
    "rows": 229,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 87.50425499333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-11T22:00:14.692616Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 87.50425499333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-11T22:00:14.747474Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 50.50425499333333,
    "authority": "official_original",
    "collected_at": "2026-10-11T22:00:14.514960Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-09T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82",
    "reason": null,
    "released_at": null,
    "rows": 195,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-11T22:00:14.889672Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "5d306907948bab9d04013b9e6927e2523d209b93fad97b9f85e66b59fccdd63e",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50425499333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-11T22:00:15.112756Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c43f6c2e79eb3487d226fada03f57806a579f970198f82c657071f787b4395f1",
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
    "collected_at": "2026-10-11T22:00:15.317976Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "441665f86111cb6aab1660ef34885ebde5b9868ba3fedc58367614bcfccfa12c",
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
    "collected_at": "2026-10-11T22:00:14.748464Z",
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
    "collected_at": "2026-10-11T22:00:14.748464Z",
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
    "collected_at": "2026-10-11T22:00:14.748464Z",
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
    "collected_at": "2026-10-11T22:00:14.748464Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-08T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-09T06:30:00+00:00'}, '30m': {'count': 229, 'last': '2026-10-08T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c43f6c2e79eb3487d226fada03f57806a579f970198f82c657071f787b4395f1'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-02T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "4e14dc03-685a-5789-a520-9adfc4c797a0/1w/technical",
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
    "atr": 9087.428642594856,
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
    "rsi": 47.81934073307465,
    "sma": [
      199405.0,
      188401.66666666666,
      189056.66666666666
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
    "volume_ratio": 0.5813296625740929
  },
  "primary": "30m",
  "reflexivity_effect": 0.015,
  "regime_effect": 0.0225,
  "sell_liquidity": null,
  "wave": {
    "atr": 1513.442348559977,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 199300.0,
    "bottom_pivots": [
      217,
      224
    ],
    "bottom_score": 0.15,
    "rsi": 34.352908660934375,
    "sma": [
      197550.0,
      199160.0,
      203564.58333333334
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
    "top_neckline": 195200.0,
    "top_pivots": [
      219,
      226
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '4e14dc03-685a-5789-a520-9adfc4c797a0/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015, 'regime_effect': 0.0225}
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
    "hypothesis_id": "52a0e4c9-c40f-5d8a-b363-750119f61022",
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
    "hypothesis_id": "52a0e4c9-c40f-5d8a-b363-750119f61022",
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
    "hypothesis_id": "52a0e4c9-c40f-5d8a-b363-750119f61022",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.09483749999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "52a0e4c9-c40f-5d8a-b363-750119f61022",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.012618049948253865
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
    "hypothesis_id": "367a1d70-e45b-5de4-88f1-1ececd6d5a3d",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.08817071232298801, -0.06635869945900152, -0.021812012863992036] | {'down': 0.34933641300540996, 'flat': 0.24978187987136008, 'up': 0.4008817071232299} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34933641300540996, 'flat': 0.24978187987136008, 'up': 0.4008817071232299} | [0.6645136691024234, -0.49848558137634, -0.16602808772607502] | {'down': 0.34435155719164656, 'flat': 0.24812159899409933, 'up': 0.40752684381425414} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34435155719164656, 'flat': 0.24812159899409933, 'up': 0.40752684381425414} | [1.1897977734713239, -0.8854319024319823, -0.3043658710393554] | {'down': 0.33549723816732674, 'flat': 0.24507794028370578, 'up': 0.4194248215489674} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33549723816732674, 'flat': 0.24507794028370578, 'up': 0.4194248215489674} | [1.1981163508504256, -0.8826692759104193, -0.3154470749399979] | {'down': 0.32667054540822255, 'flat': 0.2419234695343058, 'up': 0.43140598505747163} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.32667054540822255, 'flat': 0.2419234695343058, 'up': 0.43140598505747163} | [-7.424872735167737, 9.267435462696938, -1.8425627275292067] | {'down': 0.4193449000351919, 'flat': 0.22349784225901373, 'up': 0.35715725770579426} |
| 5 | E10/causal | ['4e14dc03-685a-5789-a520-9adfc4c797a0/1w/technical'] | {'down': 0.4193449000351919, 'flat': 0.22349784225901373, 'up': 0.35715725770579426} | [0.7391465243292372, -0.7628944130216919, 0.0237478886924658] | {'down': 0.411715955904975, 'flat': 0.2237353211459384, 'up': 0.36454872294908663} |
| 6 | E17/scenario | ['e13bb695-48d0-59e5-9a1a-3832ff1c2ea5', '0e3a9f77-9168-5f83-86b0-f435f4ac0e00', 'c25987fa-ae95-574b-a451-f03186e03d21', 'fbf10293-6406-5609-9954-fc2d7d297040'] | {'down': 0.411715955904975, 'flat': 0.2237353211459384, 'up': 0.36454872294908663} | [0.9586234665252491, 2.3736268024339147, -3.3322502689591667] | {'down': 0.43545222392931415, 'flat': 0.19041281845634672, 'up': 0.3741349576143391} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.43545222392931415, 'flat': 0.19041281845634672, 'up': 0.3741349576143391} | [-0.5574148316967342, -1.395105837517241, 1.9525206692139807] | {'down': 0.42150116555414174, 'flat': 0.20993802514848653, 'up': 0.3685608092973718} |
| 8 | E13/history | [] | {'down': 0.42150116555414174, 'flat': 0.20993802514848653, 'up': 0.3685608092973718} | [0.0, 0.0, 0.0] | {'down': 0.42150116555414174, 'flat': 0.20993802514848653, 'up': 0.3685608092973718} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.42150116555414174, 'flat': 0.20993802514848653, 'up': 0.3685608092973718} | [-0.31701396633943557, -1.0877396033816045, 1.4047535697210345] | {'down': 0.4106237695203257, 'flat': 0.22398556084569687, 'up': 0.3653906696339774} |
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c43f6c2e79eb3487d226fada03f57806a579f970198f82c657071f787b4395f1'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-02T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "4e14dc03-685a-5789-a520-9adfc4c797a0/1m/technical",
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
    "atr": 23181.788385145166,
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
    "rsi": 54.03649354201776,
    "sma": [
      198045.0,
      136554.16666666666,
      93745.41666666667
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
      1035,
      1040
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 9087.428642594856,
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
    "rsi": 47.81934073307465,
    "sma": [
      199405.0,
      188401.66666666666,
      189056.66666666666
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
    "volume_ratio": 0.5813296625740929
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '4e14dc03-685a-5789-a520-9adfc4c797a0/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "9af74556-6641-5f67-b36b-a3de1ec8d578",
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
    "hypothesis_id": "9af74556-6641-5f67-b36b-a3de1ec8d578",
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
    "hypothesis_id": "9af74556-6641-5f67-b36b-a3de1ec8d578",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.06749999999999999
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
    "hypothesis_id": "1c2efdd0-24cf-50c9-a245-6a118447b030",
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
    "hypothesis_id": "1c2efdd0-24cf-50c9-a245-6a118447b030",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.014719450051746135
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.030688486960844807, 0.038251242909276284, -0.00756275594842315] | {'down': 0.35038251242909274, 'flat': 0.24992437244051577, 'up': 0.3996931151303916} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35038251242909274, 'flat': 0.24992437244051577, 'up': 0.3996931151303916} | [0.18346226989149894, -0.13809491881970337, -0.04536735107179557] | {'down': 0.3490015632408957, 'flat': 0.2494706989297978, 'up': 0.40152773782930656} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3490015632408957, 'flat': 0.2494706989297978, 'up': 0.40152773782930656} | [0.9473572506190631, -0.7095959146381337, -0.23776133598093774] | {'down': 0.34190560409451437, 'flat': 0.24709308556998844, 'up': 0.4110013103354972} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.34190560409451437, 'flat': 0.24709308556998844, 'up': 0.4110013103354972} | [0.9532890928994842, -0.7082416002842262, -0.24504749261525793] | {'down': 0.3348231880916721, 'flat': 0.24464261064383586, 'up': 0.42053420126449204} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3348231880916721, 'flat': 0.24464261064383586, 'up': 0.42053420126449204} | [-5.529426739304011, 6.924858792261729, -1.395432052957707] | {'down': 0.4040717760142894, 'flat': 0.2306882901142588, 'up': 0.3652399338714519} |
| 5 | E10/causal | ['4e14dc03-685a-5789-a520-9adfc4c797a0/1m/technical'] | {'down': 0.4040717760142894, 'flat': 0.2306882901142588, 'up': 0.3652399338714519} | [0.08243887489353119, -0.08434289402694528, 0.0019040191334196432] | {'down': 0.40322834707401994, 'flat': 0.23070733030559298, 'up': 0.36606432262038724} |
| 6 | E17/scenario | ['b3bdc9f4-fe34-5114-8cb0-96700de41892', '166bced6-bb6e-55a1-b321-b604451cdec5', '784a3da2-5ecc-5216-96c5-4caee548f9c0', 'be49c03f-b537-5c08-8474-536a7c84e5bc'] | {'down': 0.40322834707401994, 'flat': 0.23070733030559298, 'up': 0.36606432262038724} | [1.4104322655303814, 2.2823163640621202, -3.6927486295925127] | {'down': 0.42605151071464115, 'flat': 0.19377984400966786, 'up': 0.38016864527569105} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42605151071464115, 'flat': 0.19377984400966786, 'up': 0.38016864527569105} | [-0.6390389760183135, -1.26508240630398, 1.9041213823222964] | {'down': 0.41340068665160135, 'flat': 0.21282105783289082, 'up': 0.3737782555155079} |
| 8 | E13/history | [] | {'down': 0.41340068665160135, 'flat': 0.21282105783289082, 'up': 0.3737782555155079} | [0.0, 0.0, 0.0] | {'down': 0.41340068665160135, 'flat': 0.21282105783289082, 'up': 0.3737782555155079} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.41340068665160135, 'flat': 0.21282105783289082, 'up': 0.3737782555155079} | [-0.40030344343532365, -0.9766901603017908, 1.3769936037371089] | {'down': 0.40363378504858344, 'flat': 0.2265909938702619, 'up': 0.3697752210811547} |
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '90dd05e81a0fc040fc184096aa6c3e71b1680af79f0749124348d3e7f9d6198a'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c43f6c2e79eb3487d226fada03f57806a579f970198f82c657071f787b4395f1'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_rsi_14@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_trend_alignment@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#preferred_volume_z@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:a8f59050ec015a0e6257ef12713dfdf4799a33683169d8c6afbc759cade655ca#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:b59676d5b2abe4c7d046970aba692f7fd740e0825abd7dad93114d0a46cba8d7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4dcf56a3652624c8cdb74aa2365a5a4a7afdae9ab24ba74ae01af1e38f73cc82#us_10y_yield@2026-10-02T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "4e14dc03-685a-5789-a520-9adfc4c797a0/1y/technical",
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
    "atr": 23181.788385145166,
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
    "rsi": 54.03649354201776,
    "sma": [
      198045.0,
      136554.16666666666,
      93745.41666666667
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
      1035,
      1040
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '4e14dc03-685a-5789-a520-9adfc4c797a0/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "37de0652-27e5-51db-90de-b6e057d9a239",
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
    "hypothesis_id": "37de0652-27e5-51db-90de-b6e057d9a239",
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
    "hypothesis_id": "37de0652-27e5-51db-90de-b6e057d9a239",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.031049999999999987
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
    "hypothesis_id": "3849ee78-74f8-5f30-b5d0-194012be4603",
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
    "hypothesis_id": "3849ee78-74f8-5f30-b5d0-194012be4603",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.05116945005174613
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 50.0,
      "unit": "rsi"
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
