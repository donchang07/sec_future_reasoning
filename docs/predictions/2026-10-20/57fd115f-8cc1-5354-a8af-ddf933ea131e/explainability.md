# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 57fd115f-8cc1-5354-a8af-ddf933ea131e
Cutoff / prediction: 2026-10-19T22:00:14.951794+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-19T06:30:00+00:00', 'source_refs': ['raw:573d0119bd8cbb42d529a68d7797b097c794a560eac402c385ee939bf3e6a947'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 170900.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 37.5685% | 40.3709% | 22.0606% | 5.0066% | 25.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 36.5141% | 41.1231% | 22.3628% | 2.5767% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 36.4055% / 41.5231% / 22.0714% | 37.5685% / 40.3709% / 22.0606% | [1.1629777589148294, -1.1521403673304398, -0.010837391584378464] |
| 1m | 37.7010% / 39.8981% / 22.4009% | 36.5141% / 41.1231% / 22.3628% | [-1.1868328877180145, 1.224933028816827, -0.03810014109882631] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504153276111111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-19T22:00:14.085620Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "573d0119bd8cbb42d529a68d7797b097c794a560eac402c385ee939bf3e6a947",
    "reason": null,
    "released_at": null,
    "rows": 205,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504153276111111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-19T22:00:14.478637Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504153276111111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-19T22:00:14.518719Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5041532761111114,
    "authority": "official_original",
    "collected_at": "2026-10-19T22:00:14.229051Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-19T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209",
    "reason": null,
    "released_at": null,
    "rows": 200,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-19T22:00:14.659460Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "6852cfa9715f5d81f2af1c01d2080ca0dd6e0c0a1daeee3c245e1bf63f21bf8a",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50415327611111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-19T22:00:14.622764Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "66eea662db3400604148bd1773e8e1a607eb971d6363c01123ceedf93203cb71",
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
    "collected_at": "2026-10-19T22:00:14.951794Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "d7e1f3d5a7c6be1fc762ac4d5946b303b97ca51d6050301ae3a8efa36e67c20c",
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
    "collected_at": "2026-10-19T22:00:14.519714Z",
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
    "collected_at": "2026-10-19T22:00:14.519714Z",
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
    "collected_at": "2026-10-19T22:00:14.519714Z",
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
    "collected_at": "2026-10-19T22:00:14.519714Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-10-19T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-16T06:30:00+00:00'}, '30m': {'count': 205, 'last': '2026-10-19T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:66eea662db3400604148bd1773e8e1a607eb971d6363c01123ceedf93203cb71'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "57fd115f-8cc1-5354-a8af-ddf933ea131e/1w/technical",
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
    "atr": 11040.040310443384,
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
    "bottom_neckline": 204500.0,
    "bottom_pivots": [
      4920,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 39.900831700296195,
    "sma": [
      192865.0,
      187490.0,
      190435.0
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
      4907,
      4916
    ],
    "top_score": 0.35,
    "volume_ratio": 0.9911765065938648
  },
  "primary": "30m",
  "reflexivity_effect": 0.025,
  "regime_effect": 0.0375,
  "sell_liquidity": null,
  "wave": {
    "atr": 3011.8545193897967,
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
    "bottom_neckline": 174500.0,
    "bottom_pivots": [
      192,
      202
    ],
    "bottom_score": 0.25,
    "rsi": 55.79707578116514,
    "sma": [
      169407.5,
      169011.66666666666,
      183025.83333333334
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
    "top_neckline": 164900.0,
    "top_pivots": [
      182,
      192
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '57fd115f-8cc1-5354-a8af-ddf933ea131e/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "fb13699f-8491-57ab-badc-0c4c76ba7b66",
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
    "hypothesis_id": "fb13699f-8491-57ab-badc-0c4c76ba7b66",
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
    "hypothesis_id": "fb13699f-8491-57ab-badc-0c4c76ba7b66",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.03826271119367777
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
    "hypothesis_id": "85905725-f8e9-5ef9-9205-f76836ff449a",
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
    "hypothesis_id": "85905725-f8e9-5ef9-9205-f76836ff449a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.09077627204600139
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.4870560336420582, 0.6087050463479682, -0.12164901270590445] | {'down': 0.35608705046347966, 'flat': 0.24878350987294096, 'up': 0.39512943966357944} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35608705046347966, 'flat': 0.24878350987294096, 'up': 0.39512943966357944} | [0.2668471486281687, -0.20242220794660648, -0.06442494068155113] | {'down': 0.3540628283840136, 'flat': 0.24813926046612544, 'up': 0.3977979111498611} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3540628283840136, 'flat': 0.24813926046612544, 'up': 0.3977979111498611} | [2.3759777641555404, -1.7820153202106614, -0.5939624439448898] | {'down': 0.336242675181907, 'flat': 0.24219963602667655, 'up': 0.42155768879141653} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.336242675181907, 'flat': 0.24219963602667655, 'up': 0.42155768879141653} | [2.4083432009204597, -1.770628304213917, -0.637714896706551] | {'down': 0.3185363921397678, 'flat': 0.23582248705961104, 'up': 0.4456411208006211} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3185363921397678, 'flat': 0.23582248705961104, 'up': 0.4456411208006211} | [-7.510804602187565, 9.212970751188854, -1.7021661490012885] | {'down': 0.41066609965165635, 'flat': 0.21880082556959815, 'up': 0.3705330747787455} |
| 5 | E10/causal | ['57fd115f-8cc1-5354-a8af-ddf933ea131e/1w/technical'] | {'down': 0.41066609965165635, 'flat': 0.21880082556959815, 'up': 0.3705330747787455} | [0.8830420948679085, -0.8986520443047596, 0.015609949436862225] | {'down': 0.40167957920860875, 'flat': 0.21895692506396677, 'up': 0.37936349572742456} |
| 6 | E17/scenario | ['27674115-4fef-563c-b7ca-d6b955bf164b', 'e58b5af7-1a36-5f15-902d-aa383e08aebb', '0c37e552-5ae9-572b-a9b6-afa48b267394', '0711e128-5d35-5765-b77d-24e4bf04469e'] | {'down': 0.40167957920860875, 'flat': 0.21895692506396677, 'up': 0.37936349572742456} | [0.8229810283619465, 2.3696709330013555, -3.1926519613633157] | {'down': 0.4253762885386223, 'flat': 0.18703040545033361, 'up': 0.387593306011044} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4253762885386223, 'flat': 0.18703040545033361, 'up': 0.387593306011044} | [-0.713285204791686, -1.2099688760109861, 1.9232540808026721] | {'down': 0.41327659977851244, 'flat': 0.20626294625836034, 'up': 0.38046045396312717} |
| 8 | E13/history | [] | {'down': 0.41327659977851244, 'flat': 0.20626294625836034, 'up': 0.38046045396312717} | [0.0, 0.0, 0.0] | {'down': 0.41327659977851244, 'flat': 0.20626294625836034, 'up': 0.38046045396312717} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.41327659977851244, 'flat': 0.20626294625836034, 'up': 0.38046045396312717} | [-0.47753325213938935, -0.9567443851168589, 1.4342776372562676] | {'down': 0.40370915592734385, 'flat': 0.220605722630923, 'up': 0.37568512144173327} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:66eea662db3400604148bd1773e8e1a607eb971d6363c01123ceedf93203cb71'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "57fd115f-8cc1-5354-a8af-ddf933ea131e/1m/technical",
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
      1023,
      1030
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
      1033,
      1038
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 11040.040310443384,
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
    "bottom_neckline": 204500.0,
    "bottom_pivots": [
      4920,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 39.900831700296195,
    "sma": [
      192865.0,
      187490.0,
      190435.0
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
      4907,
      4916
    ],
    "top_score": 0.35,
    "volume_ratio": 0.9911765065938648
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '57fd115f-8cc1-5354-a8af-ddf933ea131e/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "65814ce9-49c9-5479-9fe3-2f5bf1eb7acb",
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
    "hypothesis_id": "65814ce9-49c9-5479-9fe3-2f5bf1eb7acb",
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
    "hypothesis_id": "591632f9-e296-518b-956c-226e9854cdb4",
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
    "hypothesis_id": "591632f9-e296-518b-956c-226e9854cdb4",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2001262720460014
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "591632f9-e296-518b-956c-226e9854cdb4",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.07108728880632223
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.4175278860641618, 0.5215998785979392, -0.10407199253378296] | {'down': 0.35521599878597937, 'flat': 0.24895928007466217, 'up': 0.3958247211393584} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35521599878597937, 'flat': 0.24895928007466217, 'up': 0.3958247211393584} | [-0.14845083649687174, 0.18606501720938584, -0.0376141807125141] | {'down': 0.35707664895807323, 'flat': 0.24858313826753703, 'up': 0.3943402127743897} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.35707664895807323, 'flat': 0.24858313826753703, 'up': 0.3943402127743897} | [1.8935323638734625, -1.4283236495867713, -0.46520871428669675] | {'down': 0.3427934124622055, 'flat': 0.24393105112467006, 'up': 0.4132755364131243} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3427934124622055, 'flat': 0.24393105112467006, 'up': 0.4132755364131243} | [1.9166646206284277, -1.4226970398123984, -0.49396758081600434] | {'down': 0.32856644206408153, 'flat': 0.23899137531651002, 'up': 0.4324421826194086} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.32856644206408153, 'flat': 0.23899137531651002, 'up': 0.4324421826194086} | [-5.590456553792072, 6.896325687088761, -1.3058691332966943] | {'down': 0.39752969893496914, 'flat': 0.22593268398354308, 'up': 0.37653761708148786} |
| 5 | E10/causal | ['57fd115f-8cc1-5354-a8af-ddf933ea131e/1m/technical'] | {'down': 0.39752969893496914, 'flat': 0.22593268398354308, 'up': 0.37653761708148786} | [-1.7630260489159277, 1.8034906290919972, -0.04046458017607224] | {'down': 0.4155646052258891, 'flat': 0.22552803818178235, 'up': 0.3589073565923286} |
| 6 | E17/scenario | ['74a48d32-4a76-558b-8e9a-2233bc47c1a9', '4df8e1b4-ab1f-5b0a-9927-8816eea6d61c', 'f2793e58-3a5f-556a-bf64-ed456dfaf356', 'a403ad76-781c-58a7-95d4-d29576edc47c'] | {'down': 0.4155646052258891, 'flat': 0.22552803818178235, 'up': 0.3589073565923286} | [1.4631528602845278, 2.007873023178025, -3.471025883462553] | {'down': 0.43564333545766937, 'flat': 0.19081777934715682, 'up': 0.37353888519517386} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.43564333545766937, 'flat': 0.19081777934715682, 'up': 0.37353888519517386} | [-0.528287510249309, -1.3443192244095403, 1.8726067346588522] | {'down': 0.42220014321357396, 'flat': 0.20954384669374534, 'up': 0.3682560100926808} |
| 8 | E13/history | [] | {'down': 0.42220014321357396, 'flat': 0.20954384669374534, 'up': 0.3682560100926808} | [0.0, 0.0, 0.0] | {'down': 0.42220014321357396, 'flat': 0.20954384669374534, 'up': 0.3682560100926808} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.42220014321357396, 'flat': 0.20954384669374534, 'up': 0.3682560100926808} | [-0.3114803251772935, -1.0969321254837905, 1.4084124506610673] | {'down': 0.41123082195873606, 'flat': 0.22362797120035602, 'up': 0.36514120684090784} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '3223af7c62ea442766fb35a64d7237b2d43d9e432c897a8ce735b2b1281caab5'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:66eea662db3400604148bd1773e8e1a607eb971d6363c01123ceedf93203cb71'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_rsi_14@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_trend_alignment@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#preferred_volume_z@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:ffd305f0220e5dcab689caefd44768e5c968b40beb428f9cdb0e5f44b0f1613c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:de80de495b60eb8f08ad8ca9e60deae9133adfe7a6818557c971347fa8690320#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:da78525e556e8c306595444a982adbe596329af720189a188494bf84c9d3b209#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "57fd115f-8cc1-5354-a8af-ddf933ea131e/1y/technical",
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
      1023,
      1030
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
      1033,
      1038
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '57fd115f-8cc1-5354-a8af-ddf933ea131e/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "822138da-5cb0-5df9-98e2-f0b44ed3c176",
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
    "hypothesis_id": "822138da-5cb0-5df9-98e2-f0b44ed3c176",
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
    "hypothesis_id": "ddc7b3d1-11a2-554d-86c5-3548d005d778",
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
    "hypothesis_id": "ddc7b3d1-11a2-554d-86c5-3548d005d778",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.17278877204600138
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ddc7b3d1-11a2-554d-86c5-3548d005d778",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.04374978880632222
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
