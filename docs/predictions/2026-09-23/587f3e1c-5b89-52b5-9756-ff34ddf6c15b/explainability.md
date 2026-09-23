# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 587f3e1c-5b89-52b5-9756-ff34ddf6c15b
Cutoff / prediction: 2026-09-23T02:24:08.135080+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-22T06:30:00+00:00', 'source_refs': ['raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746'], 'timeframe': '1d', 'unit': 'krw_per_share', 'value': 211500.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 43.1982% | 35.4374% | 21.3644% | 5.2570% | 0.0000% | 0.0000% | None/None | None/None | WAIT |
| 1m | 41.8349% | 36.0685% | 22.0966% | 4.1175% | 65.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 43.1982% / 35.4374% / 21.3644% | 43.1982% / 35.4374% / 21.3644% | [0.0, 0.0, 0.0] |
| 1m | 40.9595% / 36.9195% / 22.1211% | 41.8349% / 36.0685% / 22.0966% | [0.8754435416743256, -0.8509295028746144, -0.024514038799713922] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 20.402259744444443,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:07.239038Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-22T06:00:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d3912de2dc766e83417003e03eb6844269611f7cdf01bde4f1445698f3e6a1a0",
    "reason": "Freshness SLA exceeded; excluded from reasoning",
    "released_at": null,
    "rows": 264,
    "source_id": "preferred_30m",
    "status": "stale",
    "used_by_model": false
  },
  {
    "age_hours": 19.902259744444443,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:07.689564Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 19.902259744444443,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:07.618037Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 6.902259744444445,
    "authority": "official_original",
    "collected_at": "2026-09-23T02:24:07.322037Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-22T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6",
    "reason": null,
    "released_at": null,
    "rows": 182,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:07.811565Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "3f412e082a5a268a46d5bf7ea17f1d7cf7e82662242d6feca3fa5c3ea69a81c6",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 43.90225974444445,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:07.900564Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "266754b347494b31424fe560f80641394efa70ed3ed16a4b3d759e4fa45e246d",
    "reason": null,
    "released_at": null,
    "rows": 242,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-23T02:24:08.135080Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "dc6f99fddd85e6142118299d3d7ce698234021ac9a65f109fc094eb26aabb04d",
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
    "collected_at": "2026-09-23T02:24:07.690564Z",
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
    "collected_at": "2026-09-23T02:24:07.690564Z",
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
    "collected_at": "2026-09-23T02:24:07.690564Z",
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
    "collected_at": "2026-09-23T02:24:07.690564Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-09-22T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-18T06:30:00+00:00'}, '30m': {'count': 0, 'last': None}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:266754b347494b31424fe560f80641394efa70ed3ed16a4b3d759e4fa45e246d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1w/technical",
  "bearish_alignment": null,
  "bullish_alignment": null,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 9989.885049542352,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4925
    ],
    "bottom_score": 0.65,
    "rsi": 61.010915030546485,
    "sma": [
      194085.0,
      188170.0,
      183559.16666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4912,
      4922
    ],
    "top_score": 0.4,
    "volume_ratio": 1.5190405469106698
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": null,
    "available": false,
    "bottom_confirmed": false,
    "bottom_features": {},
    "bottom_neckline": null,
    "bottom_pivots": [],
    "bottom_score": 0.0,
    "rsi": null,
    "sma": [],
    "top_confirmed": false,
    "top_features": {},
    "top_neckline": null,
    "top_pivots": [],
    "top_score": 0.0,
    "volume_ratio": null
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': 1.0}, 'negative_families': [], 'positive_families': ['semiconductor_export_momentum'], 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}, 'score': 1.0, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ba383c8a-8ec7-595c-9f8a-c978503c8d00",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
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
    "hypothesis_id": "ba383c8a-8ec7-595c-9f8a-c978503c8d00",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.405
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ba383c8a-8ec7-595c-9f8a-c978503c8d00",
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
    "hypothesis_id": "ba383c8a-8ec7-595c-9f8a-c978503c8d00",
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
    "hypothesis_id": "ba383c8a-8ec7-595c-9f8a-c978503c8d00",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.14864735291237754
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
    "hypothesis_id": "c53a0df0-76cd-52e3-914b-e1558dd4246b",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [1.0422733950608998, -0.7811837213599182, -0.26108967370098435] | {'down': 0.3421881627864008, 'flat': 0.24738910326299016, 'up': 0.410422733950609} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3421881627864008, 'flat': 0.24738910326299016, 'up': 0.410422733950609} | [2.8737980815540407, -2.1184022429426577, -0.7553958386113835] | {'down': 0.3210041403569742, 'flat': 0.23983514487687632, 'up': 0.43916071476614943} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3210041403569742, 'flat': 0.23983514487687632, 'up': 0.43916071476614943} | [2.908591237719965, -2.0939109526006305, -0.8146802851193208] | {'down': 0.3000650308309679, 'flat': 0.2316883420256831, 'up': 0.4682466271433491} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.3000650308309679, 'flat': 0.2316883420256831, 'up': 0.4682466271433491} | [2.4362009255633312, -1.7172988154268432, -0.7189021101365017] | {'down': 0.2828920426766995, 'flat': 0.2244993209243181, 'up': 0.4926086363989824} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.2828920426766995, 'flat': 0.2244993209243181, 'up': 0.4926086363989824} | [2.4350870607714734, -1.6848196392996562, -0.7502674214718119] | {'down': 0.2660438462837029, 'flat': 0.21699664670959998, 'up': 0.5169595070066971} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.2660438462837029, 'flat': 0.21699664670959998, 'up': 0.5169595070066971} | [-7.260206989421891, 8.237183713502855, -0.9769767240809607] | {'down': 0.34841568341873147, 'flat': 0.20722687946879037, 'up': 0.4443574371124782} |
