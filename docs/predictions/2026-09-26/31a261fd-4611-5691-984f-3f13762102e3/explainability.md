# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 31a261fd-4611-5691-984f-3f13762102e3
Cutoff / prediction: 2026-09-25T22:00:12.945347+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-23T06:30:00+00:00', 'source_refs': ['raw:2b3d86553c5968e3fc930b046e7c2adc27317c0f8f87df064fb7da2ec6763a77'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 220000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 42.7837% | 35.8758% | 21.3405% | 5.2296% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 41.8203% | 36.1288% | 22.0509% | 4.1317% | 65.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 43.2757% / 35.4420% / 21.2823% | 42.7837% / 35.8758% / 21.3405% | [-0.492001629279315, 0.43376001357604, 0.05824161570329722] |
| 1m | 40.9424% / 36.9755% / 22.0822% | 41.8203% / 36.1288% / 22.0509% | [0.8779513830583785, -0.8466734947685073, -0.03127788828989064] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 63.50359592972222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-25T22:00:12.066152Z",
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
    "age_hours": 63.50359592972222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-25T22:00:12.480904Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.50359592972222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-25T22:00:12.396900Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5035959297222226,
    "authority": "official_original",
    "collected_at": "2026-09-25T22:00:12.134185Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-25T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293",
    "reason": null,
    "released_at": null,
    "rows": 185,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-25T22:00:12.596445Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "19ecf2040fc92a93e3a55234c9a9a1bb6bb5cd1bf78cb0a007fbe79b2f0be99c",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 63.50359592972222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-25T22:00:12.640953Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "3ad653166d12143741920514a98d4ff4d25779ae0a999b05300deaa31eb43922",
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
    "collected_at": "2026-09-25T22:00:12.945347Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "1f277221f8831446d4ed147ca3d41dc29bf8eb81d83972a91d16d90c8bbf1a80",
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
    "collected_at": "2026-09-25T22:00:12.481905Z",
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
    "collected_at": "2026-09-25T22:00:12.481905Z",
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
    "collected_at": "2026-09-25T22:00:12.481905Z",
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
    "collected_at": "2026-09-25T22:00:12.481905Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-23T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-25T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-23T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ad653166d12143741920514a98d4ff4d25779ae0a999b05300deaa31eb43922'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "31a261fd-4611-5691-984f-3f13762102e3/1w/technical",
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
Feedback applied once: {'batch_id': '31a261fd-4611-5691-984f-3f13762102e3/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "ddc17ed5-60fe-57d9-8e4e-e0d4b67a4877",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.39285000000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ddc17ed5-60fe-57d9-8e4e-e0d4b67a4877",
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
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ddc17ed5-60fe-57d9-8e4e-e0d4b67a4877",
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
    "hypothesis_id": "ddc17ed5-60fe-57d9-8e4e-e0d4b67a4877",
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
    "hypothesis_id": "ddc17ed5-60fe-57d9-8e4e-e0d4b67a4877",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.18606337030436845
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
    "hypothesis_id": "8291829c-e349-5957-a164-a7dff393b700",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [1.3058001671836184, -0.9775858080096844, -0.32821435917393116] | {'down': 0.34022414191990313, 'flat': 0.2467178564082607, 'up': 0.4130580016718362} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34022414191990313, 'flat': 0.2467178564082607, 'up': 0.4130580016718362} | [2.790907749080118, -2.0534749539123984, -0.7374327951677334] | {'down': 0.31968939238077915, 'flat': 0.23934352845658335, 'up': 0.4409670791626374} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.31968939238077915, 'flat': 0.23934352845658335, 'up': 0.4409670791626374} | [2.822510118874505, -2.0296976954749857, -0.7928124233995026] | {'down': 0.2993924154260293, 'flat': 0.23141540422258833, 'up': 0.46919218035138244} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.2993924154260293, 'flat': 0.23141540422258833, 'up': 0.46919218035138244} | [2.4363744944662145, -1.716163272601351, -0.7202112218648665] | {'down': 0.2822307827000158, 'flat': 0.22421329200393966, 'up': 0.4935559252960446} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.2822307827000158, 'flat': 0.22421329200393966, 'up': 0.4935559252960446} | [2.4348098582126996, -1.6834230364378588, -0.751386821774852] | {'down': 0.2653965523356372, 'flat': 0.21669942378619114, 'up': 0.5179040238781716} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.2653965523356372, 'flat': 0.21669942378619114, 'up': 0.5179040238781716} | [-7.571583824820411, 8.595445306686301, -1.0238614818658898] | {'down': 0.3513510054025002, 'flat': 0.20646080896753224, 'up': 0.4421881856299675} |
