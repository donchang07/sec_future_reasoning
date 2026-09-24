# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 37cc806b-7584-5973-a781-a53124b6fafb
Cutoff / prediction: 2026-09-24T22:00:13.856994+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-23T06:30:00+00:00', 'source_refs': ['raw:2b3d86553c5968e3fc930b046e7c2adc27317c0f8f87df064fb7da2ec6763a77'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 220000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 47.6855% | 31.9378% | 20.3767% | 7.4173% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 44.6374% | 33.8795% | 21.4831% | 5.7812% | 65.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 48.1960% / 31.5201% / 20.2839% | 47.6855% / 31.9378% / 20.3767% | [-0.5105143245113686, 0.417732294189449, 0.09278203032193622] |
| 1m | 43.7290% / 34.6914% / 21.5796% | 44.6374% / 33.8795% / 21.4831% | [0.9083953943445466, -0.8118491891179302, -0.09654620522661361] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 39.503849165,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-24T22:00:12.969806Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2b3d86553c5968e3fc930b046e7c2adc27317c0f8f87df064fb7da2ec6763a77",
    "reason": null,
    "released_at": null,
    "rows": 277,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.503849165,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-24T22:00:13.300584Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.503849165,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-24T22:00:13.399411Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503849165,
    "authority": "official_original",
    "collected_at": "2026-09-24T22:00:13.093360Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-24T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20",
    "reason": null,
    "released_at": null,
    "rows": 184,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-24T22:00:13.497608Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "ee3aa2b6386c91c8a5c57d59a10c8aee1d744f1d5d43408ee25e1799306e3146",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503849165,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-24T22:00:13.654654Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c37796e23df24ee93f19498818dd5877c019d193a0117fb55a6395120708710d",
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
    "collected_at": "2026-09-24T22:00:13.856994Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "75b55439b917aabf264971e1dac438b74fc79e60144be3d95d98261d3ab2b4c3",
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
    "collected_at": "2026-09-24T22:00:13.399411Z",
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
    "collected_at": "2026-09-24T22:00:13.399411Z",
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
    "collected_at": "2026-09-24T22:00:13.399411Z",
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
    "collected_at": "2026-09-24T22:00:13.399411Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-23T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-18T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-23T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c37796e23df24ee93f19498818dd5877c019d193a0117fb55a6395120708710d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-17T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "37cc806b-7584-5973-a781-a53124b6fafb/1w/technical",
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
    "atr": 9883.464688860755,
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
    "rsi": 64.68247187439766,
    "sma": [
      195245.0,
      188328.33333333334,
      184442.5
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
    "volume_ratio": 1.688807602541006
  },
  "primary": "30m",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1762.1091635620198,
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
      263,
      269
    ],
    "bottom_score": 0.0,
    "rsi": 71.33035351706422,
    "sma": [
      216850.0,
      206302.5,
      199028.33333333334
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
    "top_neckline": 210000.0,
    "top_pivots": [
      260,
      267
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '37cc806b-7584-5973-a781-a53124b6fafb/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "db4bb502-ddc1-5d8b-810a-e62c1b52becb",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.59535
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "db4bb502-ddc1-5d8b-810a-e62c1b52becb",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.59535
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "db4bb502-ddc1-5d8b-810a-e62c1b52becb",
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
    "hypothesis_id": "db4bb502-ddc1-5d8b-810a-e62c1b52becb",
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
    "hypothesis_id": "db4bb502-ddc1-5d8b-810a-e62c1b52becb",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.28517005545655266
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
    "hypothesis_id": "c1a6119c-be4a-5325-8aa4-845a637cadef",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [2.0059324151515066, -1.49724371380619, -0.508688701345314] | {'down': 0.3350275628619381, 'flat': 0.24491311298654686, 'up': 0.4200593241515151} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3350275628619381, 'flat': 0.24491311298654686, 'up': 0.4200593241515151} | [4.255850660420157, -3.0948137456279334, -1.161036914792235] | {'down': 0.30407942540565874, 'flat': 0.2333027438386245, 'up': 0.46261783075571666} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.30407942540565874, 'flat': 0.2333027438386245, 'up': 0.46261783075571666} | [4.296668907937967, -3.020391780768017, -1.2762771271699362] | {'down': 0.2738755075979786, 'flat': 0.22053997256692515, 'up': 0.5055845198350963} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.2738755075979786, 'flat': 0.22053997256692515, 'up': 0.5055845198350963} | [3.6383577245544862, -2.4817722155669575, -1.1565855089875372] | {'down': 0.249057785442309, 'flat': 0.20897411747704978, 'up': 0.5419680970806412} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.249057785442309, 'flat': 0.20897411747704978, 'up': 0.5419680970806412} | [3.5839096310098406, -2.380181230877107, -1.2037284001327335] | {'down': 0.22525597313353793, 'flat': 0.19693683347572244, 'up': 0.5778071933907396} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.22525597313353793, 'flat': 0.19693683347572244, 'up': 0.5778071933907396} | [-7.3981667066970624, 7.929613718723918, -0.5314470120268477] | {'down': 0.3045521103207771, 'flat': 0.19162236335545396, 'up': 0.503825526323769} |
