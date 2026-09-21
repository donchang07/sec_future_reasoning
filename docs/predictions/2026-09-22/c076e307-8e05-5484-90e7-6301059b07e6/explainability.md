# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: c076e307-8e05-5484-90e7-6301059b07e6
Cutoff / prediction: 2026-09-21T22:00:10.445283+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-21T06:30:00+00:00', 'source_refs': ['raw:c5acc45f83d711f257d1d23773754a663a8a958f4a9ff3967b4b063ae9e1e056'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 208000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 41.5571% | 36.7850% | 21.6579% | 5.1075% | 20.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 40.3548% | 37.3939% | 22.2513% | 4.2197% | 45.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 41.5571% / 36.7850% / 21.6579% | 41.5571% / 36.7850% / 21.6579% | [0.0, 0.0, 0.0] |
| 1m | 40.1833% / 37.5707% / 22.2459% | 40.3548% / 37.3939% / 22.2513% | [0.17146683441688348, -0.17684889978820117, 0.005382065371306588] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.502901467500001,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:09.364188Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c5acc45f83d711f257d1d23773754a663a8a958f4a9ff3967b4b063ae9e1e056",
    "reason": null,
    "released_at": null,
    "rows": 253,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.502901467500001,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:09.911608Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.502901467500001,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:09.955633Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5029014674999996,
    "authority": "official_original",
    "collected_at": "2026-09-21T22:00:09.560693Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-21T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5",
    "reason": null,
    "released_at": null,
    "rows": 181,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:09.992345Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "a01a80bc5582afe4c379b047e6179bdf0845aa2ca0b6a7802cf7107d8f5346b3",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.5029014675,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:10.166098Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "99ca9ce29dcd7e83752ffe61b562c4a0c3c7b87122ccb373f5a95d413a58b2b8",
    "reason": null,
    "released_at": null,
    "rows": 242,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-21T22:00:10.444283Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "ffa54930b2f85a4e598eadebf811aa8000b4fa02c3e3cd6baa8a2cfd4f9ff919",
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
    "collected_at": "2026-09-21T22:00:09.956631Z",
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
    "collected_at": "2026-09-21T22:00:09.956631Z",
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
    "collected_at": "2026-09-21T22:00:09.956631Z",
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
    "collected_at": "2026-09-21T22:00:09.956631Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-21T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-18T06:30:00+00:00'}, '30m': {'count': 253, 'last': '2026-09-21T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:99ca9ce29dcd7e83752ffe61b562c4a0c3c7b87122ccb373f5a95d413a58b2b8'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "c076e307-8e05-5484-90e7-6301059b07e6/1w/technical",
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
    "atr": 10142.953130276379,
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
      4919,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 59.39699284476412,
    "sma": [
      193235.0,
      188320.0,
      182805.83333333334
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
      4914,
      4924
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2224241143622994
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 1436.7893371424736,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 207500.0,
    "bottom_pivots": [
      231,
      245
    ],
    "bottom_score": 0.2,
    "rsi": 73.00052365664018,
    "sma": [
      203725.0,
      196350.0,
      195627.91666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 195500.0,
    "top_pivots": [
      228,
      250
    ],
    "top_score": 0.2,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'c076e307-8e05-5484-90e7-6301059b07e6/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "d02c3a11-84c0-562a-9c08-af3043492c1d",
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
    "hypothesis_id": "d02c3a11-84c0-562a-9c08-af3043492c1d",
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
    "hypothesis_id": "d02c3a11-84c0-562a-9c08-af3043492c1d",
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
    "hypothesis_id": "d02c3a11-84c0-562a-9c08-af3043492c1d",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.160161286560164
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d02c3a11-84c0-562a-9c08-af3043492c1d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.12685940340431565
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
    "hypothesis_id": "34391e25-1baf-5b28-9a8b-6e8251e6d39d",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.8890279787811317, -0.666767945394553, -0.22226003338658706] | {'down': 0.34333232054605445, 'flat': 0.24777739966613413, 'up': 0.40889027978781134} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34333232054605445, 'flat': 0.24777739966613413, 'up': 0.40889027978781134} | [2.871381880920093, -2.1193650758678686, -0.7520168050522108] | {'down': 0.32213866978737576, 'flat': 0.24025723161561202, 'up': 0.43760409859701227} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.32213866978737576, 'flat': 0.24025723161561202, 'up': 0.43760409859701227} | [1.1464838027097746, -0.8322460171492518, -0.31423778556052273] | {'down': 0.31381620961588325, 'flat': 0.2371148537600068, 'up': 0.44906893662411} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.31381620961588325, 'flat': 0.2371148537600068, 'up': 0.44906893662411} | [2.428876816880776, -1.7380997758010108, -0.6907770410797681] | {'down': 0.29643521185787314, 'flat': 0.2302070833492091, 'up': 0.4733577047929178} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.29643521185787314, 'flat': 0.2302070833492091, 'up': 0.4733577047929178} | [2.436930057167003, -1.7110393002377267, -0.7258907569292844] | {'down': 0.27932481885549587, 'flat': 0.22294817577991627, 'up': 0.4977270053645878} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.27932481885549587, 'flat': 0.22294817577991627, 'up': 0.4977270053645878} | [-7.268299876267731, 8.410517660203427, -1.1422177839356977] | {'down': 0.36342999545753013, 'flat': 0.2115259979405593, 'up': 0.4250440066019105} |
