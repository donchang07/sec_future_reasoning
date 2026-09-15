# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 5dde8aff-37b8-5579-9565-4ccb23ca5d52
Cutoff / prediction: 2026-09-15T22:00:40.751606+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-15T06:30:00+00:00', 'source_refs': ['raw:7bc266de850a746cf1692a4de2b3e629adbadb92f60f0f71af322d7ad22c1e04'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 187100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 37.0468% | 40.7895% | 22.1637% | 4.3844% | 0.0000% | 0.0000% | 0.13333333333333333/0.2666666666666667 | None/None | WAIT |
| 1m | 37.4909% | 40.0597% | 22.4494% | 3.5269% | 30.0000% | 45.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 37.0468% / 40.7895% / 22.1637% | 37.0468% / 40.7895% / 22.1637% | [0.0, 0.0, 0.0] |
| 1m | 37.9977% / 39.5405% / 22.4618% | 37.4909% / 40.0597% / 22.4494% | [-0.5068245044853981, 0.5192260099046109, -0.012401505419210035] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.511319890555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-15T22:00:39.768528Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7bc266de850a746cf1692a4de2b3e629adbadb92f60f0f71af322d7ad22c1e04",
    "reason": null,
    "released_at": null,
    "rows": 253,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.511319890555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-15T22:00:40.255367Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.511319890555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-15T22:00:40.298223Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5113198905555554,
    "authority": "official_original",
    "collected_at": "2026-09-15T22:00:39.817560Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-15T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e",
    "reason": null,
    "released_at": null,
    "rows": 177,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-15T22:00:40.313600Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "5835357f32c02e3c37da93de7a00d4f984c77391161955fbaff40dc9c063498e",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.511319890555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-15T22:00:40.344076Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "bb1eeb442c56fdd1a2de4e97ea82b433f40a28b3680fa53230cccd80c75d356c",
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
    "collected_at": "2026-09-15T22:00:40.750605Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "cc0feb631b8b8496de8b5ad8370ae7cf21f448528fe06515bec72d8b98df11cf",
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
    "collected_at": "2026-09-15T22:00:40.299212Z",
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
    "collected_at": "2026-09-15T22:00:40.299212Z",
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
    "collected_at": "2026-09-15T22:00:40.299212Z",
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
    "collected_at": "2026-09-15T22:00:40.299212Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-15T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 253, 'last': '2026-09-15T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:bb1eeb442c56fdd1a2de4e97ea82b433f40a28b3680fa53230cccd80c75d356c'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "5dde8aff-37b8-5579-9565-4ccb23ca5d52/1w/technical",
  "bearish_alignment": 0.2666666666666667,
  "bullish_alignment": 0.13333333333333333,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 10621.080755320103,
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
      4916,
      4923
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 48.36473335872943,
    "sma": [
      191695.0,
      189703.33333333334,
      180541.66666666666
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
    "top_neckline": 179200.0,
    "top_pivots": [
      4918,
      4928
    ],
    "top_score": 0.45000000000000007,
    "volume_ratio": 0.988194152400775
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 1798.0997699568136,
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
    "bottom_neckline": 191700.0,
    "bottom_pivots": [
      240,
      250
    ],
    "bottom_score": 0.0,
    "rsi": 42.65141963185136,
    "sma": [
      187630.0,
      192599.16666666666,
      192197.08333333334
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
      233,
      245
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '5dde8aff-37b8-5579-9565-4ccb23ca5d52/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "4e25791f-4246-5e49-973d-37e5e3341d13",
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
    "hypothesis_id": "4e25791f-4246-5e49-973d-37e5e3341d13",
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
    "hypothesis_id": "a77ffbdb-4bb7-56dc-80f0-3dfc8ec93741",
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
    "hypothesis_id": "a77ffbdb-4bb7-56dc-80f0-3dfc8ec93741",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.02207609965715268
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.11837238311399045, 0.14761940693492903, -0.029247023820935802] | {'down': 0.35147619406934927, 'flat': 0.24970752976179064, 'up': 0.3988162761688601} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.35147619406934927, 'flat': 0.24970752976179064, 'up': 0.3988162761688601} | [2.375574958529425, -1.774118582756079, -0.6014563757733488] | {'down': 0.3337350082417885, 'flat': 0.24369296600405715, 'up': 0.42257202575415437} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3337350082417885, 'flat': 0.24369296600405715, 'up': 0.42257202575415437} | [2.407407964298308, -1.7621863437777385, -0.6452216205205724] | {'down': 0.3161131448040111, 'flat': 0.23724074979885143, 'up': 0.44664610539713745} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.3161131448040111, 'flat': 0.23724074979885143, 'up': 0.44664610539713745} | [-7.491587278267548, 9.18256058595635, -1.690973307688809] | {'down': 0.4079387506635746, 'flat': 0.22033101672196334, 'up': 0.371730232614462} |
| 4 | E10/causal | ['5dde8aff-37b8-5579-9565-4ccb23ca5d52/1w/technical'] | {'down': 0.4079387506635746, 'flat': 0.22033101672196334, 'up': 0.371730232614462} | [-0.03498926335846475, 0.03572110195882994, -0.0007318386003457578] | {'down': 0.4082959616831629, 'flat': 0.22032369833595988, 'up': 0.3713803399808773} |
| 5 | E17/scenario | ['aad687e6-3513-5f6f-add9-8cf3cdd5164b', '89f87351-6e7e-594f-b47d-32bfd170030d', 'b31a7cde-a5ec-5e55-8ee1-0d0b2131e2e0', '9afd2f5f-8f51-5ab8-95b2-fae9cc5b50be'] | {'down': 0.4082959616831629, 'flat': 0.22032369833595988, 'up': 0.3713803399808773} | [0.9362541966723092, 2.303203050101782, -3.2394572467740854] | {'down': 0.4313279921841807, 'flat': 0.18792912586821903, 'up': 0.3807428819476004} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4313279921841807, 'flat': 0.18792912586821903, 'up': 0.3807428819476004} | [-0.6341565105391245, -1.3107897612343822, 1.9449462717734982] | {'down': 0.4182200945718369, 'flat': 0.207378588585954, 'up': 0.3744013168422092} |
| 7 | E13/history | [] | {'down': 0.4182200945718369, 'flat': 0.207378588585954, 'up': 0.3744013168422092} | [0.0, 0.0, 0.0] | {'down': 0.4182200945718369, 'flat': 0.207378588585954, 'up': 0.3744013168422092} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.4182200945718369, 'flat': 0.207378588585954, 'up': 0.3744013168422092} | [-0.3933581438124001, -1.0325226461159687, 1.425880789928355] | {'down': 0.4078948681106772, 'flat': 0.22163739648523756, 'up': 0.3704677354040852} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:bb1eeb442c56fdd1a2de4e97ea82b433f40a28b3680fa53230cccd80c75d356c'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "5dde8aff-37b8-5579-9565-4ccb23ca5d52/1m/technical",
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
  "reflexivity_effect": -0.015000000000000003,
  "regime_effect": -0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 10621.080755320103,
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
      4916,
      4923
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 48.36473335872943,
    "sma": [
      191695.0,
      189703.33333333334,
      180541.66666666666
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
    "top_neckline": 179200.0,
    "top_pivots": [
      4918,
      4928
    ],
    "top_score": 0.45000000000000007,
    "volume_ratio": 0.988194152400775
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '5dde8aff-37b8-5579-9565-4ccb23ca5d52/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.015000000000000003, 'regime_effect': -0.022500000000000003}
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
    "hypothesis_id": "1c3136a8-2d36-5389-9ad5-6e72ee023ab4",
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
    "hypothesis_id": "1c3136a8-2d36-5389-9ad5-6e72ee023ab4",
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
    "hypothesis_id": "41a4e3ca-0c15-5686-8d5a-bd8c276f1cfa",
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
    "hypothesis_id": "41a4e3ca-0c15-5686-8d5a-bd8c276f1cfa",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.07675109965715268
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.1600555915895363, 0.19965023895492373, -0.03959464736539853] | {'down': 0.3519965023895492, 'flat': 0.24960405352634601, 'up': 0.39839944408410466} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.3519965023895492, 'flat': 0.24960405352634601, 'up': 0.39839944408410466} | [1.897204760896648, -1.4208055956946797, -0.47639916520194614] | {'down': 0.3377884464326024, 'flat': 0.24484006187432655, 'up': 0.41737149169307114} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3377884464326024, 'flat': 0.24484006187432655, 'up': 0.41737149169307114} | [1.9191029440178253, -1.4141999544676986, -0.5049029895501322] | {'down': 0.32364644688792543, 'flat': 0.23979103197882523, 'up': 0.4365625211332494} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.32364644688792543, 'flat': 0.23979103197882523, 'up': 0.4365625211332494} | [-5.582461279070134, 6.856166344244424, -1.2737050651743076] | {'down': 0.3922081103303697, 'flat': 0.22705398132708215, 'up': 0.38073790834254806} |
| 4 | E10/causal | ['5dde8aff-37b8-5579-9565-4ccb23ca5d52/1m/technical'] | {'down': 0.3922081103303697, 'flat': 0.22705398132708215, 'up': 0.38073790834254806} | [-0.6976712249234795, 0.7052915116807279, -0.007620286757231698] | {'down': 0.39926102544717695, 'flat': 0.22697777845950984, 'up': 0.37376119609331326} |
| 5 | E17/scenario | ['4564f710-6aba-54d1-bcc3-df630e4a1e55', '25d0c0a3-73f4-5c89-93fc-5ecc1c5f1280', '0cfeef93-dc49-51e5-b4b1-cd45eb0629cc', '9d559bf6-6a03-5cd4-8d9e-1cf291020bbb'] | {'down': 0.39926102544717695, 'flat': 0.22697777845950984, 'up': 0.37376119609331326} | [1.31061895725742, 2.2324361410837765, -3.5430550983412026] | {'down': 0.4215853868580147, 'flat': 0.19154722747609781, 'up': 0.38686738566588746} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4215853868580147, 'flat': 0.19154722747609781, 'up': 0.38686738566588746} | [-0.7166786164526151, -1.1814603390431055, 1.8981389554957233] | {'down': 0.40977078346758367, 'flat': 0.21052861703105505, 'up': 0.3797005995013613} |
| 7 | E13/history | [] | {'down': 0.40977078346758367, 'flat': 0.21052861703105505, 'up': 0.3797005995013613} | [0.0, 0.0, 0.0] | {'down': 0.40977078346758367, 'flat': 0.21052861703105505, 'up': 0.3797005995013613} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.40977078346758367, 'flat': 0.21052861703105505, 'up': 0.3797005995013613} | [-0.47916390550379884, -0.9173339001121494, 1.3964978056159427] | {'down': 0.40059744446646217, 'flat': 0.22449359508721448, 'up': 0.3749089604463233} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '6e9a1f93d19d44d633f463ebe434a5d5ecc8f99e88d5521855cbf3bf313aacb0'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:bb1eeb442c56fdd1a2de4e97ea82b433f40a28b3680fa53230cccd80c75d356c'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e18ff673e6ed4fde592c7caf817e4213818cbc0669e3c3e3e871274fb604d5cf#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e677b8ba7b311d6afa89aed7c5c7fa454b038ee104c58011cb326d599c1bf08b#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:b5f62197452dd5157b7eb8c4c9368af5335e026b3770c49a27c3d5a55f35d99e#us_10y_yield@2026-09-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "5dde8aff-37b8-5579-9565-4ccb23ca5d52/1y/technical",
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
Feedback applied once: {'batch_id': '5dde8aff-37b8-5579-9565-4ccb23ca5d52/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "5ae588cc-0fdc-5727-a076-ebb4879a6554",
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
    "hypothesis_id": "5ae588cc-0fdc-5727-a076-ebb4879a6554",
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
    "hypothesis_id": "b3706dda-4ca4-5599-b197-a1a16eaaf08c",
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
    "hypothesis_id": "b3706dda-4ca4-5599-b197-a1a16eaaf08c",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.058526099657152685
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