| 6 | E10/causal | ['37cc806b-7584-5973-a781-a53124b6fafb/1w/technical'] | {'down': 0.3045521103207771, 'flat': 0.19162236335545396, 'up': 0.503825526323769} | [2.0373793327021272, -1.8259791416630478, -0.21140019103908225] | {'down': 0.28629231890414664, 'flat': 0.18950836144506314, 'up': 0.5241993196507903} |
| 7 | E17/scenario | ['0ff1b5fd-8bd2-5167-b45a-6354ededc6ab', '8779a96d-0332-5473-9425-8badb6b838da', 'ef8e9a1d-d5d7-5169-9ae3-4c321580a0ec', '7b8e2557-0408-5c3b-b535-c70532bb9b2f'] | {'down': 0.28629231890414664, 'flat': 0.18950836144506314, 'up': 0.5241993196507903} | [-0.2864315413659724, 2.5311116680206913, -2.2446801266547247] | {'down': 0.31160343558435355, 'flat': 0.1670615601785159, 'up': 0.5213350042371305} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.31160343558435355, 'flat': 0.1670615601785159, 'up': 0.5213350042371305} | [-2.303556833969572, 0.2662532424338726, 2.037303591535691] | {'down': 0.3142659680086923, 'flat': 0.1874345960938728, 'up': 0.4982994358974348} |
| 9 | E13/history | [] | {'down': 0.3142659680086923, 'flat': 0.1874345960938728, 'up': 0.4982994358974348} | [0.0, 0.0, 0.0] | {'down': 0.3142659680086923, 'flat': 0.1874345960938728, 'up': 0.4982994358974348} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3142659680086923, 'flat': 0.1874345960938728, 'up': 0.4982994358974348} | [-2.1444535289597946, 0.5112287379733627, 1.6332247909864512] | {'down': 0.3193782553884259, 'flat': 0.20376684400373732, 'up': 0.47685490060783686} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c37796e23df24ee93f19498818dd5877c019d193a0117fb55a6395120708710d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-17T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "37cc806b-7584-5973-a781-a53124b6fafb/1m/technical",
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
    "atr": 9883.464688860755,
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
    "rsi": 64.68247187439766,
    "sma": [
      195245.0,
      188328.33333333334,
      184442.5
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
    "volume_ratio": 1.688807602541006
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '37cc806b-7584-5973-a781-a53124b6fafb/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "8344f614-3c12-5c95-aa20-8dffe8855438",
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
    "hypothesis_id": "8344f614-3c12-5c95-aa20-8dffe8855438",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8344f614-3c12-5c95-aa20-8dffe8855438",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.6378750000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8344f614-3c12-5c95-aa20-8dffe8855438",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6378750000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8344f614-3c12-5c95-aa20-8dffe8855438",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.32769505545655264
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
    "hypothesis_id": "00f88c86-3939-5e82-bfcf-d49bcc7b7201",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.8930882302695453, -0.6698013491547972, -0.22328688111474815] | {'down': 0.343301986508452, 'flat': 0.24776713118885252, 'up': 0.4089308823026955} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.343301986508452, 'flat': 0.24776713118885252, 'up': 0.4089308823026955} | [1.7534553864699098, -1.3002375773248864, -0.45321780914502063] | {'down': 0.33029961073520314, 'flat': 0.2432349530974023, 'up': 0.4264654361673946} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.33029961073520314, 'flat': 0.2432349530974023, 'up': 0.4264654361673946} | [1.7696914764312843, -1.2931137344712684, -0.4765777419600048] | {'down': 0.31736847339049046, 'flat': 0.23846917567780226, 'up': 0.4441623509317074} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.31736847339049046, 'flat': 0.23846917567780226, 'up': 0.4441623509317074} | [2.9126188706117495, -2.0884238154534773, -0.824195055158275] | {'down': 0.2964842352359557, 'flat': 0.23022722512621951, 'up': 0.4732885396378249} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.2964842352359557, 'flat': 0.23022722512621951, 'up': 0.4732885396378249} | [2.9242571748751334, -2.0494996231615437, -0.8747575517135925] | {'down': 0.27598923900434025, 'flat': 0.2214796496090836, 'up': 0.5025311113865762} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.27598923900434025, 'flat': 0.2214796496090836, 'up': 0.5025311113865762} | [-5.642720872695079, 6.444346425383696, -0.8016255526886201] | {'down': 0.3404327032581772, 'flat': 0.2134633940821974, 'up': 0.44610390265962546} |
