# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 9b76ec69-491c-50e1-8c43-6049261a8d2a
Cutoff / prediction: 2026-09-12T22:00:10.974469+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-11T06:30:00+00:00', 'source_refs': ['raw:7af8a36c950503df102535aa1bb67571566d5bf32311464a1d6be1297d813d61'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 193300.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 43.4432% | 35.2484% | 21.3084% | 6.1644% | 10.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 42.2178% | 35.8367% | 21.9456% | 4.8780% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 42.9712% / 35.7069% / 21.3219% | 43.4432% / 35.2484% / 21.3084% | [0.47194371197663565, -0.45848504227065656, -0.01345866970597076] |
| 1m | 41.3203% / 36.6801% / 21.9997% | 42.2178% / 35.8367% / 21.9456% | [0.8974786625357445, -0.8433925362647698, -0.05408612627097742] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 39.503048463611115,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-12T22:00:10.004316Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7af8a36c950503df102535aa1bb67571566d5bf32311464a1d6be1297d813d61",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.503048463611115,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-12T22:00:10.485875Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.503048463611115,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-12T22:00:10.414615Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf",
    "reason": null,
    "released_at": null,
    "rows": 4936,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 26.50304846361111,
    "authority": "official_original",
    "collected_at": "2026-09-12T22:00:10.092498Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-11T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c",
    "reason": null,
    "released_at": null,
    "rows": 175,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-12T22:00:10.504520Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "87974b56c5143c1e52dd9e99b27968c4f44a257fd3891f13cd83128b003170a9",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503048463611115,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-12T22:00:10.594021Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "0504ca3831afec814ba8de7225dd1e4e1cb7f9d3652a626bb295a31d8b7556f6",
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
    "collected_at": "2026-09-12T22:00:10.973463Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "25047fd91e28e07a6ce27709bcb273164a9b0c63c75c9e9b3bb83d8f10893909",
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
    "collected_at": "2026-09-12T22:00:10.486877Z",
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
    "collected_at": "2026-09-12T22:00:10.486877Z",
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
    "collected_at": "2026-09-12T22:00:10.486877Z",
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
    "collected_at": "2026-09-12T22:00:10.486877Z",
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
Bar boundaries: {'1d': {'count': 4934, 'last': '2026-09-11T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-09-11T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0504ca3831afec814ba8de7225dd1e4e1cb7f9d3652a626bb295a31d8b7556f6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "9b76ec69-491c-50e1-8c43-6049261a8d2a/1w/technical",
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
    "atr": 10868.827384868286,
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
      4920,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
    "top_neckline": 172700.0,
    "top_pivots": [
      4915,
      4922
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  },
  "primary": "30m",
  "reflexivity_effect": 0.010000000000000002,
  "regime_effect": 0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1413.3919341041053,
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
    "bottom_neckline": 193300.0,
    "bottom_pivots": [
      254,
      259
    ],
    "bottom_score": 0.1,
    "rsi": 41.95290413339034,
    "sma": [
      195142.5,
      197382.5,
      192065.83333333334
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
    "top_neckline": 191000.0,
    "top_pivots": [
      251,
      261
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '9b76ec69-491c-50e1-8c43-6049261a8d2a/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.010000000000000002, 'regime_effect': 0.015}
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
    "hypothesis_id": "1e09667b-527d-5a90-a515-c20634123c41",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.625725
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1e09667b-527d-5a90-a515-c20634123c41",
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
    "hypothesis_id": "1e09667b-527d-5a90-a515-c20634123c41",
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
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1e09667b-527d-5a90-a515-c20634123c41",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.048898003970429184
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
    "hypothesis_id": "bb39872b-db06-5d0b-8995-8bfa88917d63",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.34200455876902125, -0.25711270967664346, -0.0848918490923889] | {'down': 0.34742887290323354, 'flat': 0.2491510815090761, 'up': 0.40342004558769023} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34742887290323354, 'flat': 0.2491510815090761, 'up': 0.40342004558769023} | [4.440116017079726, -3.27106676797726, -1.1690492491024496] | {'down': 0.31471820522346095, 'flat': 0.23746058901805162, 'up': 0.4478212057584875} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.31471820522346095, 'flat': 0.23746058901805162, 'up': 0.4478212057584875} | [3.6461911310625537, -2.599378882126918, -1.0468122489356495] | {'down': 0.28872441640219176, 'flat': 0.22699246652869512, 'up': 0.48428311706911303} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.28872441640219176, 'flat': 0.22699246652869512, 'up': 0.48428311706911303} | [3.6526032519169584, -2.5315931321759466, -1.1210101197410034] | {'down': 0.2634084850804323, 'flat': 0.2157823653312851, 'up': 0.5208091495882826} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2634084850804323, 'flat': 0.2157823653312851, 'up': 0.5208091495882826} | [-7.255912574272482, 8.2005587961127, -0.9446462218402257] | {'down': 0.3454140730415593, 'flat': 0.20633590311288283, 'up': 0.4482500238455578} |