| 6 | E10/causal | ['c076e307-8e05-5484-90e7-6301059b07e6/1w/technical'] | {'down': 0.36342999545753013, 'flat': 0.2115259979405593, 'up': 0.4250440066019105} | [1.1373089975932227, -1.0935157024340614, -0.043793295159155754] | {'down': 0.3524948384331895, 'flat': 0.21108806498896773, 'up': 0.4364170965778427} |
| 7 | E17/scenario | ['145c245b-35bf-51c0-8733-68f7bd5a7baa', 'cdb93ac9-c830-51af-9e84-283bdc4d95cf', '4556473d-3615-5cf8-ba8f-a09bd7151791', 'ea826223-6377-53e8-a60f-c68775e810d7'] | {'down': 0.3524948384331895, 'flat': 0.21108806498896773, 'up': 0.4364170965778427} | [0.4749852258427334, 2.4350878089716312, -2.910073034814345] | {'down': 0.3768457165229058, 'flat': 0.18198733464082428, 'up': 0.44116694883627006} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3768457165229058, 'flat': 0.18198733464082428, 'up': 0.44116694883627006} | [-1.4135188043318925, -0.57037475348381, 1.9838935578157106] | {'down': 0.3711419689880677, 'flat': 0.2018262702189814, 'up': 0.42703176079295113} |
| 9 | E13/history | [] | {'down': 0.3711419689880677, 'flat': 0.2018262702189814, 'up': 0.42703176079295113} | [0.0, 0.0, 0.0] | {'down': 0.3711419689880677, 'flat': 0.2018262702189814, 'up': 0.42703176079295113} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3711419689880677, 'flat': 0.2018262702189814, 'up': 0.42703176079295113} | [-1.146105762309585, -0.32918382991891093, 1.4752895922284766] | {'down': 0.3678501306888786, 'flat': 0.21657916614126616, 'up': 0.4155707031698553} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:99ca9ce29dcd7e83752ffe61b562c4a0c3c7b87122ccb373f5a95d413a58b2b8'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "c076e307-8e05-5484-90e7-6301059b07e6/1m/technical",
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
  "reflexivity_effect": 0.0050000000000000044,
  "regime_effect": 0.007500000000000007,
  "sell_liquidity": null,
  "wave": {
    "atr": 10142.953130276379,
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
      4919,
      4927
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 59.39699284476412,
    "sma": [
      193235.0,
      188320.0,
      182805.83333333334
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
      4914,
      4924
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2224241143622994
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'c076e307-8e05-5484-90e7-6301059b07e6/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0050000000000000044, 'regime_effect': 0.007500000000000007}
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
    "hypothesis_id": "36e4971c-d1d5-5c02-aded-8bd51366e0d7",
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
    "hypothesis_id": "36e4971c-d1d5-5c02-aded-8bd51366e0d7",
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
    "hypothesis_id": "36e4971c-d1d5-5c02-aded-8bd51366e0d7",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.41107499999999997
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "36e4971c-d1d5-5c02-aded-8bd51366e0d7",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.16623628656016404
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "36e4971c-d1d5-5c02-aded-8bd51366e0d7",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.13293440340431564
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
    "hypothesis_id": "4a520617-c97b-524d-a856-adcf7554ba72",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.3616053882826653, -0.2718250079800033, -0.08978038030267033] | {'down': 0.34728174992019994, 'flat': 0.2491021961969733, 'up': 0.4036160538828267} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34728174992019994, 'flat': 0.2491021961969733, 'up': 0.4036160538828267} | [1.1240213700075719, -0.8395286092401588, -0.28449276076739916] | {'down': 0.33888646382779836, 'flat': 0.2462572685892993, 'up': 0.4148562675829024} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.33888646382779836, 'flat': 0.2462572685892993, 'up': 0.4148562675829024} | [0.4568632322849653, -0.3389283677743826, -0.11793486451058266] | {'down': 0.33549718015005453, 'flat': 0.24507791994419348, 'up': 0.41942489990575205} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.33549718015005453, 'flat': 0.24507791994419348, 'up': 0.41942489990575205} | [1.9204107538228932, -1.4105670980722407, -0.5098436557506636] | {'down': 0.3213915091693321, 'flat': 0.23997948338668684, 'up': 0.438629007443981} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3213915091693321, 'flat': 0.23997948338668684, 'up': 0.438629007443981} | [1.936050238356074, -1.399780684269064, -0.5362695540870044] | {'down': 0.3073937023266415, 'flat': 0.2346167878458168, 'up': 0.4579895098275417} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.3073937023266415, 'flat': 0.2346167878458168, 'up': 0.4579895098275417} | [-5.391474960193449, 6.452890036784675, -1.0614150765912238] | {'down': 0.37192260269448824, 'flat': 0.22400263707990456, 'up': 0.40407476022560723} |
