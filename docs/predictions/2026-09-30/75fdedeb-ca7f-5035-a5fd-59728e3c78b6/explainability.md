# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 75fdedeb-ca7f-5035-a5fd-59728e3c78b6
Cutoff / prediction: 2026-09-29T22:00:14.081372+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-29T06:30:00+00:00', 'source_refs': ['raw:2dfa06b6e9b3da090e45e05c01885b4fe224673a95a886f2dfc2ea7497b82b1f'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 204000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 40.0768% | 38.1029% | 21.8203% | 5.1886% | 0.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 41.0462% | 36.7500% | 22.2038% | 4.2665% | 45.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 40.0768% / 38.1029% / 21.8203% | 40.0768% / 38.1029% / 21.8203% | [0.0, 0.0, 0.0] |
| 1m | 39.4298% / 38.2495% / 22.3207% | 41.0462% / 36.7500% / 22.2038% | [1.6164223765727626, -1.4994642397814284, -0.11695813679132028] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503911492222223,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:13.111959Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-29T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2dfa06b6e9b3da090e45e05c01885b4fe224673a95a886f2dfc2ea7497b82b1f",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503911492222223,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:13.604740Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-29T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57",
    "reason": null,
    "released_at": null,
    "rows": 4930,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503911492222223,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:13.541019Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-29T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5039114922222225,
    "authority": "official_original",
    "collected_at": "2026-09-29T22:00:13.172250Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-29T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b",
    "reason": null,
    "released_at": null,
    "rows": 187,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:13.636782Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "779dbf09991e79f7f6e0133f63f49c3f8e6e3b93802dfd330706c85e996eed08",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503911492222215,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:13.604740Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-28T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "a3a79d80f42ec6efdc769674e89bf0abee70f1ece967cc256328a5d679405a02",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-29T22:00:14.081372Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "4c3bfa0bec78f8331b2ddbb09f2b1c599e1ba4498e91ad331b1fde95fb8ef317",
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
    "collected_at": "2026-09-29T22:00:13.604740Z",
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
    "collected_at": "2026-09-29T22:00:13.604740Z",
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
    "collected_at": "2026-09-29T22:00:13.604740Z",
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
    "collected_at": "2026-09-29T22:00:13.604740Z",
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
Document statuses: {'dram_spot': 'available_unmapped', 'exports_10': 'stale', 'exports_20': 'available_unmapped', 'exports_month': 'available_unmapped', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 4930, 'last': '2026-09-29T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-25T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-09-29T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a3a79d80f42ec6efdc769674e89bf0abee70f1ece967cc256328a5d679405a02'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-22T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1w/technical",
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
    "atr": 9924.518022538101,
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
      4913,
      4921
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 54.188918868379865,
    "sma": [
      196740.0,
      188236.66666666666,
      185816.66666666666
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
      4918,
      4927
    ],
    "top_score": 0.0,
    "volume_ratio": 1.0509198394781363
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 2261.0378472916427,
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
    "bottom_neckline": 207000.0,
    "bottom_pivots": [
      228,
      236
    ],
    "bottom_score": 0.0,
    "rsi": 44.37013219162456,
    "sma": [
      204475.0,
      210016.66666666666,
      201010.41666666666
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
    "top_neckline": 201500.0,
    "top_pivots": [
      225,
      231
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "8967cfea-2658-503e-96ac-b633bf9774d6",
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
    "hypothesis_id": "8967cfea-2658-503e-96ac-b633bf9774d6",
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
    "hypothesis_id": "8967cfea-2658-503e-96ac-b633bf9774d6",
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
    "hypothesis_id": "8967cfea-2658-503e-96ac-b633bf9774d6",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.05655040472312819
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8967cfea-2658-503e-96ac-b633bf9774d6",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.02577727598105948
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
    "hypothesis_id": "49b8fc3b-2654-53be-af2e-57f422eb048c",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.3956049269790485, -0.2973389617449973, -0.09826596523405118] | {'down': 0.34702661038255, 'flat': 0.2490173403476595, 'up': 0.4039560492697905} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34702661038255, 'flat': 0.2490173403476595, 'up': 0.4039560492697905} | [2.8632139878164375, -2.1222245987532693, -0.740989389063168] | {'down': 0.3258043643950173, 'flat': 0.2416074464570278, 'up': 0.4325881891479549} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3258043643950173, 'flat': 0.2416074464570278, 'up': 0.4325881891479549} | [0.18376545333027572, -0.13447402482557602, -0.04929142850470247] | {'down': 0.32445962414676155, 'flat': 0.24111453217198078, 'up': 0.43442584368125764} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.32445962414676155, 'flat': 0.24111453217198078, 'up': 0.43442584368125764} | [2.418377271508559, -1.751067843429266, -0.6673094280792963] | {'down': 0.3069489457124689, 'flat': 0.23444143789118782, 'up': 0.45860961639634323} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3069489457124689, 'flat': 0.23444143789118782, 'up': 0.45860961639634323} | [2.4334281749158415, -1.7282857997401646, -0.7051423751756686] | {'down': 0.28966608771506724, 'flat': 0.22739001413943113, 'up': 0.48294389814550165} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.28966608771506724, 'flat': 0.22739001413943113, 'up': 0.48294389814550165} | [-7.568178023614131, 8.90929984497461, -1.3411218213604803] | {'down': 0.37875908616481335, 'flat': 0.21397879592582633, 'up': 0.40726211790936034} |
