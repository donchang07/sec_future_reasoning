# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 6487e450-7fef-501a-bc1d-12662ad45bbf
Cutoff / prediction: 2026-11-05T22:00:13.459585+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-11-05T06:30:00+00:00', 'source_refs': ['raw:4d2aed8444a66c8db19eb955de702c6ac8b92b8b13817cfe5f53da0008648a5b'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 160400.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 39.3829% | 39.0869% | 21.5302% | 7.3743% | 0.0000% | 20.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 40.7128% | 37.3107% | 21.9765% | 3.8395% | 0.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 10.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 40.3315% / 38.1409% / 21.5276% | 39.3829% / 39.0869% / 21.5302% | [-0.9485429259784517, 0.9460003710932419, 0.0025425548852126] |
| 1m | 40.7128% / 37.3107% / 21.9765% | 40.7128% / 37.3107% / 21.9765% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.50373877361111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-05T22:00:12.798411Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-05T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "4d2aed8444a66c8db19eb955de702c6ac8b92b8b13817cfe5f53da0008648a5b",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.50373877361111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-05T22:00:13.118961Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-05T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.50373877361111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-05T22:00:13.070321Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-11-05T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 1.503738773611111,
    "authority": "official_original",
    "collected_at": "2026-11-05T22:00:13.022187Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-11-05T20:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b",
    "reason": null,
    "released_at": null,
    "rows": 213,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-05T22:00:13.199260Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "20216c5ffb6c3f38162fa936f6bdc1e3d5fa3adfd8ddd9afe1c762f5d83d505e",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50373877361111,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-05T22:00:13.329338Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-11-04T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "6402a4a18aef2930fb87fbe146abeec6c8addc21fdd820d5432dd27ba9c58dce",
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
    "collected_at": "2026-11-05T22:00:13.443424Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "c553a53fae9ce257ba5db1182f488705c527f85d5ad5f622fec63f3dd6d44c06",
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
    "collected_at": "2026-11-05T22:00:13.118961Z",
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
    "collected_at": "2026-11-05T22:00:13.118961Z",
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
    "collected_at": "2026-11-05T22:00:13.118961Z",
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
    "collected_at": "2026-11-05T22:00:13.118961Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-11-05T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-30T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-11-05T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:6402a4a18aef2930fb87fbe146abeec6c8addc21fdd820d5432dd27ba9c58dce'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "6487e450-7fef-501a-bc1d-12662ad45bbf/1w/technical",
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
    "atr": 11390.567067575863,
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
      4922,
      4927
    ],
    "bottom_score": 0.0,
    "rsi": 39.43205368828307,
    "sma": [
      173155.0,
      186808.33333333334,
      190950.0
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
    "top_neckline": 159000.0,
    "top_pivots": [
      4920,
      4926
    ],
    "top_score": 0.0,
    "volume_ratio": 1.093036986457418
  },
  "primary": "30m",
  "reflexivity_effect": -0.020000000000000004,
  "regime_effect": -0.03,
  "sell_liquidity": null,
  "wave": {
    "atr": 2262.6048371175284,
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
    "bottom_neckline": 171900.0,
    "bottom_pivots": [
      247,
      254
    ],
    "bottom_score": 0.0,
    "rsi": 33.33506599107923,
    "sma": [
      164487.5,
      170145.83333333334,
      172575.41666666666
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
    "top_neckline": 160600.0,
    "top_pivots": [
      251,
      257
    ],
    "top_score": 0.2,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '6487e450-7fef-501a-bc1d-12662ad45bbf/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "8062cb64-554f-520c-881e-698577180c46",
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
    "hypothesis_id": "8062cb64-554f-520c-881e-698577180c46",
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
    "hypothesis_id": "8062cb64-554f-520c-881e-698577180c46",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.03376212384053817
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
    "hypothesis_id": "e0fe87c6-cad9-5a93-9133-c0d35c37f11d",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6803999999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e0fe87c6-cad9-5a93-9133-c0d35c37f11d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.3217845504163571
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.7295686271034505, 2.177137128111084, -0.44756850100762247] | {'down': 0.3717713712811108, 'flat': 0.24552431498992378, 'up': 0.3827043137289655} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3717713712811108, 'flat': 0.24552431498992378, 'up': 0.3827043137289655} | [0.23362065600718296, -0.18110833272392823, -0.052512323283260276] | {'down': 0.36996028795387154, 'flat': 0.24499919175709117, 'up': 0.38504052028903735} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36996028795387154, 'flat': 0.24499919175709117, 'up': 0.38504052028903735} | [4.759536770929406, -3.612889209683673, -1.1466475612457339] | {'down': 0.3338313958570348, 'flat': 0.23353271614463383, 'up': 0.4326358879983314} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3338313958570348, 'flat': 0.23353271614463383, 'up': 0.4326358879983314} | [4.869036925942166, -3.5567866190361785, -1.3122503069059877] | {'down': 0.298263529666673, 'flat': 0.22041021307557396, 'up': 0.4813262572577531} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.298263529666673, 'flat': 0.22041021307557396, 'up': 0.4813262572577531} | [-6.42810597824075, 7.529074096980414, -1.100968118739662] | {'down': 0.37355427063647717, 'flat': 0.20940053188817734, 'up': 0.4170451974753456} |
| 5 | E10/causal | ['6487e450-7fef-501a-bc1d-12662ad45bbf/1w/technical'] | {'down': 0.37355427063647717, 'flat': 0.20940053188817734, 'up': 0.4170451974753456} | [-1.267663335350161, 1.2470288749296399, 0.02063446042052386] | {'down': 0.38602455938577357, 'flat': 0.20960687649238258, 'up': 0.40436856412184397} |
| 6 | E17/scenario | ['ccba0261-76d6-520c-b259-67dd4f9d23c8', 'be37adaf-5af5-5aee-8824-0bff0dfbae98', 'c46e2f84-a6fe-5ffe-89b9-450b5c392a38', '1a4bf329-1298-50ca-b0ef-91674634e246'] | {'down': 0.38602455938577357, 'flat': 0.20960687649238258, 'up': 0.40436856412184397} | [0.6655877484995798, 2.104599817910019, -2.77018756640961] | {'down': 0.40707055756487376, 'flat': 0.18190500082828648, 'up': 0.41102444160683976} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.40707055756487376, 'flat': 0.18190500082828648, 'up': 0.41102444160683976} | [-0.9531742264795418, -0.9046649382605743, 1.8578391647401133] | {'down': 0.398023908182268, 'flat': 0.2004833924756876, 'up': 0.40149269934204435} |
| 8 | E13/history | [] | {'down': 0.398023908182268, 'flat': 0.2004833924756876, 'up': 0.40149269934204435} | [0.0, 0.0, 0.0] | {'down': 0.398023908182268, 'flat': 0.2004833924756876, 'up': 0.40149269934204435} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.398023908182268, 'flat': 0.2004833924756876, 'up': 0.40149269934204435} | [-0.7663412368436873, -0.7155060154978576, 1.481847252341556] | {'down': 0.39086884802728944, 'flat': 0.21530186499910317, 'up': 0.3938292869736075} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:6402a4a18aef2930fb87fbe146abeec6c8addc21fdd820d5432dd27ba9c58dce'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "6487e450-7fef-501a-bc1d-12662ad45bbf/1m/technical",
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
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1028,
      1039
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
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
      1031,
      1036
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 11390.567067575863,
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
      4922,
      4927
    ],
    "bottom_score": 0.0,
    "rsi": 39.43205368828307,
    "sma": [
      173155.0,
      186808.33333333334,
      190950.0
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
    "top_neckline": 159000.0,
    "top_pivots": [
      4920,
      4926
    ],
    "top_score": 0.0,
    "volume_ratio": 1.093036986457418
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '6487e450-7fef-501a-bc1d-12662ad45bbf/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "31e2211e-8b70-5237-81fb-ea1c45887c76",
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
    "hypothesis_id": "31e2211e-8b70-5237-81fb-ea1c45887c76",
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
    "hypothesis_id": "31e2211e-8b70-5237-81fb-ea1c45887c76",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.07021212384053818
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
    "hypothesis_id": "bf0205e0-ba30-51a1-a04c-f796f870e0d3",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6803999999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "bf0205e0-ba30-51a1-a04c-f796f870e0d3",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.28533455041635714
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.5954755564124836, 0.7446737177825957, -0.14919816137010933] | {'down': 0.35744673717782594, 'flat': 0.2485080183862989, 'up': 0.3940452444358752} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35744673717782594, 'flat': 0.2485080183862989, 'up': 0.3940452444358752} | [0.19025082491211376, -0.14464310151695026, -0.0456077233951635] | {'down': 0.35600030616265643, 'flat': 0.24805194115234727, 'up': 0.3959477526849963} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.35600030616265643, 'flat': 0.24805194115234727, 'up': 0.3959477526849963} | [3.814366621255394, -2.8509991688661196, -0.9633674523892882] | {'down': 0.32749031447399524, 'flat': 0.2384182666284544, 'up': 0.43409141889755026} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32749031447399524, 'flat': 0.2384182666284544, 'up': 0.43409141889755026} | [3.8823779231104805, -2.812236614322744, -1.0701413087877225] | {'down': 0.2993679483307678, 'flat': 0.22771685354057716, 'up': 0.47291519812865507} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2993679483307678, 'flat': 0.22771685354057716, 'up': 0.47291519812865507} | [-4.746718116354737, 5.567101781005918, -0.8203836646511947] | {'down': 0.355038966140827, 'flat': 0.21951301689406522, 'up': 0.4254480169651077} |
| 5 | E10/causal | ['6487e450-7fef-501a-bc1d-12662ad45bbf/1m/technical'] | {'down': 0.355038966140827, 'flat': 0.21951301689406522, 'up': 0.4254480169651077} | [-0.3499667617836155, 0.3369476435616192, 0.013019118222018511] | {'down': 0.35840844257644316, 'flat': 0.2196432080762854, 'up': 0.42194834934727155} |
| 6 | E17/scenario | ['be48e99e-ae3e-592d-81d7-3569f109c1e0', '8585f2a9-7982-56a0-99ab-41fbf6d151e3', 'b23ae0ec-c3b9-5172-b2fd-4fd28c8de445', '2dda6cce-aeb4-57a5-9ed0-c762c8ea4343'] | {'down': 0.35840844257644316, 'flat': 0.2196432080762854, 'up': 0.42194834934727155} | [0.6995122838717505, 2.514584840165229, -3.214097124036988] | {'down': 0.38355429097809546, 'flat': 0.18750223683591552, 'up': 0.42894347218598905} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.38355429097809546, 'flat': 0.18750223683591552, 'up': 0.42894347218598905} | [-1.1691230566579558, -0.6141030670441638, 1.783226123702117] | {'down': 0.3774132603076538, 'flat': 0.2053344980729367, 'up': 0.4172522416194095} |
| 8 | E13/history | [] | {'down': 0.3774132603076538, 'flat': 0.2053344980729367, 'up': 0.4172522416194095} | [0.0, 0.0, 0.0] | {'down': 0.3774132603076538, 'flat': 0.2053344980729367, 'up': 0.4172522416194095} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3774132603076538, 'flat': 0.2053344980729367, 'up': 0.4172522416194095} | [-1.012472893848887, -0.43061934800418533, 1.4430922418530807] | {'down': 0.37310706682761197, 'flat': 0.2197654204914675, 'up': 0.4071275126809206} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '20ac63f4ac8b5bd080ddc617ed54a477b4890239c5728f11a7138b8cf4153be0'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:6402a4a18aef2930fb87fbe146abeec6c8addc21fdd820d5432dd27ba9c58dce'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9daef8c2b1d61cca8321ff06b9f7937ad4eff51541a1241725b4aafdf47a5886#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:87ece106ff5a2fde50abd202018a2f4e8f80da650393925baaf7924bd43e72a7#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:e96199b32569922ed01f894b55501a7ae11d17498c837f0bae088978b68a4d0b#us_10y_yield@2026-10-29T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "6487e450-7fef-501a-bc1d-12662ad45bbf/1y/technical",
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
  "reflexivity_effect": -0.030000000000000006,
  "regime_effect": -0.045000000000000005,
  "sell_liquidity": null,
  "wave": {
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1028,
      1039
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
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
      1031,
      1036
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '6487e450-7fef-501a-bc1d-12662ad45bbf/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.030000000000000006, 'regime_effect': -0.045000000000000005}
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
    "hypothesis_id": "b47f10f9-edbb-5dbe-bd0d-1d7d5ab77cf3",
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
    "hypothesis_id": "b47f10f9-edbb-5dbe-bd0d-1d7d5ab77cf3",
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
    "hypothesis_id": "b47f10f9-edbb-5dbe-bd0d-1d7d5ab77cf3",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.015537123840538167
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
    "hypothesis_id": "8900ef95-8665-5f14-90d5-d39a312545a8",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6803999999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8900ef95-8665-5f14-90d5-d39a312545a8",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.34000955041635716
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
