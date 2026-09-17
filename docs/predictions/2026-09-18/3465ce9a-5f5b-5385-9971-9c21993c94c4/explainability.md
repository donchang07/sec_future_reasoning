# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 3465ce9a-5f5b-5385-9971-9c21993c94c4
Cutoff / prediction: 2026-09-17T22:00:13.196740+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-17T06:30:00+00:00', 'source_refs': ['raw:4f02680ad06a971d2e8a553b1323e87a82cca6fcdc082768362b45a1abe1b93b'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 193300.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 44.4504% | 34.5713% | 20.9784% | 7.8958% | 10.0000% | 45.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 43.9198% | 34.5312% | 21.5490% | 6.3223% | 45.0000% | 30.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 46.2289% / 33.0659% / 20.7051% | 44.4504% / 34.5713% / 20.9784% | [-1.7785636475009137, 1.5053364144002657, 0.2732272331006369] |
| 1m | 43.3615% / 35.0137% / 21.6248% | 43.9198% / 34.5312% / 21.5490% | [0.5583160071825966, -0.48250742807218194, -0.07580857911040906] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503665761111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-17T22:00:12.126985Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-17T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "4f02680ad06a971d2e8a553b1323e87a82cca6fcdc082768362b45a1abe1b93b",
    "reason": null,
    "released_at": null,
    "rows": 277,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503665761111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-17T22:00:12.591528Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-17T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503665761111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-17T22:00:12.550848Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-17T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503665761111111,
    "authority": "official_original",
    "collected_at": "2026-09-17T22:00:12.506405Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-17T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda",
    "reason": null,
    "released_at": null,
    "rows": 179,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-17T22:00:12.720411Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "531320a1a313d047cb43cd92e7b70b6d5e7ef20c05e647f9f97a1095e75d2dfc",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503665761111115,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-17T22:00:13.182270Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d3ce15299442235ff3307f5d973d304808c51b13d9854305296e4a7a9303eba7",
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
    "collected_at": "2026-09-17T22:00:13.196740Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f085fee893f64056628ccd6ab1e0126dd16055fed36626f4bb07c4acbf49b979",
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
    "collected_at": "2026-09-17T22:00:12.591528Z",
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
    "collected_at": "2026-09-17T22:00:12.591528Z",
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
    "collected_at": "2026-09-17T22:00:12.591528Z",
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
    "collected_at": "2026-09-17T22:00:12.591528Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-09-17T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-17T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d3ce15299442235ff3307f5d973d304808c51b13d9854305296e4a7a9303eba7'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-10T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "3465ce9a-5f5b-5385-9971-9c21993c94c4/1w/technical",
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
    "atr": 10179.401263515801,
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
    "rsi": 51.70672468093133,
    "sma": [
      192845.0,
      189060.0,
      181543.33333333334
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
    "volume_ratio": 0.8967376775124289
  },
  "primary": "30m",
  "reflexivity_effect": -0.03500000000000001,
  "regime_effect": -0.05250000000000001,
  "sell_liquidity": null,
  "wave": {
    "atr": 1619.2137510555938,
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
    "bottom_neckline": 197100.0,
    "bottom_pivots": [
      256,
      268
    ],
    "bottom_score": 0.1,
    "rsi": 51.658443449766295,
    "sma": [
      193620.0,
      190861.66666666666,
      193805.41666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 191900.0,
    "top_pivots": [
      264,
      274
    ],
    "top_score": 0.45000000000000007,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '3465ce9a-5f5b-5385-9971-9c21993c94c4/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.03500000000000001, 'regime_effect': -0.05250000000000001}
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
    "hypothesis_id": "71c5c4bb-0e75-5245-9f4c-c422eaf65cce",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.7462125
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "71c5c4bb-0e75-5245-9f4c-c422eaf65cce",
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
    "hypothesis_id": "71c5c4bb-0e75-5245-9f4c-c422eaf65cce",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
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
    "hypothesis_id": "80fbffdb-b8f6-596b-9cec-73278f2ce13e",
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
    "hypothesis_id": "80fbffdb-b8f6-596b-9cec-73278f2ce13e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.017705933614854095
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.09493544261551246, 0.11837551082037878, -0.023440068204855224] | {'down': 0.35118375510820377, 'flat': 0.24976559931795145, 'up': 0.3990506455738449} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35118375510820377, 'flat': 0.24976559931795145, 'up': 0.3990506455738449} | [5.294354397329915, -3.904552068942607, -1.3898023283873184] | {'down': 0.3121382344187777, 'flat': 0.23586757603407826, 'up': 0.45199418954714404} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3121382344187777, 'flat': 0.23586757603407826, 'up': 0.45199418954714404} | [4.8686684226040775, -3.4466877897669335, -1.421980632837136] | {'down': 0.27767135652110836, 'flat': 0.2216477697057069, 'up': 0.5006808737731848} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.27767135652110836, 'flat': 0.2216477697057069, 'up': 0.5006808737731848} | [4.849009002309379, -3.308422135993186, -1.5405868663161904] | {'down': 0.2445871351611765, 'flat': 0.206241901042545, 'up': 0.5491709637962786} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2445871351611765, 'flat': 0.206241901042545, 'up': 0.5491709637962786} | [-7.04661013691924, 7.741049245650802, -0.6944391087315566] | {'down': 0.3219976276176845, 'flat': 0.19929750995522943, 'up': 0.4787048624270862} |
| 5 | E10/causal | ['3465ce9a-5f5b-5385-9971-9c21993c94c4/1w/technical'] | {'down': 0.3219976276176845, 'flat': 0.19929750995522943, 'up': 0.4787048624270862} | [-0.20270194876756964, 0.18721185026018272, 0.015490098507353611] | {'down': 0.32386974612028635, 'flat': 0.19945241094030297, 'up': 0.4766778429394105} |
| 6 | E17/scenario | ['287fc6fa-31f3-508a-8936-1a5fce3c897f', 'cb3c89f3-8b66-5bc9-a3ae-1fc1ce6e0523', 'cde14578-aa1a-575f-9c9d-fb7978abcebb', 'ecdfc4d8-1cf2-5e9a-8627-c575076f19fd'] | {'down': 0.32386974612028635, 'flat': 0.19945241094030297, 'up': 0.4766778429394105} | [0.15049583116373833, 2.2784266110947025, -2.428922442258419] | {'down': 0.3466540122312334, 'flat': 0.17516318651771878, 'up': 0.4781828012510479} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3466540122312334, 'flat': 0.17516318651771878, 'up': 0.4781828012510479} | [-1.7491498597944966, -0.16085570738765265, 1.9100055671821576] | {'down': 0.34504545515735685, 'flat': 0.19426324218954036, 'up': 0.46069130265310293} |
| 8 | E13/history | [] | {'down': 0.34504545515735685, 'flat': 0.19426324218954036, 'up': 0.46069130265310293} | [0.0, 0.0, 0.0] | {'down': 0.34504545515735685, 'flat': 0.19426324218954036, 'up': 0.46069130265310293} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.34504545515735685, 'flat': 0.19426324218954036, 'up': 0.46069130265310293} | [-1.618771876639602, 0.06673977736745829, 1.5520320992721215] | {'down': 0.34571285293103143, 'flat': 0.20978356318226157, 'up': 0.4445035838867069} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d3ce15299442235ff3307f5d973d304808c51b13d9854305296e4a7a9303eba7'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-10T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "3465ce9a-5f5b-5385-9971-9c21993c94c4/1m/technical",
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
      1028,
      1035
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  },
  "primary": "1d",
  "reflexivity_effect": 0.015000000000000003,
  "regime_effect": 0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 10179.401263515801,
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
    "rsi": 51.70672468093133,
    "sma": [
      192845.0,
      189060.0,
      181543.33333333334
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
    "volume_ratio": 0.8967376775124289
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '3465ce9a-5f5b-5385-9971-9c21993c94c4/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015000000000000003, 'regime_effect': 0.022500000000000003}
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
    "hypothesis_id": "15dc80f5-ca63-543e-a8d5-cb29de5839a8",
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
    "hypothesis_id": "15dc80f5-ca63-543e-a8d5-cb29de5839a8",
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
    "hypothesis_id": "15dc80f5-ca63-543e-a8d5-cb29de5839a8",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.8373375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "15dc80f5-ca63-543e-a8d5-cb29de5839a8",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.07341906638514593
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
    "hypothesis_id": "9dbf5084-1c04-5323-9c61-58302b48bad2",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.19959374528841778, -0.15014424850409713, -0.04944949678432897] | {'down': 0.348498557514959, 'flat': 0.2495055050321567, 'up': 0.4019959374528842} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.348498557514959, 'flat': 0.2495055050321567, 'up': 0.4019959374528842} | [2.295573419437819, -1.7084022354228012, -0.5871711840150035] | {'down': 0.331414535160731, 'flat': 0.24363379319200668, 'up': 0.4249516716472624} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.331414535160731, 'flat': 0.24363379319200668, 'up': 0.4249516716472624} | [3.865006521240205, -2.803810653831984, -1.0611958674082405] | {'down': 0.30337642862241115, 'flat': 0.23302183451792427, 'up': 0.46360173685966444} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.30337642862241115, 'flat': 0.23302183451792427, 'up': 0.46360173685966444} | [3.8974210118782326, -2.7418262560000963, -1.1555947558781337] | {'down': 0.2759581660624102, 'flat': 0.22146588695914293, 'up': 0.5025759469784468} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2759581660624102, 'flat': 0.22146588695914293, 'up': 0.5025759469784468} | [-5.296340471046385, 6.037838035297299, -0.7414975642508925] | {'down': 0.3363365464153832, 'flat': 0.214050911316634, 'up': 0.4496125422679829} |
