# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245
Cutoff / prediction: 2026-10-15T22:00:15.052532+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-15T06:30:00+00:00', 'source_refs': ['raw:b34c28307264b0c53bd3162cde550ecc1e175a3529d717989ad977a5cf5a3cdd'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 159100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 43.5150% | 35.9823% | 20.5027% | 7.5264% | 35.0000% | 20.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 40.3868% | 38.0483% | 21.5649% | 3.8154% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 42.7652% / 36.6703% / 20.5645% | 43.5150% / 35.9823% / 20.5027% | [0.7497942887785769, -0.6879527476418124, -0.06184154113676177] |
| 1m | 41.6397% / 36.8189% / 21.5414% | 40.3868% / 38.0483% / 21.5649% | [-1.2528597566908772, 1.2293909550669557, 0.02346880162392151] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.50418125888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-15T22:00:14.208039Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b34c28307264b0c53bd3162cde550ecc1e175a3529d717989ad977a5cf5a3cdd",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.50418125888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-15T22:00:14.568289Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.50418125888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-15T22:00:14.611290Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.504181258888889,
    "authority": "official_original",
    "collected_at": "2026-10-15T22:00:14.260556Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-15T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6",
    "reason": null,
    "released_at": null,
    "rows": 198,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-15T22:00:14.684485Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "1cfbe05505feaefc7a438412b5bd523fdbffeff768c7a98a449c42922d7d4115",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50418125888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-15T22:00:14.770150Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "904f621717ffcab1f76aa3929eef1891a8ed18693b966dd0a4244696ac24cd41",
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
    "collected_at": "2026-10-15T22:00:15.051532Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "28c063cdcce9cb3aeb469cfa207cb4e3a3574310e6a649b892e3921e7ca8413a",
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
    "collected_at": "2026-10-15T22:00:14.612289Z",
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
    "collected_at": "2026-10-15T22:00:14.612289Z",
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
    "collected_at": "2026-10-15T22:00:14.612289Z",
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
    "collected_at": "2026-10-15T22:00:14.612289Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-10-15T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-09T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-15T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:904f621717ffcab1f76aa3929eef1891a8ed18693b966dd0a4244696ac24cd41'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1w/technical",
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
    "atr": 10391.999413295287,
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
    "rsi": 31.45588048122859,
    "sma": [
      194485.0,
      187541.66666666666,
      190059.16666666666
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
    "volume_ratio": 1.7199973889904023
  },
  "primary": "30m",
  "reflexivity_effect": 0.014999999999999998,
  "regime_effect": 0.022499999999999996,
  "sell_liquidity": null,
  "wave": {
    "atr": 2847.3341349689667,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": true,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 160800.0,
    "bottom_pivots": [
      206,
      212
    ],
    "bottom_score": 0.35,
    "rsi": 36.455734224169696,
    "sma": [
      164522.5,
      178850.83333333334,
      189085.41666666666
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
    "top_neckline": 155300.0,
    "top_pivots": [
      208,
      214
    ],
    "top_score": 0.2,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.014999999999999998, 'regime_effect': 0.022499999999999996}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': None}, 'negative_families': [], 'positive_families': [], 'root_contributions': {}, 'score': None, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment', 'semiconductor_export_momentum']}

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
    "hypothesis_id": "ad50a36b-0b03-561a-ae45-b0ddce529f74",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.8240980294910846
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ad50a36b-0b03-561a-ae45-b0ddce529f74",
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
    "hypothesis_id": "ad50a36b-0b03-561a-ae45-b0ddce529f74",
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
    "hypothesis_id": "266c241f-a2bc-5d36-bec3-06681257be14",
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
    "hypothesis_id": "266c241f-a2bc-5d36-bec3-06681257be14",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.4733537270068281
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-2.546338383648128, 3.2202588694819125, -0.6739204858337816] | {'down': 0.3822025886948191, 'flat': 0.24326079514166218, 'up': 0.37453661616351874} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3822025886948191, 'flat': 0.24326079514166218, 'up': 0.37453661616351874} | [5.797216781751463, -4.4517281008142895, -1.3454886809371764] | {'down': 0.3376853076866762, 'flat': 0.22980590833229042, 'up': 0.4325087839810334} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3376853076866762, 'flat': 0.22980590833229042, 'up': 0.4325087839810334} | [4.877978382279008, -3.5913446072084962, -1.286633775070506] | {'down': 0.30177186161459124, 'flat': 0.21693957058158536, 'up': 0.48128856780382345} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.30177186161459124, 'flat': 0.21693957058158536, 'up': 0.48128856780382345} | [4.89569416080029, -3.477499892789515, -1.4181942680107835] | {'down': 0.2669968626866961, 'flat': 0.20275762790147753, 'up': 0.5302455094118264} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2669968626866961, 'flat': 0.20275762790147753, 'up': 0.5302455094118264} | [-7.723596444951331, 8.669460727038153, -0.9458642820868196] | {'down': 0.3536914699570776, 'flat': 0.19329898508060933, 'up': 0.45300954496231305} |
| 5 | E10/causal | ['b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1w/technical'] | {'down': 0.3536914699570776, 'flat': 0.19329898508060933, 'up': 0.45300954496231305} | [1.2009913179536535, -1.1379268690759003, -0.06306444887775597] | {'down': 0.3423122012663186, 'flat': 0.19266834059183177, 'up': 0.4650194581418496} |
| 6 | E17/scenario | ['cecf57cc-05b3-5730-b872-4ee7d62fab0e', 'c41dbaaa-7584-58a2-a4cb-e2badf10003a', 'cb98ee3f-d496-5b23-9f22-6dc714b0447c', '9aed2d6f-598c-5a16-9616-34cc1f2349fc'] | {'down': 0.3423122012663186, 'flat': 0.19266834059183177, 'up': 0.4650194581418496} | [0.06811896333903111, 2.284325226883194, -2.352444190222225] | {'down': 0.36515545353515055, 'flat': 0.16914389868960952, 'up': 0.4657006477752399} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.36515545353515055, 'flat': 0.16914389868960952, 'up': 0.4657006477752399} | [-1.616529892751356, -0.3886262161762022, 2.0051561089275696] | {'down': 0.36126919137338853, 'flat': 0.18919545977888522, 'up': 0.44953534884772633} |
| 8 | E13/history | [] | {'down': 0.36126919137338853, 'flat': 0.18919545977888522, 'up': 0.44953534884772633} | [0.0, 0.0, 0.0] | {'down': 0.36126919137338853, 'flat': 0.18919545977888522, 'up': 0.44953534884772633} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.36126919137338853, 'flat': 0.18919545977888522, 'up': 0.44953534884772633} | [-1.4385059636348174, -0.1446199285286831, 1.5831258921634976] | {'down': 0.3598229920881017, 'flat': 0.2050267187005202, 'up': 0.43515028921137816} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:904f621717ffcab1f76aa3929eef1891a8ed18693b966dd0a4244696ac24cd41'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1m/technical",
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
      1024,
      1031
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 10391.999413295287,
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
    "rsi": 31.45588048122859,
    "sma": [
      194485.0,
      187541.66666666666,
      190059.16666666666
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
    "volume_ratio": 1.7199973889904023
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "d3fca6aa-cc35-5940-96ad-3cc86d0529bf",
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
    "hypothesis_id": "d3fca6aa-cc35-5940-96ad-3cc86d0529bf",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d3fca6aa-cc35-5940-96ad-3cc86d0529bf",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.7329730294910848
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
    "hypothesis_id": "76f66ec5-1bc1-5ea9-bdb6-3cb1fe5c32c1",
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
    "hypothesis_id": "76f66ec5-1bc1-5ea9-bdb6-3cb1fe5c32c1",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.5644787270068281
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.1790691051882352, 1.479485145109588, -0.30041603992135013] | {'down': 0.36479485145109586, 'flat': 0.2469958396007865, 'up': 0.38820930894811767} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.36479485145109586, 'flat': 0.2469958396007865, 'up': 0.38820930894811767} | [1.9933938787889405, -1.5192083079647478, -0.47418557082419266] | {'down': 0.3496027683714484, 'flat': 0.24225398389254457, 'up': 0.4081432477360071} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3496027683714484, 'flat': 0.24225398389254457, 'up': 0.4081432477360071} | [3.846443998290022, -2.861150514558214, -0.9852934837318195] | {'down': 0.32099126322586624, 'flat': 0.23240104905522638, 'up': 0.4466076877189073} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32099126322586624, 'flat': 0.23240104905522638, 'up': 0.4466076877189073} | [3.899743653549864, -2.813464127691306, -1.0862795258585467] | {'down': 0.2928566219489532, 'flat': 0.2215382537966409, 'up': 0.48560512425440594} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2928566219489532, 'flat': 0.2215382537966409, 'up': 0.48560512425440594} | [-5.70282446213175, 6.628569641524407, -0.9257451793926563] | {'down': 0.35914231836419724, 'flat': 0.21228080200271435, 'up': 0.42857687963308844} |
| 5 | E10/causal | ['b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1m/technical'] | {'down': 0.35914231836419724, 'flat': 0.21228080200271435, 'up': 0.42857687963308844} | [-1.1177232180655028, 1.0828786802926482, 0.03484453777284624] | {'down': 0.3699711051671237, 'flat': 0.2126292473804428, 'up': 0.4173996474524334} |
| 6 | E17/scenario | ['c839947a-4bfe-5623-bcf0-9ad50fdcc98f', '7e1b643c-87bf-58f2-bd03-06fe45e803d6', 'bbee869f-3ef7-5620-91ad-2a2c4b7a78ce', 'bbc0461e-99ee-5bf6-9cff-4d88eca722c5'] | {'down': 0.3699711051671237, 'flat': 0.2126292473804428, 'up': 0.4173996474524334} | [0.7029254816011132, 2.3236749743306753, -3.0266004559317827] | {'down': 0.3932078549104305, 'flat': 0.18236324282112498, 'up': 0.42442890226844454} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3932078549104305, 'flat': 0.18236324282112498, 'up': 0.42442890226844454} | [-1.11550395978533, -0.7331889650645851, 1.8486929248499095] | {'down': 0.3858759652597846, 'flat': 0.20085017206962408, 'up': 0.41327386267059124} |
| 8 | E13/history | [] | {'down': 0.3858759652597846, 'flat': 0.20085017206962408, 'up': 0.41327386267059124} | [0.0, 0.0, 0.0] | {'down': 0.3858759652597846, 'flat': 0.20085017206962408, 'up': 0.41327386267059124} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3858759652597846, 'flat': 0.20085017206962408, 'up': 0.41327386267059124} | [-0.9405751828626407, -0.5393162556501574, 1.4798914385128037] | {'down': 0.38048280270328305, 'flat': 0.21564908645475211, 'up': 0.40386811084196483} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '8709794310018a2088e8f8f79276f9e1735b25c9100272c627288a98054ada33'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:904f621717ffcab1f76aa3929eef1891a8ed18693b966dd0a4244696ac24cd41'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:04b1ce7ec3109d8ecf13c3bf7f40e62ef35b38e3b4484a3f7963b3a959dc2e79#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:ed8e40f422f46b3c06b20770985235942815999edba92274b3d6be3148e4453c#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:9a8440a2f7f543745af8ff61b78f9f3fa617124f447709450c96e974d07905f6#us_10y_yield@2026-10-08T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1y/technical",
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
      1024,
      1031
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'b7f5b4c4-c8cc-5ea4-b4fe-49c59e66b245/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "7d8e1b64-989f-5f03-89de-90e9925f31c4",
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
    "hypothesis_id": "7d8e1b64-989f-5f03-89de-90e9925f31c4",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "7d8e1b64-989f-5f03-89de-90e9925f31c4",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.7603105294910847
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
    "hypothesis_id": "879bd030-9094-580b-91c5-6b147a7c555e",
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
    "hypothesis_id": "879bd030-9094-580b-91c5-6b147a7c555e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.537141227006828
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
