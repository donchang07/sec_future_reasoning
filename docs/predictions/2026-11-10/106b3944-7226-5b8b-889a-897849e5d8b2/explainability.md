# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 106b3944-7226-5b8b-889a-897849e5d8b2
Cutoff / prediction: 2026-11-09T22:00:13.000308+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-11-09T06:30:00+00:00', 'source_refs': ['raw:b46e15d0dc4c86fdbdca35cc6ac302620acb3f2fa855ec3ed8655a13fc535e79'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 150900.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 36.2737% | 41.6773% | 22.0490% | 5.0731% | 35.0000% | 30.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 36.9969% | 40.5868% | 22.4163% | 2.5558% | 0.0000% | 20.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 36.0376% / 41.8975% / 22.0649% | 36.2737% / 41.6773% / 22.0490% | [0.23611882346305513, -0.22024467612066223, -0.01587414734239012] |
| 1m | 37.6717% / 39.8846% / 22.4436% | 36.9969% / 40.5868% / 22.4163% | [-0.67484461413852, 0.7021820607871099, -0.027337446648595387] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503611196666668,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-09T22:00:12.197642Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b46e15d0dc4c86fdbdca35cc6ac302620acb3f2fa855ec3ed8655a13fc535e79",
    "reason": null,
    "released_at": null,
    "rows": 253,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503611196666668,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-09T22:00:12.500468Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503611196666668,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-09T22:00:12.813274Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-11-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 1.5036111966666665,
    "authority": "official_original",
    "collected_at": "2026-11-09T22:00:12.255408Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-11-09T20:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089",
    "reason": null,
    "released_at": null,
    "rows": 215,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-09T22:00:12.762555Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "b5ac8ffb1838a704e2e07dc29f9cde495906587352562ead1105d25d1f40f664",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50361119666667,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-09T22:00:12.799837Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-11-06T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "544ce216bbdce876d590fe829b088dad7d8d8451faa6f7b1527e9ab95a4e3215",
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
    "collected_at": "2026-11-09T22:00:12.998801Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f84d2028772506fb69584bbcd0cb626b4f3ef37f529d1dbfce9051222eca1a2f",
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
    "collected_at": "2026-11-09T22:00:12.762555Z",
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
    "collected_at": "2026-11-09T22:00:12.762555Z",
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
    "collected_at": "2026-11-09T22:00:12.762555Z",
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
    "collected_at": "2026-11-09T22:00:12.762555Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-11-09T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-11-06T06:30:00+00:00'}, '30m': {'count': 253, 'last': '2026-11-09T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:544ce216bbdce876d590fe829b088dad7d8d8451faa6f7b1527e9ab95a4e3215'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-11-02T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "106b3944-7226-5b8b-889a-897849e5d8b2/1w/technical",
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
    "atr": 11641.356298062861,
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
    "bottom_neckline": 197000.0,
    "bottom_pivots": [
      4919,
      4924
    ],
    "bottom_score": 0.0,
    "rsi": 35.65079968290931,
    "sma": [
      169175.0,
      186126.66666666666,
      190325.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 159000.0,
    "top_pivots": [
      4917,
      4923
    ],
    "top_score": 0.2,
    "volume_ratio": 0.7032549507855004
  },
  "primary": "30m",
  "reflexivity_effect": 0.004999999999999994,
  "regime_effect": 0.007499999999999989,
  "sell_liquidity": null,
  "wave": {
    "atr": 2668.4036136026684,
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
    "bottom_neckline": 154700.0,
    "bottom_pivots": [
      236,
      243
    ],
    "bottom_score": 0.35,
    "rsi": 38.07390936057594,
    "sma": [
      153235.0,
      161535.0,
      169954.58333333334
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
    "top_neckline": 148100.0,
    "top_pivots": [
      233,
      245
    ],
    "top_score": 0.30000000000000004,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '106b3944-7226-5b8b-889a-897849e5d8b2/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.004999999999999994, 'regime_effect': 0.007499999999999989}
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
    "hypothesis_id": "6d191f96-294e-5573-831a-5428c3c48298",
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
    "hypothesis_id": "6d191f96-294e-5573-831a-5428c3c48298",
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
    "hypothesis_id": "679de00a-635e-5499-a441-38bde251b0e7",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7128
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "679de00a-635e-5499-a441-38bde251b0e7",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.18460170428072437
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "679de00a-635e-5499-a441-38bde251b0e7",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.13718516446206064
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.991254786659751, 1.2424672000203474, -0.25121241336060196] | {'down': 0.36242467200020345, 'flat': 0.24748787586639398, 'up': 0.3900874521334025} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.36242467200020345, 'flat': 0.24748787586639398, 'up': 0.3900874521334025} | [-0.7383263265904494, 0.9346858013660753, -0.19635947477562865] | {'down': 0.3717715300138642, 'flat': 0.2455242811186377, 'up': 0.382704188867498} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3717715300138642, 'flat': 0.2455242811186377, 'up': 0.382704188867498} | [2.3561182466783515, -1.8099511925868839, -0.5461670540914509] | {'down': 0.35367201808799537, 'flat': 0.24006261057772318, 'up': 0.40626537133428153} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.35367201808799537, 'flat': 0.24006261057772318, 'up': 0.40626537133428153} | [2.3956304919422857, -1.8041715913540646, -0.5914589005882265] | {'down': 0.3356303021744547, 'flat': 0.23414802157184092, 'up': 0.4302216762537044} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3356303021744547, 'flat': 0.23414802157184092, 'up': 0.4302216762537044} | [-6.618889040712056, 8.21412660387057, -1.5952375631585163] | {'down': 0.4177715682131604, 'flat': 0.21819564594025576, 'up': 0.36403278584658383} |
| 5 | E10/causal | ['106b3944-7226-5b8b-889a-897849e5d8b2/1w/technical'] | {'down': 0.4177715682131604, 'flat': 0.21819564594025576, 'up': 0.36403278584658383} | [-0.3157548077851957, 0.32599406663885167, -0.010239258853653177] | {'down': 0.42103150887954893, 'flat': 0.21809325335171922, 'up': 0.36087523776873187} |
| 6 | E17/scenario | ['a725b64d-8a8b-5158-bef5-0009a21fd41f', '53318a5f-0a7d-50d3-b5eb-b97a85450ddd', 'e1e1af0a-b775-5486-b088-e198c14a88c1', 'bc2a5909-a374-57b6-b484-0777a13c5752'] | {'down': 0.42103150887954893, 'flat': 0.21809325335171922, 'up': 0.36087523776873187} | [0.9285462297817626, 2.1939103110898417, -3.1224565408715987] | {'down': 0.44297061199044735, 'flat': 0.18686868794300324, 'up': 0.3701607000665495} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.44297061199044735, 'flat': 0.18686868794300324, 'up': 0.3701607000665495} | [-0.4832141139781809, -1.4385573872022939, 1.9217715011804692] | {'down': 0.4285850381184244, 'flat': 0.20608640295480793, 'up': 0.3653285589267677} |
| 8 | E13/history | [] | {'down': 0.4285850381184244, 'flat': 0.20608640295480793, 'up': 0.3653285589267677} | [0.0, 0.0, 0.0] | {'down': 0.4285850381184244, 'flat': 0.20608640295480793, 'up': 0.3653285589267677} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4285850381184244, 'flat': 0.20608640295480793, 'up': 0.3653285589267677} | [-0.259126792238934, -1.1812116920091709, 1.4403384842481075] | {'down': 0.4167729211983327, 'flat': 0.220489787797289, 'up': 0.36273729100437835} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:544ce216bbdce876d590fe829b088dad7d8d8451faa6f7b1527e9ab95a4e3215'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-11-02T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "106b3944-7226-5b8b-889a-897849e5d8b2/1m/technical",
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
    "atr": 25580.499220848895,
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
      1027,
      1038
    ],
    "bottom_score": 0.0,
    "rsi": 41.438831579365605,
    "sma": [
      188895.0,
      143664.16666666666,
      97033.75
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
      1030,
      1035
    ],
    "top_score": 0.4,
    "volume_ratio": 1.0160682793524498
  },
  "primary": "1d",
  "reflexivity_effect": -0.020000000000000004,
  "regime_effect": -0.03,
  "sell_liquidity": null,
  "wave": {
    "atr": 11641.356298062861,
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
    "bottom_neckline": 197000.0,
    "bottom_pivots": [
      4919,
      4924
    ],
    "bottom_score": 0.0,
    "rsi": 35.65079968290931,
    "sma": [
      169175.0,
      186126.66666666666,
      190325.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 159000.0,
    "top_pivots": [
      4917,
      4923
    ],
    "top_score": 0.2,
    "volume_ratio": 0.7032549507855004
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '106b3944-7226-5b8b-889a-897849e5d8b2/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "54901336-14f0-5e1f-a2d7-ab3e40eaebab",
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
    "hypothesis_id": "54901336-14f0-5e1f-a2d7-ab3e40eaebab",
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
    "hypothesis_id": "ad3c2c25-9cd7-5314-94b8-bb1b7fa545e8",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7128
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ad3c2c25-9cd7-5314-94b8-bb1b7fa545e8",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.23016420428072432
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ad3c2c25-9cd7-5314-94b8-bb1b7fa545e8",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.18274766446206064
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.48024734146258075, 0.6001719821712104, -0.11992464070863518] | {'down': 0.3560017198217121, 'flat': 0.24880075359291365, 'up': 0.3951975265853742} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3560017198217121, 'flat': 0.24880075359291365, 'up': 0.3951975265853742} | [-0.38183509018703266, 0.4795784409599768, -0.09774335077294694] | {'down': 0.36079750423131185, 'flat': 0.24782332008518418, 'up': 0.3913791756835039} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36079750423131185, 'flat': 0.24782332008518418, 'up': 0.3913791756835039} | [1.8906707957691282, -1.4336172426966998, -0.4570535530724146] | {'down': 0.34646133180434485, 'flat': 0.24325278455446003, 'up': 0.41028588364119517} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.34646133180434485, 'flat': 0.24325278455446003, 'up': 0.41028588364119517} | [1.9147009935924775, -1.4287139120080228, -0.48598708158446857] | {'down': 0.3321741926842646, 'flat': 0.23839291373861535, 'up': 0.42943289357711995} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3321741926842646, 'flat': 0.23839291373861535, 'up': 0.42943289357711995} | [-4.920756644547353, 6.068213440870246, -1.1474567963228821] | {'down': 0.3928563270929671, 'flat': 0.22691834577538653, 'up': 0.3802253271316464} |
| 5 | E10/causal | ['106b3944-7226-5b8b-889a-897849e5d8b2/1m/technical'] | {'down': 0.3928563270929671, 'flat': 0.22691834577538653, 'up': 0.3802253271316464} | [-1.4173139597507267, 1.4399008968717653, -0.02258693712104687] | {'down': 0.40725533606168474, 'flat': 0.22669247640417606, 'up': 0.36605218753413915} |
| 6 | E17/scenario | ['4afcff62-a0e8-5244-87fb-69053b771283', '70be6a88-4ee5-5994-b4db-189fc15aece0', 'ef0c390b-97d4-50af-b77f-21e47a8de969', 'fccf3ff2-ea85-5bc5-8abe-e9c932e9f754'] | {'down': 0.40725533606168474, 'flat': 0.22669247640417606, 'up': 0.36605218753413915} | [1.4009271806544765, 2.1191486823939565, -3.520075863048433] | {'down': 0.4284468228856243, 'flat': 0.19149171777369173, 'up': 0.3800614593406839} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4284468228856243, 'flat': 0.19149171777369173, 'up': 0.3800614593406839} | [-0.6146973952308732, -1.251195356516438, 1.8658927517473085] | {'down': 0.4159348693204599, 'flat': 0.2101506452911648, 'up': 0.3739144853883752} |
| 8 | E13/history | [] | {'down': 0.4159348693204599, 'flat': 0.2101506452911648, 'up': 0.3739144853883752} | [0.0, 0.0, 0.0] | {'down': 0.4159348693204599, 'flat': 0.2101506452911648, 'up': 0.3739144853883752} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4159348693204599, 'flat': 0.2101506452911648, 'up': 0.3739144853883752} | [-0.3945687810284815, -1.0066568602054016, 1.4012256412338941] | {'down': 0.4058683007184059, 'flat': 0.22416290170350375, 'up': 0.36996879757809037} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '98f473b8219dbdbf3e2b6248e14ab86f21486b315f9fa04410ec1403a583c2bd'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:544ce216bbdce876d590fe829b088dad7d8d8451faa6f7b1527e9ab95a4e3215'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_rsi_14@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_trend_alignment@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#preferred_volume_z@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:2ec8b2d7f75c48e52951f8871bc0c0da32ad7ec85d3ccff9675822dc2c9ec380#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:f54e68efabad854342dcd63c00dddf9498185582b3d31afb800e63ac90d790f0#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f6d7c9a23468909a6fbefea1d49a9b6b7bfcf7f07b6d1b80904c8e6c17758089#us_10y_yield@2026-11-02T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "106b3944-7226-5b8b-889a-897849e5d8b2/1y/technical",
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
  "reflexivity_effect": -0.04000000000000001,
  "regime_effect": -0.06,
  "sell_liquidity": null,
  "wave": {
    "atr": 25580.499220848895,
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
      1027,
      1038
    ],
    "bottom_score": 0.0,
    "rsi": 41.438831579365605,
    "sma": [
      188895.0,
      143664.16666666666,
      97033.75
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
      1030,
      1035
    ],
    "top_score": 0.4,
    "volume_ratio": 1.0160682793524498
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '106b3944-7226-5b8b-889a-897849e5d8b2/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.04000000000000001, 'regime_effect': -0.06}
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
    "hypothesis_id": "85c6116f-dd4a-5702-b380-2543ee857041",
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
    "hypothesis_id": "85c6116f-dd4a-5702-b380-2543ee857041",
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
    "hypothesis_id": "3317ff9b-dd40-502a-8839-32f6559c26f1",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7128
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "3317ff9b-dd40-502a-8839-32f6559c26f1",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.26661420428072435
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "3317ff9b-dd40-502a-8839-32f6559c26f1",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.2191976644620606
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