| 6 | E10/causal | ['587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1w/technical'] | {'down': 0.34841568341873147, 'flat': 0.20722687946879037, 'up': 0.4443574371124782} | [1.5854227381738417, -1.4945822381465856, -0.09084050002726995] | {'down': 0.3334698610372656, 'flat': 0.20631847446851767, 'up': 0.46021166449421663} |
| 7 | E17/scenario | ['f1f18828-434f-58f5-bbf9-47d4c418a1de', '9a31cfe7-eb34-5727-9d0a-5ff5102800f3', '636421d8-8c49-5572-bcd1-ece79105fe81', 'd267e65e-8d0f-56d0-8d96-034ac37f8879'] | {'down': 0.3334698610372656, 'flat': 0.20631847446851767, 'up': 0.46021166449421663} | [0.28894003557893844, 2.5122234558474235, -2.8011634914263643] | {'down': 0.35859209559573985, 'flat': 0.17830683955425403, 'up': 0.463101064850006} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.35859209559573985, 'flat': 0.17830683955425403, 'up': 0.463101064850006} | [-1.693853992107508, -0.32970180486182055, 2.0235557969693314] | {'down': 0.35529507754712164, 'flat': 0.19854239752394734, 'up': 0.44616252492893094} |
| 9 | E13/history | [] | {'down': 0.35529507754712164, 'flat': 0.19854239752394734, 'up': 0.44616252492893094} | [0.0, 0.0, 0.0] | {'down': 0.35529507754712164, 'flat': 0.19854239752394734, 'up': 0.44616252492893094} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.35529507754712164, 'flat': 0.19854239752394734, 'up': 0.44616252492893094} | [-1.4180921768891852, -0.09210685698913257, 1.5101990338783122] | {'down': 0.3543740089772303, 'flat': 0.21364438786273046, 'up': 0.4319816031600391} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:266754b347494b31424fe560f80641394efa70ed3ed16a4b3d759e4fa45e246d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1m/technical",
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
      1027,
      1034
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  },
  "primary": "1d",
  "reflexivity_effect": 0.025,
  "regime_effect": 0.0375,
  "sell_liquidity": null,
  "wave": {
    "atr": 9989.885049542352,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4925
    ],
    "bottom_score": 0.65,
    "rsi": 61.010915030546485,
    "sma": [
      194085.0,
      188170.0,
      183559.16666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4912,
      4922
    ],
    "top_score": 0.4,
    "volume_ratio": 1.5190405469106698
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "0be30174-392f-5085-af00-d6ed550f93c1",
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
    "hypothesis_id": "0be30174-392f-5085-af00-d6ed550f93c1",
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
    "hypothesis_id": "0be30174-392f-5085-af00-d6ed550f93c1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.435375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0be30174-392f-5085-af00-d6ed550f93c1",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.435375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "0be30174-392f-5085-af00-d6ed550f93c1",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.17902235291237756
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
    "hypothesis_id": "655cb846-062c-55c3-9f90-153a052360d2",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.4871957654961456, -0.3660330843906878, -0.12116268110546335] | {'down': 0.3463396691560931, 'flat': 0.24878837318894537, 'up': 0.4048719576549615} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3463396691560931, 'flat': 0.24878837318894537, 'up': 0.4048719576549615} | [1.1917225746897686, -0.8888761678614743, -0.30284640682829433] | {'down': 0.33745090747747836, 'flat': 0.24575990912066242, 'up': 0.41678918340185916} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.33745090747747836, 'flat': 0.24575990912066242, 'up': 0.41678918340185916} | [1.2003965092733937, -0.8862968096368162, -0.314099699636583] | {'down': 0.3285879393811102, 'flat': 0.2426189121242966, 'up': 0.4287931484945931} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.3285879393811102, 'flat': 0.2426189121242966, 'up': 0.4287931484945931} | [1.9287762629630834, -1.405755226286154, -0.5230210366769156] | {'down': 0.31453038711824866, 'flat': 0.23738870175752744, 'up': 0.44808091112422394} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.31453038711824866, 'flat': 0.23738870175752744, 'up': 0.44808091112422394} | [1.941589317033543, -1.3931617700605137, -0.5484275469730349] | {'down': 0.3005987694176435, 'flat': 0.2319044262877971, 'up': 0.46749680429455936} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.3005987694176435, 'flat': 0.2319044262877971, 'up': 0.46749680429455936} | [-5.403216724986903, 6.3985844092211694, -0.9953676842342662] | {'down': 0.3645846135098552, 'flat': 0.22195074944545443, 'up': 0.41346463704469033} |