| 6 | E10/causal | ['c076e307-8e05-5484-90e7-6301059b07e6/1m/technical'] | {'down': 0.37192260269448824, 'flat': 0.22400263707990456, 'up': 0.40407476022560723} | [1.342083697010571, -1.307297813010383, -0.034785884000182454] | {'down': 0.3588496245643844, 'flat': 0.22365477823990274, 'up': 0.41749559719571294} |
| 7 | E17/scenario | ['846f6215-efe8-5497-b8d3-cc1bbde0590e', '57fbe690-a4f2-56b4-9c52-4dd1feb22212', 'b65bfb8f-488a-55fc-980e-8b7844513f38', 'fe76510d-d807-5459-b14c-abde5313142e'] | {'down': 0.3588496245643844, 'flat': 0.22365477823990274, 'up': 0.41749559719571294} | [0.7664071655663185, 2.6432256528948814, -3.4096328184612195] | {'down': 0.3852818810933332, 'flat': 0.18955845005529054, 'up': 0.4251596688513761} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3852818810933332, 'flat': 0.18955845005529054, 'up': 0.4251596688513761} | [-1.2002205563320267, -0.6789960041571841, 1.8792165604892137] | {'down': 0.3784919210517614, 'flat': 0.20835061566018268, 'up': 0.41315746328805586} |
| 9 | E13/history | [] | {'down': 0.3784919210517614, 'flat': 0.20835061566018268, 'up': 0.41315746328805586} | [0.0, 0.0, 0.0] | {'down': 0.3784919210517614, 'flat': 0.20835061566018268, 'up': 0.41315746328805586} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3784919210517614, 'flat': 0.20835061566018268, 'up': 0.41315746328805586} | [-0.9609340862426929, -0.45530965217115416, 1.416243738413847] | {'down': 0.37393882453004984, 'flat': 0.22251305304432115, 'up': 0.40354812242562893} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'b5b1f09e1a95aef532d35613f3e5950d042f86138ea457d19c3bb5eb30c0f411'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:99ca9ce29dcd7e83752ffe61b562c4a0c3c7b87122ccb373f5a95d413a58b2b8'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_rsi_14@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_trend_alignment@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#preferred_volume_z@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1b70c2eaeec8de5b273bac754fd8e6845eea41fc8cecb91147463a5fa260786a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:1c9e6a1a2b9b0e0527163b6e7d8e74a6c2aadc4ee8df7cda51a6bf2bd27be815#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:912151897a5094f1084dfcbbb7d2b1f3f188d6e08a05fdc5515cdc6f12cb11e5#us_10y_yield@2026-09-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "c076e307-8e05-5484-90e7-6301059b07e6/1y/technical",
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
Feedback applied once: {'batch_id': 'c076e307-8e05-5484-90e7-6301059b07e6/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "49a17ef4-5f4c-5bd4-a9c2-58a94f2b523e",
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
    "hypothesis_id": "49a17ef4-5f4c-5bd4-a9c2-58a94f2b523e",
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
    "hypothesis_id": "49a17ef4-5f4c-5bd4-a9c2-58a94f2b523e",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "49a17ef4-5f4c-5bd4-a9c2-58a94f2b523e",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.14801128656016402
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "49a17ef4-5f4c-5bd4-a9c2-58a94f2b523e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.11470940340431565
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
    "hypothesis_id": "eb700cd6-ad27-558e-ae56-6e0e50d4fe79",
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