| 5 | E10/causal | ['3465ce9a-5f5b-5385-9971-9c21993c94c4/1m/technical'] | {'down': 0.3363365464153832, 'flat': 0.214050911316634, 'up': 0.4496125422679829} | [2.0917833838673294, -1.9423567950831833, -0.14942658878415727] | {'down': 0.31691297846455135, 'flat': 0.21255664542879243, 'up': 0.4705303761066562} |
| 6 | E17/scenario | ['934c2ddd-af40-5f3d-94e9-c5e3046895c6', 'f87ede4c-625a-5682-8abc-45f2a305af8b', 'b3b90819-1069-5510-add6-5e25a983e1d3', '9d8490f4-5983-5f8b-8c38-a96c0fda8dd7'] | {'down': 0.31691297846455135, 'flat': 0.21255664542879243, 'up': 0.4705303761066562} | [0.08753554509464134, 2.949338445192984, -3.0368739902876114] | {'down': 0.3464063629164812, 'flat': 0.18218790552591632, 'up': 0.4714057315576026} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3464063629164812, 'flat': 0.18218790552591632, 'up': 0.4714057315576026} | [-1.671936063178353, -0.1583029620414067, 1.8302390252197542] | {'down': 0.3448233332960671, 'flat': 0.20049029577811386, 'up': 0.4546863709258191} |
| 8 | E13/history | [] | {'down': 0.3448233332960671, 'flat': 0.20049029577811386, 'up': 0.4546863709258191} | [0.0, 0.0, 0.0] | {'down': 0.3448233332960671, 'flat': 0.20049029577811386, 'up': 0.4546863709258191} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3448233332960671, 'flat': 0.20049029577811386, 'up': 0.4546863709258191} | [-1.5488513128900594, 0.0489035084992262, 1.4999478043908332] | {'down': 0.3453123683810594, 'flat': 0.2154897738220222, 'up': 0.4391978577969185} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'ca0ed93bfc83e1a9a73f37fe841a49a5f768b10acba258be09509e8a11ff3415'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d3ce15299442235ff3307f5d973d304808c51b13d9854305296e4a7a9303eba7'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e89d0aea561e2ed3cc06fb69374337ee70660bc2748ad3a1f3047bbdb465a6ba#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:3ee6ad930ac48584dbad191dc8e06ca6d18b05e1dddf52756f1691047a85057d#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:52a608f43b75c12d18befa0557dd8071f662fc0247b7b0015acf5d33bf64bfda#us_10y_yield@2026-09-10T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "3465ce9a-5f5b-5385-9971-9c21993c94c4/1y/technical",
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
      1028,
      1035
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '3465ce9a-5f5b-5385-9971-9c21993c94c4/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "077507b7-b89e-55fc-b6d0-0cb95e01c4b0",
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
    "hypothesis_id": "077507b7-b89e-55fc-b6d0-0cb95e01c4b0",
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
    "hypothesis_id": "077507b7-b89e-55fc-b6d0-0cb95e01c4b0",
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
    "hypothesis_id": "077507b7-b89e-55fc-b6d0-0cb95e01c4b0",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.027856566385145925
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
    "hypothesis_id": "fd2d7be1-5906-59cc-87f2-55b7422e728f",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
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