| 6 | E10/causal | ['75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1w/technical'] | {'down': 0.37875908616481335, 'flat': 0.21397879592582633, 'up': 0.40726211790936034} | [0.7946953448786542, -0.7790921439169596, -0.015603200961702979] | {'down': 0.37096816472564376, 'flat': 0.2138227639162093, 'up': 0.4152090713581469} |
| 7 | E17/scenario | ['0aa445de-14c2-5af1-8662-21f992e3aea6', '2664ece5-a325-5f7a-96dd-a4a7538518cb', 'dad252b6-0827-53f2-a4fd-be8f1878ed21', '8bcc63da-7385-556d-81bb-67d4c2c0e827'] | {'down': 0.37096816472564376, 'flat': 0.2138227639162093, 'up': 0.4152090713581469} | [0.6026404314379452, 2.3666335769526095, -2.969274008390549] | {'down': 0.39463450049516985, 'flat': 0.1841300238323038, 'up': 0.42123547567252634} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.39463450049516985, 'flat': 0.1841300238323038, 'up': 0.42123547567252634} | [-1.1496116554081226, -0.8017157987735113, 1.9513274541816257] | {'down': 0.38661734250743474, 'flat': 0.20364329837412007, 'up': 0.4097393591184451} |
| 9 | E13/history | [] | {'down': 0.38661734250743474, 'flat': 0.20364329837412007, 'up': 0.4097393591184451} | [0.0, 0.0, 0.0] | {'down': 0.38661734250743474, 'flat': 0.20364329837412007, 'up': 0.4097393591184451} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.38661734250743474, 'flat': 0.20364329837412007, 'up': 0.4097393591184451} | [-0.8970955392911373, -0.5588794258772789, 1.4559749651684217] | {'down': 0.38102854824866195, 'flat': 0.21820304802580429, 'up': 0.40076840372553374} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a3a79d80f42ec6efdc769674e89bf0abee70f1ece967cc256328a5d679405a02'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-22T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1m/technical",
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
    "atr": 24085.97942892576,
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
      1026,
      1033
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1028,
      1036
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  },
  "primary": "1d",
  "reflexivity_effect": 0.04500000000000001,
  "regime_effect": 0.0675,
  "sell_liquidity": null,
  "wave": {
    "atr": 9924.518022538101,
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
      4913,
      4921
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 54.188918868379865,
    "sma": [
      196740.0,
      188236.66666666666,
      185816.66666666666
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
      4918,
      4927
    ],
    "top_score": 0.0,
    "volume_ratio": 1.0509198394781363
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.04500000000000001, 'regime_effect': 0.0675}
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
    "hypothesis_id": "102aeb3a-874a-5799-a789-08b18fbf2f7f",
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
    "hypothesis_id": "102aeb3a-874a-5799-a789-08b18fbf2f7f",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "102aeb3a-874a-5799-a789-08b18fbf2f7f",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.45967499999999994
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "102aeb3a-874a-5799-a789-08b18fbf2f7f",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.11122540472312821
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "102aeb3a-874a-5799-a789-08b18fbf2f7f",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.0804522759810595
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
    "hypothesis_id": "fc77edf6-34ba-5394-98df-f08fe4a77f9e",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.30248735872706045, -0.22744363033253, -0.07504372839453322] | {'down': 0.3477255636966747, 'flat': 0.24924956271605467, 'up': 0.4030248735872706} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3477255636966747, 'flat': 0.24924956271605467, 'up': 0.4030248735872706} | [1.2569573484830787, -0.9387616705198776, -0.3181956779631928] | {'down': 0.3383379469914759, 'flat': 0.24606760593642274, 'up': 0.4155944470721014} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3383379469914759, 'flat': 0.24606760593642274, 'up': 0.4155944470721014} | [0.22104741606880363, -0.16404729139530283, -0.05700012467351745] | {'down': 0.3366974740775229, 'flat': 0.24549760468968757, 'up': 0.41780492123278945} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.3366974740775229, 'flat': 0.24549760468968757, 'up': 0.41780492123278945} | [1.9188215593689717, -1.4113113266716049, -0.5075102326973641] | {'down': 0.3225843608108068, 'flat': 0.24042250236271392, 'up': 0.43699313682647917} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3225843608108068, 'flat': 0.24042250236271392, 'up': 0.43699313682647917} | [1.9349473711545218, -1.4008392859409635, -0.5341080852135499] | {'down': 0.3085759679513972, 'flat': 0.23508142151057843, 'up': 0.4563426105380244} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.3085759679513972, 'flat': 0.23508142151057843, 'up': 0.4563426105380244} | [-5.616428728159006, 6.742649812215623, -1.1262210840566222] | {'down': 0.3760024660735534, 'flat': 0.2238192106700122, 'up': 0.4001783232564343} |