| 6 | E10/causal | ['31a261fd-4611-5691-984f-3f13762102e3/1w/technical'] | {'down': 0.3513510054025002, 'flat': 0.20646080896753224, 'up': 0.4421881856299675} | [1.2062412628441432, -1.1428152594211205, -0.06342600342301719] | {'down': 0.339922852808289, 'flat': 0.20582654893330207, 'up': 0.4542505982584089} |
| 7 | E17/scenario | ['80de9545-9553-53f6-a2f3-ffa37fb89b0e', '6af55748-9caf-5d5c-a82d-61c8e57e0305', '87899f32-bc44-52dc-a448-4016f2ef96c8', '37f2f658-68d4-5637-8db6-aa2fb1b52c7d'] | {'down': 0.339922852808289, 'flat': 0.20582654893330207, 'up': 0.4542505982584089} | [0.32663063061568187, 2.4539418394128876, -2.7805724700285777] | {'down': 0.36446227120241786, 'flat': 0.1780208242330163, 'up': 0.45751690456456573} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.36446227120241786, 'flat': 0.1780208242330163, 'up': 0.45751690456456573} | [-1.62222334364715, -0.4066406624765373, 2.028864006123693] | {'down': 0.3603958645776525, 'flat': 0.19830946429425322, 'up': 0.44129467112809423} |
| 9 | E13/history | [] | {'down': 0.3603958645776525, 'flat': 0.19830946429425322, 'up': 0.44129467112809423} | [0.0, 0.0, 0.0] | {'down': 0.3603958645776525, 'flat': 0.19830946429425322, 'up': 0.44129467112809423} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3603958645776525, 'flat': 0.19830946429425322, 'up': 0.44129467112809423} | [-1.3457400145057807, -0.16380871716817902, 1.5095487316739735] | {'down': 0.3587577774059707, 'flat': 0.21340495161099296, 'up': 0.4278372709830364} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ad653166d12143741920514a98d4ff4d25779ae0a999b05300deaa31eb43922'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "31a261fd-4611-5691-984f-3f13762102e3/1m/technical",
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
      1027,
      1034
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
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
Feedback applied once: {'batch_id': '31a261fd-4611-5691-984f-3f13762102e3/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "13531549-b97e-5a42-b3a5-1845ce55cd4e",
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
    "hypothesis_id": "13531549-b97e-5a42-b3a5-1845ce55cd4e",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "13531549-b97e-5a42-b3a5-1845ce55cd4e",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.435375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "13531549-b97e-5a42-b3a5-1845ce55cd4e",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.435375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "13531549-b97e-5a42-b3a5-1845ce55cd4e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.22858837030436846
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
    "hypothesis_id": "a382ac34-31ac-5993-ba9c-1acacd0db88b",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.6223891437918239, -0.46732980441123173, -0.15505933938060046] | {'down': 0.34532670195588766, 'flat': 0.248449406606194, 'up': 0.40622389143791826} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34532670195588766, 'flat': 0.248449406606194, 'up': 0.40622389143791826} | [1.1927783226180655, -0.8886287058139097, -0.3041496168041419] | {'down': 0.33644041489774856, 'flat': 0.24540791043815258, 'up': 0.4181516746640989} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.33644041489774856, 'flat': 0.24540791043815258, 'up': 0.4181516746640989} | [1.2012974282684996, -0.8859450448701067, -0.31535238339838456] | {'down': 0.3275809644490475, 'flat': 0.24225438660416873, 'up': 0.4301646489467839} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.3275809644490475, 'flat': 0.24225438660416873, 'up': 0.4301646489467839} | [1.9298831513788528, -1.4049785316913754, -0.5249046196874885] | {'down': 0.31353117913213374, 'flat': 0.23700534040729385, 'up': 0.44946348046057244} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.31353117913213374, 'flat': 0.23700534040729385, 'up': 0.44946348046057244} | [1.9422806494431455, -1.392122230751558, -0.5501584186915959] | {'down': 0.29960995682461816, 'flat': 0.2315037562203779, 'up': 0.4688862869550039} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.29960995682461816, 'flat': 0.2315037562203779, 'up': 0.4688862869550039} | [-5.633365278604413, 6.668769158195376, -1.0354038795909544] | {'down': 0.3662976484065719, 'flat': 0.22114971742446835, 'up': 0.41255263416895976} |