| 6 | E10/causal | ['37cc806b-7584-5973-a781-a53124b6fafb/1m/technical'] | {'down': 0.3404327032581772, 'flat': 0.2134633940821974, 'up': 0.44610390265962546} | [3.6276941429007725, -3.356131680164398, -0.2715624627363855] | {'down': 0.3068713864565332, 'flat': 0.21074776945483353, 'up': 0.4823808440886332} |
| 7 | E17/scenario | ['66fedae9-1071-507f-8e7b-8796c75e7633', 'afb3cef4-cdd2-5124-bff2-845da8ab06e4', '674ce9a5-765c-5b09-9425-4ff3255c2ddd', '0c957e60-08db-5e65-9209-dc38f7238396'] | {'down': 0.3068713864565332, 'flat': 0.21074776945483353, 'up': 0.4823808440886332} | [-0.10238540302507926, 3.090014313326084, -2.987628910300999] | {'down': 0.33777152958979406, 'flat': 0.18087148035182354, 'up': 0.4813569900583824} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.33777152958979406, 'flat': 0.18087148035182354, 'up': 0.4813569900583824} | [-1.8290618738949826, -0.05484079870174963, 1.8839026725967378] | {'down': 0.33722312160277657, 'flat': 0.19971050707779092, 'up': 0.46306637131943257} |
| 9 | E13/history | [] | {'down': 0.33722312160277657, 'flat': 0.19971050707779092, 'up': 0.46306637131943257} | [0.0, 0.0, 0.0] | {'down': 0.33722312160277657, 'flat': 0.19971050707779092, 'up': 0.46306637131943257} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.33722312160277657, 'flat': 0.19971050707779092, 'up': 0.46306637131943257} | [-1.6692438631060624, 0.15720199413480906, 1.5120418689712505] | {'down': 0.33879514154412466, 'flat': 0.21483092576750343, 'up': 0.44637393268837194} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '5e7a6215442420c6eefa224ac6725467f9d5ab648be417790c7ea624eea80e8b'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c37796e23df24ee93f19498818dd5877c019d193a0117fb55a6395120708710d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:65961cb0bda47a16e7e30c27370121f932083dc33fa2ffeeb9e5d73dac6130a6#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:592f0f8d272efa9dfe15980f7877d6b1d272bc5d29bc9d7247b0b29172f9d3f9#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:55ef947f24f1de75e226a8fc628aebb527f7cae705dc3d212f16524c4f2faa20#us_10y_yield@2026-09-17T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "37cc806b-7584-5973-a781-a53124b6fafb/1y/technical",
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
Feedback applied once: {'batch_id': '37cc806b-7584-5973-a781-a53124b6fafb/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "d0bbc149-1c08-590a-9b7f-86ec64f83521",
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
    "hypothesis_id": "d0bbc149-1c08-590a-9b7f-86ec64f83521",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d0bbc149-1c08-590a-9b7f-86ec64f83521",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.59535
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d0bbc149-1c08-590a-9b7f-86ec64f83521",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.59535
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d0bbc149-1c08-590a-9b7f-86ec64f83521",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.28517005545655266
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
    "hypothesis_id": "82970630-b8c1-5f30-bbee-8da9aac99fda",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
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