| 6 | E10/causal | ['75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1m/technical'] | {'down': 0.3760024660735534, 'flat': 0.2238192106700122, 'up': 0.4001783232564343} | [2.8189667812737795, -2.735587001079298, -0.08337978019447023] | {'down': 0.34864659606276044, 'flat': 0.2229854128680675, 'up': 0.4283679910691721} |
| 7 | E17/scenario | ['6babffbd-fc00-51ec-a2ea-c7b50f03fd3a', '37a715e9-d949-5683-9432-afbb82a77e97', '002c184a-1f94-50a1-a53e-1e8939a696a7', 'da40491e-8f00-5f72-9d2e-269c232c97cf'] | {'down': 0.34864659606276044, 'flat': 0.2229854128680675, 'up': 0.4283679910691721} | [0.6068484159391485, 2.794832260717628, -3.4016806766567904] | {'down': 0.3765949186699367, 'flat': 0.1889686061014996, 'up': 0.4344364752285636} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3765949186699367, 'flat': 0.1889686061014996, 'up': 0.4344364752285636} | [-1.3193085304105012, -0.5645262600524115, 1.8838347904629211] | {'down': 0.3709496560694126, 'flat': 0.2078069540061288, 'up': 0.4212433899244586} |
| 9 | E13/history | [] | {'down': 0.3709496560694126, 'flat': 0.2078069540061288, 'up': 0.4212433899244586} | [0.0, 0.0, 0.0] | {'down': 0.3709496560694126, 'flat': 0.2078069540061288, 'up': 0.4212433899244586} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3709496560694126, 'flat': 0.2078069540061288, 'up': 0.4212433899244586} | [-1.0781242586538786, -0.3449649802856669, 1.423089238939551] | {'down': 0.36750000626655593, 'flat': 0.22203784639552432, 'up': 0.4104621473379198} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '06667e976572415c19c8989366e7a710ea156a8abab35958a46cfe3806bd88ba'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a3a79d80f42ec6efdc769674e89bf0abee70f1ece967cc256328a5d679405a02'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_rsi_14@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_trend_alignment@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#preferred_volume_z@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:87b57eb8b124de278240d03ed0107a09b1ce21b358a008fefe66536bbff5313f#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:14d3b6ffdc3ca6928a87b5b24cfdefe77e105c85e5f25808565ab280d2946d57#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:fd7d64e19b9fced33e0d2a5e04b6863642c0efbd913280391c120cd66dedf69b#us_10y_yield@2026-09-22T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1y/technical",
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
    "atr": 24085.97942892576,
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
      1026,
      1033
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1028,
      1036
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '75fdedeb-ca7f-5035-a5fd-59728e3c78b6/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "c29d8b9d-7695-541e-8311-cf99d2d233d8",
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
    "hypothesis_id": "c29d8b9d-7695-541e-8311-cf99d2d233d8",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c29d8b9d-7695-541e-8311-cf99d2d233d8",
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
    "hypothesis_id": "c29d8b9d-7695-541e-8311-cf99d2d233d8",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.04440040472312819
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c29d8b9d-7695-541e-8311-cf99d2d233d8",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.013627275981059476
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
    "hypothesis_id": "58edd588-bd15-56dd-8b0c-ae796ab1fd21",
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
