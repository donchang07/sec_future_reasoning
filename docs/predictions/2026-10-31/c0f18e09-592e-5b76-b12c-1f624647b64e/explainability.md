# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: c0f18e09-592e-5b76-b12c-1f624647b64e
Cutoff / prediction: 2026-10-30T22:00:17.121488+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-30T06:30:00+00:00', 'source_refs': ['raw:13e1b49f6de7f03d46fc79e1affc2d8bb32989d24bb29fb12c7eeba024a3f67c'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 174100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 42.2728% | 36.4278% | 21.2994% | 7.5487% | 0.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 42.7717% | 35.4663% | 21.7621% | 3.8999% | 45.0000% | 10.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 10.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 42.2728% / 36.4278% / 21.2994% | 42.2728% / 36.4278% / 21.2994% | [0.0, 0.0, 0.0] |
| 1m | 41.5062% / 36.6335% / 21.8602% | 42.7717% / 35.4663% / 21.7621% | [1.2654133626098407, -1.1672753654556278, -0.09813799715419902] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504755968888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-30T22:00:16.193380Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "13e1b49f6de7f03d46fc79e1affc2d8bb32989d24bb29fb12c7eeba024a3f67c",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504755968888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-30T22:00:16.616434Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504755968888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-30T22:00:16.575434Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.504755968888889,
    "authority": "official_original",
    "collected_at": "2026-10-30T22:00:16.527903Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-30T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c",
    "reason": null,
    "released_at": null,
    "rows": 209,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-30T22:00:16.698609Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "1153fa1fdf8034ae52bdf10b2caec29fa0ae5020d9a94fdd68408e856ff03d9a",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50475596888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-30T22:00:17.069488Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-29T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b0ab4079d19dc5f32df5e139ee509ac4aad15a79dfca2ade8d5e1411ea35872a",
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
    "collected_at": "2026-10-30T22:00:17.120488Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "372108beb2eaf69e5e17c7ae73cb54ef12ce9bcb63081ff4bbc38ade2ce2761a",
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
    "collected_at": "2026-10-30T22:00:16.617434Z",
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
    "collected_at": "2026-10-30T22:00:16.617434Z",
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
    "collected_at": "2026-10-30T22:00:16.617434Z",
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
    "collected_at": "2026-10-30T22:00:16.617434Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-30T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-30T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-10-30T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b0ab4079d19dc5f32df5e139ee509ac4aad15a79dfca2ade8d5e1411ea35872a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "c0f18e09-592e-5b76-b12c-1f624647b64e/1w/technical",
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
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 3040.485586005412,
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
    "bottom_neckline": 187700.0,
    "bottom_pivots": [
      223,
      232
    ],
    "bottom_score": 0.0,
    "rsi": 43.55056764861911,
    "sma": [
      176947.5,
      176667.5,
      172580.41666666666
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
    "top_neckline": 168100.0,
    "top_pivots": [
      227,
      237
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'c0f18e09-592e-5b76-b12c-1f624647b64e/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "55008a1c-33e5-5742-88e3-6719ddf4dcc8",
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
    "hypothesis_id": "55008a1c-33e5-5742-88e3-6719ddf4dcc8",
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
    "hypothesis_id": "55008a1c-33e5-5742-88e3-6719ddf4dcc8",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.318971540482879
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
    "hypothesis_id": "eed392fb-6f38-516a-924c-fae23da1bc09",
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
    "hypothesis_id": "eed392fb-6f38-516a-924c-fae23da1bc09",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.10508346134520768
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.563892159843582, 0.705047424688654, -0.14115526484508312] | {'down': 0.3570504742468865, 'flat': 0.24858844735154917, 'up': 0.3943610784015642} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3570504742468865, 'flat': 0.24858844735154917, 'up': 0.3943610784015642} | [2.2396352027241164, -1.6868490272933856, -0.5527861754307112] | {'down': 0.34018198397395266, 'flat': 0.24306058559724206, 'up': 0.41675743042880536} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34018198397395266, 'flat': 0.24306058559724206, 'up': 0.41675743042880536} | [4.829806256058672, -3.5330229148991474, -1.2967833411595353] | {'down': 0.3048517548249612, 'flat': 0.2300927521856467, 'up': 0.4650554929893921} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3048517548249612, 'flat': 0.2300927521856467, 'up': 0.4650554929893921} | [4.877835827318544, -3.43546657122808, -1.4423692560904562] | {'down': 0.2704970891126804, 'flat': 0.21566905962474214, 'up': 0.5138338512625775} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2704970891126804, 'flat': 0.21566905962474214, 'up': 0.5138338512625775} | [-7.14253303655989, 8.124323265749938, -0.9817902291900493] | {'down': 0.3517403217701798, 'flat': 0.20585115733284165, 'up': 0.44240852089697863} |
| 5 | E10/causal | ['c0f18e09-592e-5b76-b12c-1f624647b64e/1w/technical'] | {'down': 0.3517403217701798, 'flat': 0.20585115733284165, 'up': 0.44240852089697863} | [0.3541640119830991, -0.3371165116868413, -0.017047500296271667] | {'down': 0.34836915665331136, 'flat': 0.20568068232987893, 'up': 0.4459501610168096} |
| 6 | E17/scenario | ['16e8b0b4-d2db-5925-b37a-3cb07adffdaa', 'b93d0666-9d7a-5aed-93c5-bf93701932ab', '5f95f291-8c1e-517d-9040-4265954809cf', '16cfac3a-b605-5b9d-bc42-94fd640a66f3'] | {'down': 0.34836915665331136, 'flat': 0.20568068232987893, 'up': 0.4459501610168096} | [0.3508930459282633, 2.3106938623992046, -2.6615869083274624] | {'down': 0.3714760952773034, 'flat': 0.1790648132466043, 'up': 0.44945909147609225} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3714760952773034, 'flat': 0.1790648132466043, 'up': 0.44945909147609225} | [-1.4172199730367374, -0.465501236920457, 1.882721209957186] | {'down': 0.36682108290809884, 'flat': 0.19789202534617617, 'up': 0.4352868917457249} |
| 8 | E13/history | [] | {'down': 0.36682108290809884, 'flat': 0.19789202534617617, 'up': 0.4352868917457249} | [0.0, 0.0, 0.0] | {'down': 0.36682108290809884, 'flat': 0.19789202534617617, 'up': 0.4352868917457249} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.36682108290809884, 'flat': 0.19789202534617617, 'up': 0.4352868917457249} | [-1.2559265922192198, -0.25426892734687345, 1.510195519566107] | {'down': 0.3642783936346301, 'flat': 0.21299398054183724, 'up': 0.4227276258235327} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b0ab4079d19dc5f32df5e139ee509ac4aad15a79dfca2ade8d5e1411ea35872a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "c0f18e09-592e-5b76-b12c-1f624647b64e/1m/technical",
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
      1029,
      1040
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
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  },
  "primary": "1d",
  "reflexivity_effect": 0.034999999999999996,
  "regime_effect": 0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'c0f18e09-592e-5b76-b12c-1f624647b64e/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.034999999999999996, 'regime_effect': 0.0525}
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
    "hypothesis_id": "7c1a0b4b-1eff-5425-9a8b-ce8677256424",
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
    "hypothesis_id": "7c1a0b4b-1eff-5425-9a8b-ce8677256424",
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
    "hypothesis_id": "7c1a0b4b-1eff-5425-9a8b-ce8677256424",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.382759040482879
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
    "hypothesis_id": "d732812e-70aa-5d03-97f7-d7b2791e299a",
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
    "hypothesis_id": "d732812e-70aa-5d03-97f7-d7b2791e299a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.041295961345207695
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.0861064473099693, 0.10736103976484723, -0.02125459245487793] | {'down': 0.35107361039764845, 'flat': 0.24978745407545122, 'up': 0.39913893552690033} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35107361039764845, 'flat': 0.24978745407545122, 'up': 0.39913893552690033} | [1.0432698357634662, -0.783132629840072, -0.2601372059233914] | {'down': 0.34324228409924773, 'flat': 0.2471860820162173, 'up': 0.409571633884535} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34324228409924773, 'flat': 0.2471860820162173, 'up': 0.409571633884535} | [3.839542717122324, -2.82341526524561, -1.0161274518767194] | {'down': 0.31500813144679163, 'flat': 0.2370248074974501, 'up': 0.44796706105575823} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.31500813144679163, 'flat': 0.2370248074974501, 'up': 0.44796706105575823} | [3.8908242853205763, -2.773288927075712, -1.11753535824487] | {'down': 0.2872752421760345, 'flat': 0.2258494539150014, 'up': 0.486875303908964} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2872752421760345, 'flat': 0.2258494539150014, 'up': 0.486875303908964} | [-5.303719987403127, 6.146513996164648, -0.8427940087615049] | {'down': 0.348740382137681, 'flat': 0.21742151382738636, 'up': 0.4338381040349327} |
| 5 | E10/causal | ['c0f18e09-592e-5b76-b12c-1f624647b64e/1m/technical'] | {'down': 0.348740382137681, 'flat': 0.21742151382738636, 'up': 0.4338381040349327} | [1.949124757299192, -1.8384246316560993, -0.11070012564310117] | {'down': 0.33035613582112, 'flat': 0.21631451257095535, 'up': 0.45332935160792465} |
| 6 | E17/scenario | ['e642fd4e-1300-5ac1-ae5e-ffee0b34707a', '3b482ca2-4314-5a58-a6b6-a237c2604a33', 'dc5250a1-141b-51be-9db3-be174cbcfe93', '67b57a05-96ef-530a-bcd0-be0c8eec7d98'] | {'down': 0.33035613582112, 'flat': 0.21631451257095535, 'up': 0.45332935160792465} | [0.2961818179313125, 2.855707241075417, -3.1518890590067294] | {'down': 0.35891320823187417, 'flat': 0.18479562198088806, 'up': 0.45629116978723777} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.35891320823187417, 'flat': 0.18479562198088806, 'up': 0.45629116978723777} | [-1.4981655724258025, -0.3116750345092456, 1.8098406069350537] | {'down': 0.3557964578867817, 'flat': 0.2028940280502386, 'up': 0.44130951406297975} |
| 8 | E13/history | [] | {'down': 0.3557964578867817, 'flat': 0.2028940280502386, 'up': 0.44130951406297975} | [0.0, 0.0, 0.0] | {'down': 0.3557964578867817, 'flat': 0.2028940280502386, 'up': 0.44130951406297975} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3557964578867817, 'flat': 0.2028940280502386, 'up': 0.44130951406297975} | [-1.3592965433038617, -0.11337946683578348, 1.4726760101396423] | {'down': 0.3546626632184239, 'flat': 0.21762078815163502, 'up': 0.42771654862994113} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '15c55a92f0c4dc7a6a44198dcac3958ad64d80def71e91a7c7a60661450095fa'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b0ab4079d19dc5f32df5e139ee509ac4aad15a79dfca2ade8d5e1411ea35872a'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c15e90a939a7eb627fde6bb694d2f98ad5998929d9ffe5fb5f06ca7bc63bc283#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191d3c9bc6ae13fcc07bd95cabb4351c2079a627c4c82a7f71b6b2e0b2d886a1#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:37fd0cb364e981dd363f6e459fbc04feed5ecd8fe89d45f1fe420f9d78798d0c#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "c0f18e09-592e-5b76-b12c-1f624647b64e/1y/technical",
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
      1029,
      1040
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
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'c0f18e09-592e-5b76-b12c-1f624647b64e/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.030000000000000006, 'regime_effect': -0.045000000000000005}
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
    "hypothesis_id": "350936f2-6662-58e4-83c4-65487b2b1e58",
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
    "hypothesis_id": "350936f2-6662-58e4-83c4-65487b2b1e58",
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
    "hypothesis_id": "350936f2-6662-58e4-83c4-65487b2b1e58",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.264296540482879
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
    "hypothesis_id": "2a684ce2-c37c-554d-941d-c406ba716add",
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
    "hypothesis_id": "2a684ce2-c37c-554d-941d-c406ba716add",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.1597584613452077
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