| 6 | E10/causal | ['587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1m/technical'] | {'down': 0.3645846135098552, 'flat': 0.22195074944545443, 'up': 0.41346463704469033} | [2.6915936468220436, -2.577953690075546, -0.11363995674650573] | {'down': 0.33880507660909975, 'flat': 0.22081434987798937, 'up': 0.44038057351291077} |
| 7 | E17/scenario | ['dd7b5b44-14b7-526b-8abf-9889abbb6ea8', '9e6c9cfe-1169-5b2d-a181-2be6ce417581', '0bd55e1e-4645-52c9-87ca-29e58f3418b5', '87cfaacf-f692-5469-b39f-50029f884db4'] | {'down': 0.33880507660909975, 'flat': 0.22081434987798937, 'up': 0.44038057351291077} | [0.47312762539923336, 2.861943983732557, -3.3350716091317762] | {'down': 0.3674245164464253, 'flat': 0.1874636337866716, 'up': 0.4451118497669031} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3674245164464253, 'flat': 0.1874636337866716, 'up': 0.4451118497669031} | [-1.4662287762176651, -0.447183191283701, 1.9134119675013634] | {'down': 0.3629526845335883, 'flat': 0.20659775346168524, 'up': 0.43044956200472645} |
| 9 | E13/history | [] | {'down': 0.3629526845335883, 'flat': 0.20659775346168524, 'up': 0.43044956200472645} | [0.0, 0.0, 0.0] | {'down': 0.3629526845335883, 'flat': 0.20659775346168524, 'up': 0.43044956200472645} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3629526845335883, 'flat': 0.20659775346168524, 'up': 0.43044956200472645} | [-1.210030082369301, -0.22674633089893592, 1.436776413268226] | {'down': 0.36068522122459895, 'flat': 0.2209655175943675, 'up': 0.41834926118103344} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'd9a4c1432ffdbdc31fde954c6bd2019555763ad3d09c3a200c0bc9af3328328f'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:266754b347494b31424fe560f80641394efa70ed3ed16a4b3d759e4fa45e246d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d7dc7f3ffdd6fd80c6d6a34b93fab0602d141bfb43464f9bf3ac0cbdbeb257c7#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f830fd1577fa36b8a862dab4f447f04d7fe369877f86fdb6180a73449997d746#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:165ecbb56a2ce737905962cf2a98f5bcb3b67ce85305345e019135f98d071ea6#us_10y_yield@2026-09-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1y/technical",
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
      1027,
      1034
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '587f3e1c-5b89-52b5-9756-ff34ddf6c15b/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "89c96e26-5b08-5e9b-9a62-d96ed277eb8f",
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
    "hypothesis_id": "89c96e26-5b08-5e9b-9a62-d96ed277eb8f",
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
    "hypothesis_id": "89c96e26-5b08-5e9b-9a62-d96ed277eb8f",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.39285000000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "89c96e26-5b08-5e9b-9a62-d96ed277eb8f",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.39285000000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "89c96e26-5b08-5e9b-9a62-d96ed277eb8f",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.13649735291237758
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
    "hypothesis_id": "67088fa5-b491-5ad9-9941-e8e619574cbd",
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