| 5 | E10/causal | ['9b76ec69-491c-50e1-8c43-6049261a8d2a/1w/technical'] | {'down': 0.3454140730415593, 'flat': 0.20633590311288283, 'up': 0.4482500238455578} | [1.518820987607744, -1.4274044835980826, -0.09141650400966428] | {'down': 0.3311400282055785, 'flat': 0.2054217380727862, 'up': 0.46343823372163523} |
| 6 | E17/scenario | ['258c63ad-b08d-5d93-ac3e-1ef748a06ef8', '741d357a-db57-5545-874a-5a0dff6a2599', '5bb8f151-9416-5ad4-9124-d8f480c6ac58', 'cea3d40e-1461-5e1c-9718-fb91648d85a7'] | {'down': 0.3311400282055785, 'flat': 0.2054217380727862, 'up': 0.46343823372163523} | [0.242973332712354, 2.48047664178071, -2.7234499744930476] | {'down': 0.3559447946233856, 'flat': 0.1781872383278557, 'up': 0.46586796704875877} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3559447946233856, 'flat': 0.1781872383278557, 'up': 0.46586796704875877} | [-1.6854293592642955, -0.28754763676301365, 1.9729769960273091] | {'down': 0.35306931825575544, 'flat': 0.1979170082881288, 'up': 0.4490136734561158} |
| 8 | E13/history | [] | {'down': 0.35306931825575544, 'flat': 0.1979170082881288, 'up': 0.4490136734561158} | [0.0, 0.0, 0.0] | {'down': 0.35306931825575544, 'flat': 0.1979170082881288, 'up': 0.4490136734561158} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.35306931825575544, 'flat': 0.1979170082881288, 'up': 0.4490136734561158} | [-1.4581756373049315, -0.05852642285856802, 1.516702060163491] | {'down': 0.35248405402716976, 'flat': 0.21308402888976372, 'up': 0.4344319170830665} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0504ca3831afec814ba8de7225dd1e4e1cb7f9d3652a626bb295a31d8b7556f6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "9b76ec69-491c-50e1-8c43-6049261a8d2a/1m/technical",
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
      1029,
      1036
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
      1031,
      1039
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  },
  "primary": "1d",
  "reflexivity_effect": 0.02500000000000001,
  "regime_effect": 0.037500000000000006,
  "sell_liquidity": null,
  "wave": {
    "atr": 10868.827384868286,
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
      4920,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
    "top_neckline": 172700.0,
    "top_pivots": [
      4915,
      4922
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '9b76ec69-491c-50e1-8c43-6049261a8d2a/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'regime_effect': 0.037500000000000006}
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
    "hypothesis_id": "91abf5e3-841b-599d-a12a-6253b5381f02",
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
    "hypothesis_id": "91abf5e3-841b-599d-a12a-6253b5381f02",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "91abf5e3-841b-599d-a12a-6253b5381f02",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6530625
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "91abf5e3-841b-599d-a12a-6253b5381f02",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.07623550397042919
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
    "hypothesis_id": "f8e09b8c-a9c8-5f0c-9b9f-0737bde9f3d8",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.20725627745850628, -0.15590315993723736, -0.05135311752127447] | {'down': 0.3484409684006276, 'flat': 0.24948646882478726, 'up': 0.4020725627745851} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3484409684006276, 'flat': 0.24948646882478726, 'up': 0.4020725627745851} | [1.7876741721143563, -1.3331984168400535, -0.4544757552742945] | {'down': 0.33510898423222707, 'flat': 0.2449417112720443, 'up': 0.41994930449572865} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33510898423222707, 'flat': 0.2449417112720443, 'up': 0.41994930449572865} | [2.88754045825394, -2.111629179476843, -0.7759112787771028] | {'down': 0.31399269243745864, 'flat': 0.23718259848427328, 'up': 0.44882470907826805} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.31399269243745864, 'flat': 0.23718259848427328, 'up': 0.44882470907826805} | [2.9158354434851876, -2.0829887059033103, -0.832846737581891] | {'down': 0.29316280537842554, 'flat': 0.22885413110845437, 'up': 0.4779830635131199} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.29316280537842554, 'flat': 0.22885413110845437, 'up': 0.4779830635131199} | [-5.411500934229341, 6.335273070514552, -0.9237721362851892] | {'down': 0.35651553608357106, 'flat': 0.21961640974560248, 'up': 0.4238680541708265} |