| 6 | E10/causal | ['31a261fd-4611-5691-984f-3f13762102e3/1m/technical'] | {'down': 0.3662976484065719, 'flat': 0.22114971742446835, 'up': 0.41255263416895976} | [2.7741797615663533, -2.6603518003136095, -0.11382796125275207] | {'down': 0.3396941304034358, 'flat': 0.22001143781194082, 'up': 0.4402944317846233} |
| 7 | E17/scenario | ['02f7cf61-ae9f-5c39-81f1-85466525e481', 'f6c8dd97-3eea-5ead-9a51-10f7af5cf08a', '0db07f2e-cd66-5d9a-9695-f81398da3f09', 'a13bcb15-ffef-5df3-91be-a3c59e72175b'] | {'down': 0.3396941304034358, 'flat': 0.22001143781194082, 'up': 0.4402944317846233} | [0.4593311640883835, 2.8516654442479084, -3.3109966083362945] | {'down': 0.3682107848459149, 'flat': 0.18690147172857788, 'up': 0.44488774342550713} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3682107848459149, 'flat': 0.18690147172857788, 'up': 0.44488774342550713} | [-1.4625677902173895, -0.45727136331967233, 1.9198391535370674] | {'down': 0.3636380712127182, 'flat': 0.20609986326394855, 'up': 0.43026206552333324} |
| 9 | E13/history | [] | {'down': 0.3636380712127182, 'flat': 0.20609986326394855, 'up': 0.43026206552333324} | [0.0, 0.0, 0.0] | {'down': 0.3636380712127182, 'flat': 0.20609986326394855, 'up': 0.43026206552333324} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3636380712127182, 'flat': 0.20609986326394855, 'up': 0.43026206552333324} | [-1.2058971080622038, -0.23500360579665758, 1.4409007138588559] | {'down': 0.3612880351547516, 'flat': 0.2205088704025371, 'up': 0.4182030944427112} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '7536b5ebe9481bb079e98e3874f56f68cc3130e9e9712fb99cfca9ad3ee844c9'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ad653166d12143741920514a98d4ff4d25779ae0a999b05300deaa31eb43922'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:701830e776c3f55341ee6feedd2db394e1baca575d455bf1fbfce6e9da63f1df#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:6afe37192267f6861d1954b90c22c4f651705a41781ccf6a27db3162d279f849#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:24a56ac626ee529e45e0c578481122216c9bccaebb4d10848eceb613ee1cd293#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "31a261fd-4611-5691-984f-3f13762102e3/1y/technical",
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
      1027,
      1034
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '31a261fd-4611-5691-984f-3f13762102e3/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "fba26de8-b820-555f-9bff-62f09b439255",
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
    "hypothesis_id": "fba26de8-b820-555f-9bff-62f09b439255",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "fba26de8-b820-555f-9bff-62f09b439255",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.39285000000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "fba26de8-b820-555f-9bff-62f09b439255",
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
    "hypothesis_id": "fba26de8-b820-555f-9bff-62f09b439255",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.18606337030436845
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
    "hypothesis_id": "4765ca70-6d21-5f9c-b796-08490768c143",
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
