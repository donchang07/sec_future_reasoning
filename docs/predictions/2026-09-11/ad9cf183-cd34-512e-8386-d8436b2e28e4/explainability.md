# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: ad9cf183-cd34-512e-8386-d8436b2e28e4
Cutoff / prediction: 2026-09-10T22:00:11.251454+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-10T06:30:00+00:00', 'source_refs': ['raw:9da0d79fd158e721ea4792642779e02172fbbafad37f7579ce1ba270b11d4b91'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 203000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 47.1222% | 32.3323% | 20.5454% | 8.0346% | 35.0000% | 35.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 44.6916% | 33.8612% | 21.4473% | 6.3603% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 47.1222% / 32.3323% / 20.5454% | 47.1222% / 32.3323% / 20.5454% | [0.0, 0.0, 0.0] |
| 1m | 43.7929% / 34.6875% / 21.5196% | 44.6916% / 33.8612% / 21.4473% | [0.8986164011967557, -0.8262967596829041, -0.07231964151385162] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503125403888887,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-10T22:00:09.728745Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-10T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "9da0d79fd158e721ea4792642779e02172fbbafad37f7579ce1ba270b11d4b91",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503125403888887,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-10T22:00:10.820651Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-10T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503125403888887,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-10T22:00:10.637090Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-10T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503125403888889,
    "authority": "official_original",
    "collected_at": "2026-09-10T22:00:09.824646Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-10T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291",
    "reason": null,
    "released_at": null,
    "rows": 174,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-10T22:00:10.371471Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "b8755f0e8014537f09883bf44ada16e98f3d7dd37fcbf05ac21490e7f6ce467d",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503125403888895,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-10T22:00:10.819652Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d59c556fe3a61dcfc9dbe033a02ecd8f9fdfd6111a35a7c4521c13ab416bd499",
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
    "collected_at": "2026-09-10T22:00:11.251454Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "020f081df6420b0d98bd0fd38cf757da0845cd66bc97804ae70b10235429ec04",
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
    "collected_at": "2026-09-10T22:00:10.637090Z",
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
    "collected_at": "2026-09-10T22:00:10.637090Z",
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
    "collected_at": "2026-09-10T22:00:10.637090Z",
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
    "collected_at": "2026-09-10T22:00:10.637090Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-09-10T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-04T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-09-10T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d59c556fe3a61dcfc9dbe033a02ecd8f9fdfd6111a35a7c4521c13ab416bd499'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-03T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "ad9cf183-cd34-512e-8386-d8436b2e28e4/1w/technical",
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
    "atr": 10781.81410678123,
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
    "rsi": 57.487916523569275,
    "sma": [
      192090.0,
      191590.0,
      179295.83333333334
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
    "volume_ratio": 0.8549708689274952
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 1362.9272634478245,
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
    "bottom_neckline": 200500.0,
    "bottom_pivots": [
      241,
      254
    ],
    "bottom_score": 0.35,
    "rsi": 70.92107493756853,
    "sma": [
      198247.5,
      196880.83333333334,
      191625.0
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 195600.0,
    "top_pivots": [
      245,
      252
    ],
    "top_score": 0.35,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'ad9cf183-cd34-512e-8386-d8436b2e28e4/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "2f4d6157-96eb-5c7c-a1e7-0f3ab3043d7d",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2f4d6157-96eb-5c7c-a1e7-0f3ab3043d7d",
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
    "hypothesis_id": "2f4d6157-96eb-5c7c-a1e7-0f3ab3043d7d",
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
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2f4d6157-96eb-5c7c-a1e7-0f3ab3043d7d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.20217374613637043
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
    "hypothesis_id": "c2420ad3-3a57-5089-8f3b-38df0381e457",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7695000000000002
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [1.419405732460871, -1.0621175877593647, -0.35728814470150083] | {'down': 0.33937882412240633, 'flat': 0.246427118552985, 'up': 0.41419405732460873} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.33937882412240633, 'flat': 0.246427118552985, 'up': 0.41419405732460873} | [5.791229133953651, -4.2056257475307, -1.5856033864229513] | {'down': 0.29732256664709933, 'flat': 0.23057108468875548, 'up': 0.47210634866414525} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.29732256664709933, 'flat': 0.23057108468875548, 'up': 0.47210634866414525} | [4.870645213238511, -3.391657748429433, -1.4789874648090868] | {'down': 0.263405989162805, 'flat': 0.2157812100406646, 'up': 0.5208128007965304} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.263405989162805, 'flat': 0.2157812100406646, 'up': 0.5208128007965304} | [4.813150833276925, -3.232207447580451, -1.580943385696465] | {'down': 0.23108391468700049, 'flat': 0.19997177618369996, 'up': 0.5689443091292996} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.23108391468700049, 'flat': 0.19997177618369996, 'up': 0.5689443091292996} | [-7.048584348075221, 7.602512864466629, -0.5539285163914109] | {'down': 0.3071090433316668, 'flat': 0.19443249101978585, 'up': 0.4984584656485474} |
| 5 | E10/causal | ['ad9cf183-cd34-512e-8386-d8436b2e28e4/1w/technical'] | {'down': 0.3071090433316668, 'flat': 0.19443249101978585, 'up': 0.4984584656485474} | [1.673337301650063, -1.5061835558665693, -0.1671537457834965] | {'down': 0.2920472077730011, 'flat': 0.1927609535619509, 'up': 0.515191838665048} |
| 6 | E17/scenario | ['d9c84965-02d2-5ecd-9df3-450a55300fb1', 'a662a4d1-7e1d-5503-9227-b2b4817521ca', '8fdfc1ca-7360-576c-a7a3-e77da19c0eec', '197f290a-c726-5a66-b6ab-c0f82bd1c5a9'] | {'down': 0.2920472077730011, 'flat': 0.1927609535619509, 'up': 0.515191838665048} | [-0.17481574233119135, 2.4875746699968895, -2.3127589276656924] | {'down': 0.31692295447297, 'flat': 0.16963336428529396, 'up': 0.5134436812417361} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.31692295447297, 'flat': 0.16963336428529396, 'up': 0.5134436812417361} | [-2.165688937138377, 0.19732223253609016, 1.9683667046022812] | {'down': 0.3188961767983309, 'flat': 0.18931703133131678, 'up': 0.49178679187035235} |
| 8 | E13/history | [] | {'down': 0.3188961767983309, 'flat': 0.18931703133131678, 'up': 0.49178679187035235} | [0.0, 0.0, 0.0] | {'down': 0.3188961767983309, 'flat': 0.18931703133131678, 'up': 0.49178679187035235} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3188961767983309, 'flat': 0.18931703133131678, 'up': 0.49178679187035235} | [-2.0564328244847605, 0.4426982198197871, 1.6137346046649763] | {'down': 0.32332315899652875, 'flat': 0.20545437737796654, 'up': 0.47122246362550474} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d59c556fe3a61dcfc9dbe033a02ecd8f9fdfd6111a35a7c4521c13ab416bd499'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-03T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "ad9cf183-cd34-512e-8386-d8436b2e28e4/1m/technical",
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
    "atr": 25575.479086468946,
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
    "rsi": 56.03519597017332,
    "sma": [
      190905.0,
      124510.83333333333,
      87986.25
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
    "volume_ratio": 0.5330666693133895
  },
  "primary": "1d",
  "reflexivity_effect": 0.02500000000000001,
  "regime_effect": 0.037500000000000006,
  "sell_liquidity": null,
  "wave": {
    "atr": 10781.81410678123,
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
    "rsi": 57.487916523569275,
    "sma": [
      192090.0,
      191590.0,
      179295.83333333334
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
    "volume_ratio": 0.8549708689274952
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'ad9cf183-cd34-512e-8386-d8436b2e28e4/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'regime_effect': 0.037500000000000006}
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
    "hypothesis_id": "8ea5454b-d2e2-5b20-973a-f003b2c318d6",
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
    "hypothesis_id": "8ea5454b-d2e2-5b20-973a-f003b2c318d6",
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
    "hypothesis_id": "8ea5454b-d2e2-5b20-973a-f003b2c318d6",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.8555625
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8ea5454b-d2e2-5b20-973a-f003b2c318d6",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.24773624613637046
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
    "hypothesis_id": "e77dc05f-223a-55f6-b470-5f8391267af7",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7695000000000002
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.6746501183487963, -0.5064557320429264, -0.16819438630587547] | {'down': 0.3449354426795707, 'flat': 0.24831805613694125, 'up': 0.406746501183488} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3449354426795707, 'flat': 0.24831805613694125, 'up': 0.406746501183488} | [2.3527772270449, -1.7434916609889772, -0.6092855660559088] | {'down': 0.32750052606968094, 'flat': 0.24222520047638216, 'up': 0.430274273453937} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.32750052606968094, 'flat': 0.24222520047638216, 'up': 0.430274273453937} | [3.8723049224306303, -2.796954026333381, -1.0753508960972658] | {'down': 0.2995309858063471, 'flat': 0.2314716915154095, 'up': 0.4689973226782433} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.2995309858063471, 'flat': 0.2314716915154095, 'up': 0.4689973226782433} | [3.8981796252430865, -2.7309736269113536, -1.1672059983317218] | {'down': 0.2722212495372336, 'flat': 0.21979963153209228, 'up': 0.5079791189306742} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2722212495372336, 'flat': 0.21979963153209228, 'up': 0.5079791189306742} | [-5.350407822323833, 6.067503861334966, -0.7170960390111419] | {'down': 0.33289628815058325, 'flat': 0.21262867114198086, 'up': 0.45447504070743583} |
| 5 | E10/causal | ['ad9cf183-cd34-512e-8386-d8436b2e28e4/1m/technical'] | {'down': 0.33289628815058325, 'flat': 0.21262867114198086, 'up': 0.45447504070743583} | [2.8073929443349908, -2.5860619518641768, -0.22133099247081678] | {'down': 0.3070356686319415, 'flat': 0.2104153612172727, 'up': 0.48254897015078574} |
| 6 | E17/scenario | ['dd62d37d-13bc-5a62-96cd-41afcaf44ed8', '14697e73-7bbb-517d-b9e8-ebe0824fd11a', 'fe2eb95d-67f6-51af-9f37-2f3fe7166f5d', 'a2e1f244-d9c2-5fbb-98af-60b4e2f0ef03'] | {'down': 0.3070356686319415, 'flat': 0.2104153612172727, 'up': 0.48254897015078574} | [-0.09309247780013852, 3.046347381431019, -2.9532549036308726] | {'down': 0.3374991424462517, 'flat': 0.18088281218096397, 'up': 0.48161804537278435} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3374991424462517, 'flat': 0.18088281218096397, 'up': 0.48161804537278435} | [-1.7930213182669408, -0.050371912549596054, 1.8433932308165368] | {'down': 0.3369954233207557, 'flat': 0.19931674448912934, 'up': 0.46368783219011495} |
| 8 | E13/history | [] | {'down': 0.3369954233207557, 'flat': 0.19931674448912934, 'up': 0.46368783219011495} | [0.0, 0.0, 0.0] | {'down': 0.3369954233207557, 'flat': 0.19931674448912934, 'up': 0.46368783219011495} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3369954233207557, 'flat': 0.19931674448912934, 'up': 0.46368783219011495} | [-1.6772274747355376, 0.1616509279278533, 1.515576546807687] | {'down': 0.33861193260003425, 'flat': 0.2144725099572062, 'up': 0.44691555744275957} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '03fb4d91bbf79b760d50306ad25f276098d96579eff6e5c084501e2b76bdae61'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:d59c556fe3a61dcfc9dbe033a02ecd8f9fdfd6111a35a7c4521c13ab416bd499'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f78e14959ab483dd686e92299ab5188f4659cce165419c1be7f6cacff5be8a37#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1ccf7c83b195e35cff5d94dbebd37465b830b82e80a54826acbf1ca43d451ef1#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d8f1af7e03ae00b02709464ca239fa177a79787cea93900b5d86de0a19c87291#us_10y_yield@2026-09-03T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "ad9cf183-cd34-512e-8386-d8436b2e28e4/1y/technical",
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
    "atr": 25575.479086468946,
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
    "rsi": 56.03519597017332,
    "sma": [
      190905.0,
      124510.83333333333,
      87986.25
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
    "volume_ratio": 0.5330666693133895
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'ad9cf183-cd34-512e-8386-d8436b2e28e4/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "259a4c0e-ef73-5642-b7cb-c3c51dbdc50e",
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
    "hypothesis_id": "259a4c0e-ef73-5642-b7cb-c3c51dbdc50e",
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
    "hypothesis_id": "259a4c0e-ef73-5642-b7cb-c3c51dbdc50e",
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
    "hypothesis_id": "259a4c0e-ef73-5642-b7cb-c3c51dbdc50e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.18394874613637047
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
    "hypothesis_id": "eccc3c06-d447-546e-b821-816e4f3460b6",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7695000000000002
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