| 5 | E10/causal | ['9b76ec69-491c-50e1-8c43-6049261a8d2a/1m/technical'] | {'down': 0.35651553608357106, 'flat': 0.21961640974560248, 'up': 0.4238680541708265} | [2.1792756241832634, -2.072444112400329, -0.10683151178293993] | {'down': 0.33579109495956777, 'flat': 0.21854809462777308, 'up': 0.44566081041265915} |
| 6 | E17/scenario | ['60c340d6-8640-5bba-a8a1-afb0495385e4', '5eebda03-4fe1-5907-9199-ceca17615b4d', 'f86672b5-02ac-5192-bc2d-8e8f4e249894', '9317f7c3-07ec-5365-8767-79d0008fee6f'] | {'down': 0.33579109495956777, 'flat': 0.21854809462777308, 'up': 0.44566081041265915} | [0.4088016498513203, 2.832880864341397, -3.2416825141927146] | {'down': 0.36411990360298174, 'flat': 0.18613126948584593, 'up': 0.44974882691117235} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.36411990360298174, 'flat': 0.18613126948584593, 'up': 0.44974882691117235} | [-1.486575717494909, -0.39313124379968256, 1.8797069612945971] | {'down': 0.3601885911649849, 'flat': 0.2049283390987919, 'up': 0.43488306973622326} |
| 8 | E13/history | [] | {'down': 0.3601885911649849, 'flat': 0.2049283390987919, 'up': 0.43488306973622326} | [0.0, 0.0, 0.0] | {'down': 0.3601885911649849, 'flat': 0.2049283390987919, 'up': 0.43488306973622326} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3601885911649849, 'flat': 0.2049283390987919, 'up': 0.43488306973622326} | [-1.270552319698398, -0.18218490305533241, 1.4527372227537194] | {'down': 0.3583667421344316, 'flat': 0.2194557113263291, 'up': 0.4221775465392393} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '8596716bdf70d13e27855fdd90e6f83b13a1515151c2b1a069f21446cf2c75b8'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0504ca3831afec814ba8de7225dd1e4e1cb7f9d3652a626bb295a31d8b7556f6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:dddfae0d52dd5e4dbef6efe44a2823a4e608e0a6ea0e6521a7bd4341ff183cdf#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:734b2ff903a737007814153a502b9625ebec43b4cb08369616c7ba9e186b8f92#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:83045ed7bb73e46e2eed1bde7b0b1b23691ae33aa9db7cc37dcec685c6ac987c#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "9b76ec69-491c-50e1-8c43-6049261a8d2a/1y/technical",
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
      1029,
      1036
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
      1031,
      1039
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '9b76ec69-491c-50e1-8c43-6049261a8d2a/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "1f0338d3-1beb-5615-b2da-386a54275ab6",
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
    "hypothesis_id": "1f0338d3-1beb-5615-b2da-386a54275ab6",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1f0338d3-1beb-5615-b2da-386a54275ab6",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.5892750000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1f0338d3-1beb-5615-b2da-386a54275ab6",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.012448003970429186
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
    "hypothesis_id": "f9ef4aea-af7f-5e43-a4c6-6cad0e8a7e4d",
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
