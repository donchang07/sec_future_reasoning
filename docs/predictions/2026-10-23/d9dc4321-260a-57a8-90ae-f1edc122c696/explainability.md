# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: d9dc4321-260a-57a8-90ae-f1edc122c696
Cutoff / prediction: 2026-10-22T22:00:13.189667+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-22T06:30:00+00:00', 'source_refs': ['raw:5d969209683f0f11512990b82a0736d32bf6c06832fc19c60eba969708df6144'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 167100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 36.2776% | 42.4673% | 21.2550% | 6.4894% | 0.0000% | 65.0000% | 0.0/0.8 | None/None | WAIT |
| 1m | 38.8109% | 39.2441% | 21.9450% | 3.1984% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.2357% / 39.2903% / 21.4740% | 36.2776% / 42.4673% / 21.2550% | [-2.9580467322526447, 3.1770540140337253, -0.21900728178108064] |
| 1m | 40.0356% / 38.0273% / 21.9371% | 38.8109% / 39.2441% / 21.9450% | [-1.224693113472869, 1.2168141796223275, 0.007878933850541392] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503663796388889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-22T22:00:12.516070Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "5d969209683f0f11512990b82a0736d32bf6c06832fc19c60eba969708df6144",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503663796388889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-22T22:00:12.774005Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503663796388889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-22T22:00:12.844931Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503663796388889,
    "authority": "official_original",
    "collected_at": "2026-10-22T22:00:12.473570Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-22T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9",
    "reason": null,
    "released_at": null,
    "rows": 203,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-22T22:00:12.934447Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "bfe2f8c45c954007b15afac6e912f002794ea417b1157ec4aa583a9532e5120a",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 63.503663796388885,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-22T22:00:13.007648Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-20T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "4ba912d2da75d96d26abdada1854c51ae2398934d4c5c8532cb50e49e9047955",
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
    "collected_at": "2026-10-22T22:00:13.189667Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "c234b9b3bb537458c8b36b83310c85787670e92b5a607795c3d3d61898eeea99",
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
    "collected_at": "2026-10-22T22:00:12.845931Z",
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
    "collected_at": "2026-10-22T22:00:12.845931Z",
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
    "collected_at": "2026-10-22T22:00:12.845931Z",
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
    "collected_at": "2026-10-22T22:00:12.845931Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-10-22T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-16T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-22T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:4ba912d2da75d96d26abdada1854c51ae2398934d4c5c8532cb50e49e9047955'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "d9dc4321-260a-57a8-90ae-f1edc122c696/1w/technical",
  "bearish_alignment": 0.8,
  "bullish_alignment": 0.0,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 10785.885044476718,
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
    "bottom_neckline": 204500.0,
    "bottom_pivots": [
      4918,
      4926
    ],
    "bottom_score": 0.0,
    "rsi": 39.62940639467188,
    "sma": [
      188925.0,
      186623.33333333334,
      190829.16666666666
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
      4905,
      4914
    ],
    "top_score": 0.35,
    "volume_ratio": 0.5754308939137739
  },
  "primary": "30m",
  "reflexivity_effect": -0.065,
  "regime_effect": -0.0975,
  "sell_liquidity": null,
  "wave": {
    "atr": 2054.6661689711896,
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
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      190,
      200
    ],
    "bottom_score": 0.0,
    "rsi": 43.41349042553601,
    "sma": [
      169650.0,
      169134.16666666666,
      174024.16666666666
    ],
    "top_confirmed": true,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 168900.0,
    "top_pivots": [
      193,
      205
    ],
    "top_score": 0.65,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'd9dc4321-260a-57a8-90ae-f1edc122c696/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.065, 'regime_effect': -0.0975}
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
    "hypothesis_id": "814adf49-dafd-5294-81dc-57edcefaebb3",
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
    "hypothesis_id": "814adf49-dafd-5294-81dc-57edcefaebb3",
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
    "hypothesis_id": "d6ccc342-6845-5f89-9fd4-9f0163bfe90d",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d6ccc342-6845-5f89-9fd4-9f0163bfe90d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.5169310273438592
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-2.781277022517542, 3.522074424844207, -0.7407974023266595] | {'down': 0.38522074424844205, 'flat': 0.2425920259767334, 'up': 0.3721872297748246} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.38522074424844205, 'flat': 0.2425920259767334, 'up': 0.3721872297748246} | [4.7250788587335615, -3.658496599819533, -1.0665822589140284] | {'down': 0.3486357782502467, 'flat': 0.23192620338759312, 'up': 0.4194380183621602} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3486357782502467, 'flat': 0.23192620338759312, 'up': 0.4194380183621602} | [4.859621324486035, -3.6216559468351175, -1.2379653776509096] | {'down': 0.31241921878189555, 'flat': 0.21954654961108402, 'up': 0.46803423160702057} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.31241921878189555, 'flat': 0.21954654961108402, 'up': 0.46803423160702057} | [-7.404992378200914, 8.826994690414814, -1.422002312213913] | {'down': 0.4006891656860437, 'flat': 0.2053265264889449, 'up': 0.3939843078250114} |
| 4 | E10/causal | ['d9dc4321-260a-57a8-90ae-f1edc122c696/1w/technical'] | {'down': 0.4006891656860437, 'flat': 0.2053265264889449, 'up': 0.3939843078250114} | [-3.383954742862738, 3.4563509331888955, -0.07239619032615718] | {'down': 0.43525267501793263, 'flat': 0.20460256458568332, 'up': 0.36014476039638404} |
| 5 | E17/scenario | ['cf8cdd3c-57de-5faf-a9d8-296f342ab1f6', '42562174-cfcf-55a8-ad60-ee6800a3b3fa', '336d60d9-efb3-513e-9f08-24604f82ca8b', '943c0beb-4ab3-536e-99fd-9fa14508f618'] | {'down': 0.43525267501793263, 'flat': 0.20460256458568332, 'up': 0.36014476039638404} | [0.9474730187585323, 1.7318827810592852, -2.679355799817812] | {'down': 0.4525715028285255, 'flat': 0.1778090065875052, 'up': 0.36961949058396937} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4525715028285255, 'flat': 0.1778090065875052, 'up': 0.36961949058396937} | [-0.45707964962192205, -1.501987117510678, 1.9590667671326056] | {'down': 0.4375516316534187, 'flat': 0.19739967425883126, 'up': 0.36504869408775015} |
| 7 | E13/history | [] | {'down': 0.4375516316534187, 'flat': 0.19739967425883126, 'up': 0.36504869408775015} | [0.0, 0.0, 0.0] | {'down': 0.4375516316534187, 'flat': 0.19739967425883126, 'up': 0.36504869408775015} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.4375516316534187, 'flat': 0.19739967425883126, 'up': 0.36504869408775015} | [-0.22722801953408145, -1.2878154814528642, 1.515043500986943] | {'down': 0.42467347683889006, 'flat': 0.2125501092687007, 'up': 0.36277641389240933} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.207765
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:4ba912d2da75d96d26abdada1854c51ae2398934d4c5c8532cb50e49e9047955'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "d9dc4321-260a-57a8-90ae-f1edc122c696/1m/technical",
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
    "atr": 24540.23207192051,
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
      1023,
      1030
    ],
    "bottom_score": 0.0,
    "rsi": 45.79911672763005,
    "sma": [
      196280.0,
      138369.16666666666,
      94608.75
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
      1033,
      1038
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 10785.885044476718,
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
    "bottom_neckline": 204500.0,
    "bottom_pivots": [
      4918,
      4926
    ],
    "bottom_score": 0.0,
    "rsi": 39.62940639467188,
    "sma": [
      188925.0,
      186623.33333333334,
      190829.16666666666
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
      4905,
      4914
    ],
    "top_score": 0.35,
    "volume_ratio": 0.5754308939137739
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'd9dc4321-260a-57a8-90ae-f1edc122c696/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "542a8684-726b-54cc-ae17-3522cce064b6",
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
    "hypothesis_id": "542a8684-726b-54cc-ae17-3522cce064b6",
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
    "hypothesis_id": "1d2b2144-cf2a-548f-ae5d-65bbcce84d59",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1d2b2144-cf2a-548f-ae5d-65bbcce84d59",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.40758102734385915
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.850938223040193, 1.0657235269059262, -0.21478530386573325] | {'down': 0.36065723526905924, 'flat': 0.24785214696134267, 'up': 0.3914906177695981} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.36065723526905924, 'flat': 0.24785214696134267, 'up': 0.3914906177695981} | [3.8055590231178216, -2.8619112021121773, -0.9436478210056498] | {'down': 0.33203812324793747, 'flat': 0.23841566875128617, 'up': 0.4295462080007763} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33203812324793747, 'flat': 0.23841566875128617, 'up': 0.4295462080007763} | [3.8790498502638773, -2.827081778402696, -1.0519680718611868] | {'down': 0.3037673054639105, 'flat': 0.2278959880326743, 'up': 0.4683367065034151} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.3037673054639105, 'flat': 0.2278959880326743, 'up': 0.4683367065034151} | [-5.443942935221652, 6.438439781553395, -0.9944968463317355] | {'down': 0.36815170327944446, 'flat': 0.21795101956935695, 'up': 0.41389727715119856} |
| 4 | E10/causal | ['d9dc4321-260a-57a8-90ae-f1edc122c696/1m/technical'] | {'down': 0.36815170327944446, 'flat': 0.21795101956935695, 'up': 0.41389727715119856} | [-2.036350004490828, 2.007518625245158, 0.02883137924565571] | {'down': 0.38822688953189605, 'flat': 0.2182393333618135, 'up': 0.3935337771062903} |
| 5 | E17/scenario | ['0df78d10-b3ec-596b-895e-98308b5cdf4f', 'ece5834b-aac2-5c30-94eb-65f86580be2b', '57cac1b1-1f87-5d0c-8025-7ed3af21f30a', 'd8838320-1de9-50d5-a0a2-67abf1c40a00'] | {'down': 0.38822688953189605, 'flat': 0.2182393333618135, 'up': 0.3935337771062903} | [1.0378006118741512, 2.149723828780953, -3.1875244406550847] | {'down': 0.4097241278197056, 'flat': 0.18636408895526266, 'up': 0.4039117832250318} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4097241278197056, 'flat': 0.18636408895526266, 'up': 0.4039117832250318} | [-0.8957026834398696, -0.9694664549383225, 1.8651691383781892] | {'down': 0.40002946327032235, 'flat': 0.20501578033904455, 'up': 0.3949547563906331} |
| 7 | E13/history | [] | {'down': 0.40002946327032235, 'flat': 0.20501578033904455, 'up': 0.3949547563906331} | [0.0, 0.0, 0.0] | {'down': 0.40002946327032235, 'flat': 0.20501578033904455, 'up': 0.3949547563906331} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.40002946327032235, 'flat': 0.20501578033904455, 'up': 0.3949547563906331} | [-0.6846157180004198, -0.7588183075462329, 1.44343402554665] | {'down': 0.39244128019486, 'flat': 0.21945012059451105, 'up': 0.3881085992106289} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.0, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '6bcf7a7c675a6fa72e854f3d1febdf3a75f9003f6a84d75982e3dba52a9f545b'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:4ba912d2da75d96d26abdada1854c51ae2398934d4c5c8532cb50e49e9047955'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:4265bc75d3a2a859a6d9f783ef3ae027006b120092e4ae10d70815b13e3deed2#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2e1788e266da4bc330bfd7c2b7da8e3a0e4aa0bb0af42414e0780602d7bd0ebd#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:88116418e55d686baaba6095c2f6783148ec6824f4d8d36589aba7bb01f9a5c9#us_10y_yield@2026-10-15T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "d9dc4321-260a-57a8-90ae-f1edc122c696/1y/technical",
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
    "atr": 24540.23207192051,
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
      1023,
      1030
    ],
    "bottom_score": 0.0,
    "rsi": 45.79911672763005,
    "sma": [
      196280.0,
      138369.16666666666,
      94608.75
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
      1033,
      1038
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'd9dc4321-260a-57a8-90ae-f1edc122c696/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "889bf8de-b56a-5353-82a4-3a6acbc10218",
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
    "hypothesis_id": "889bf8de-b56a-5353-82a4-3a6acbc10218",
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
    "hypothesis_id": "d68bc063-c0c4-566d-828c-067ce9d6fe33",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d68bc063-c0c4-566d-828c-067ce9d6fe33",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.35290602734385923
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
