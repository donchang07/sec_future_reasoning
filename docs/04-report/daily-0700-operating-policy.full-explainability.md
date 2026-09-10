# Operating context: daily-preopen-v1.0.0

Actual exception prediction: 2026-09-10 12:15:33 KST. Nominal schedule: 07:00 KST. Korean ceiling: September 9 15:30 KST. US cash ceiling: September 10 05:00 KST (September 9 16:00 EDT). Conservative US/FX source semantics retain September 8 provider-date data. The unavailable 30m Wave has internal sentinel scores of zero; these are not measured reversal probabilities. The model was not adjusted.

# live-forward-v2 — sealed forward evidence

Run: 2ce0e81e-6569-53de-8b7a-fc7ecd854d7a
Cutoff / prediction: 2026-09-10T03:15:33.112563+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'value': 197500.0, 'unit': 'krw_per_share', 'timeframe': '1d', 'effective_at': '2026-09-09T06:30:00+00:00', 'definition': 'last eligible completed close, not execution quote', 'source_refs': ['raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4']}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 44.4074% | 34.1754% | 21.4172% | 16.1764% | 0.0000% | 0.0000% | None/None | None/None | WAIT |
| 1m | 43.1804% | 34.8810% | 21.9386% | 7.4879% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 44.4074% / 34.1754% / 21.4172% | 44.4074% / 34.1754% / 21.4172% | [0.0, 0.0, 0.0] |
| 1m | 42.2587% / 35.7019% / 22.0395% | 43.1804% / 34.8810% / 21.9386% | [0.9217815405810625, -0.8208717263852139, -0.10090981419584866] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "source_id": "preferred_30m",
    "instrument": "005935.KS",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "daef5113bd5a06ff1c9f299e7d9e6e101c1d1564253c93ecb6064ada3545ba48",
    "status": "stale",
    "latest_effective_at": "2026-09-09T06:00:00Z",
    "collected_at": "2026-09-10T03:15:32.072585Z",
    "released_at": null,
    "age_hours": 21.259197934166668,
    "rows": 258,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 0
    },
    "used_by_model": false,
    "reason": "Freshness SLA exceeded; excluded from reasoning"
  },
  {
    "source_id": "preferred_daily",
    "instrument": "005935.KS",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "collected_at": "2026-09-10T03:15:32.558773Z",
    "released_at": null,
    "age_hours": 20.759197934166668,
    "rows": 4932,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 4
    },
    "used_by_model": true,
    "reason": null
  },
  {
    "source_id": "common_daily",
    "instrument": "005930.KS",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "collected_at": "2026-09-10T03:15:32.532255Z",
    "released_at": null,
    "age_hours": 20.759197934166668,
    "rows": 4934,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 2
    },
    "used_by_model": true,
    "reason": null
  },
  {
    "source_id": "treasury_10y",
    "instrument": "daily_par_yield_10y",
    "provider": "US Treasury",
    "authority": "official_original",
    "raw_sha256": "f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "collected_at": "2026-09-10T03:15:32.283588Z",
    "released_at": null,
    "age_hours": 23.259475711944447,
    "rows": 172,
    "excluded": {},
    "used_by_model": true,
    "reason": null
  },
  {
    "source_id": "usdkrw",
    "instrument": "KRW=X",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642",
    "status": "fresh",
    "latest_effective_at": "2026-09-08T22:59:59Z",
    "collected_at": "2026-09-10T03:15:32.650812Z",
    "released_at": null,
    "age_hours": 28.259475711944447,
    "rows": 217,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 43
    },
    "used_by_model": true,
    "reason": null
  },
  {
    "source_id": "kospi",
    "instrument": "%5EKS11",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "9294e05741a3560356d6c7b0466e74ca387b9a67ea6900cc9b542814a1cb3dab",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "collected_at": "2026-09-10T03:15:32.930785Z",
    "released_at": null,
    "age_hours": 20.759197934166668,
    "rows": 243,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 0
    },
    "used_by_model": false,
    "reason": null
  },
  {
    "source_id": "dxy",
    "instrument": "DX-Y.NYB",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "574b0ac2d80291b8d4fb28d9c94d2571ab61b8156ff8d15e9c455776a39d71d6",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "collected_at": "2026-09-10T03:15:33.112563Z",
    "released_at": null,
    "age_hours": 23.259475711944447,
    "rows": 251,
    "excluded": {
      "incomplete": 0,
      "off_grid": 0,
      "invalid": 52
    },
    "used_by_model": false,
    "reason": null
  },
  {
    "source_id": "foreign_net_buy",
    "instrument": "foreign_net_buy",
    "provider": "not_connected",
    "authority": "unavailable",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "status": "unavailable",
    "latest_effective_at": null,
    "collected_at": "2026-09-10T03:15:32.558773Z",
    "released_at": null,
    "age_hours": null,
    "rows": 0,
    "excluded": {},
    "used_by_model": false,
    "reason": "ValueError: No verified source credentials/series; unavailable"
  },
  {
    "source_id": "institution_net_buy",
    "instrument": "institution_net_buy",
    "provider": "not_connected",
    "authority": "unavailable",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "status": "unavailable",
    "latest_effective_at": null,
    "collected_at": "2026-09-10T03:15:32.558773Z",
    "released_at": null,
    "age_hours": null,
    "rows": 0,
    "excluded": {},
    "used_by_model": false,
    "reason": "ValueError: No verified source credentials/series; unavailable"
  },
  {
    "source_id": "program_net_buy",
    "instrument": "program_net_buy",
    "provider": "not_connected",
    "authority": "unavailable",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "status": "unavailable",
    "latest_effective_at": null,
    "collected_at": "2026-09-10T03:15:32.558773Z",
    "released_at": null,
    "age_hours": null,
    "rows": 0,
    "excluded": {},
    "used_by_model": false,
    "reason": "ValueError: No verified source credentials/series; unavailable"
  },
  {
    "source_id": "dram_contract_asp",
    "instrument": "dram_contract_asp",
    "provider": "not_connected",
    "authority": "unavailable",
    "raw_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "status": "unavailable",
    "latest_effective_at": null,
    "collected_at": "2026-09-10T03:15:32.558773Z",
    "released_at": null,
    "age_hours": null,
    "rows": 0,
    "excluded": {},
    "used_by_model": false,
    "reason": "ValueError: No verified source credentials/series; unavailable"
  }
]
```
Document statuses: {'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped', 'dram_spot': 'available_unmapped', 'exports_10': 'available_unmapped', 'exports_20': 'available_unmapped', 'exports_month': 'available_unmapped', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response'}
Bar boundaries: {'30m': {'count': 0, 'last': None}, '1d': {'count': 4932, 'last': '2026-09-09T06:30:00+00:00'}, '1w': {'count': 1042, 'last': '2026-09-04T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'macro': 1.0, 'memory': 0.5833333333333334, 'earnings': 0.5, 'flow': 0.0, 'price_regime': 1.0, 'ai_demand': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.9
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy']
Unmapped/conflicting evidence: [{'source_ref': 'raw:574b0ac2d80291b8d4fb28d9c94d2571ab61b8156ff8d15e9c455776a39d71d6', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:9294e05741a3560356d6c7b0466e74ca387b9a67ea6900cc9b542814a1cb3dab', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1w/technical",
  "primary": "30m",
  "higher": "1d",
  "wave": {
    "available": false,
    "bottom_score": 0.0,
    "top_score": 0.0,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": null,
    "sma": [],
    "atr": null,
    "volume_ratio": null,
    "bottom_features": {},
    "top_features": {},
    "bottom_neckline": null,
    "top_neckline": null,
    "bottom_pivots": [],
    "top_pivots": []
  },
  "higher_wave": {
    "available": true,
    "bottom_score": 0.45000000000000007,
    "top_score": 0.2,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 54.72382942450808,
    "sma": [
      191245.0,
      191940.0,
      178846.66666666666
    ],
    "atr": 10957.338268841326,
    "volume_ratio": 0.672290280335483,
    "bottom_features": {
      "double": true,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": true,
      "neckline": false,
      "ma": true
    },
    "top_features": {
      "double": true,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "bottom_neckline": 204000.0,
    "top_neckline": 172700.0,
    "bottom_pivots": [
      4920,
      4927
    ],
    "top_pivots": [
      4915,
      4922
    ]
  },
  "bullish_alignment": null,
  "bearish_alignment": null,
  "buy_liquidity": null,
  "sell_liquidity": null,
  "regime_effect": 0.0,
  "flow_effect": 0.0,
  "reflexivity_effect": 0.0,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ]
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'regime_effect': 0.0, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'batch_id': '2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1w/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "115084c5-26b6-5a75-b967-489b86c584c0",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "115084c5-26b6-5a75-b967-489b86c584c0",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "115084c5-26b6-5a75-b967-489b86c584c0",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "115084c5-26b6-5a75-b967-489b86c584c0",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.09565754584628867,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "115084c5-26b6-5a75-b967-489b86c584c0",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

negative_paths (up to five; never padded)
```json
[
  {
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "hypothesis_id": "6dcaf865-86e3-5320-a670-53b456d1c856",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

### Probability contribution reconstruction
Prior: {'up': 0.4, 'down': 0.35, 'flat': 0.25}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'up': 0.4, 'down': 0.35, 'flat': 0.25} | [0.6698465145587307, -0.502860183908016, -0.166986330650723] | {'up': 0.40669846514558733, 'down': 0.3449713981609198, 'flat': 0.24833013669349277} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'up': 0.40669846514558733, 'down': 0.3449713981609198, 'flat': 0.24833013669349277} | [4.316946085228867, -3.1732308826509237, -1.1437152025779385] | {'up': 0.449867925997876, 'down': 0.3132390893344106, 'flat': 0.23689298466771339} |
| 2 | E12/causal | ['samsung_common_price'] | {'up': 0.449867925997876, 'down': 0.3132390893344106, 'flat': 0.23689298466771339} | [3.6475925784543395, -2.596178013042494, -1.051414565411843] | {'up': 0.4863438517824194, 'down': 0.28727730920398564, 'flat': 0.22637883901359496} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'up': 0.4863438517824194, 'down': 0.28727730920398564, 'flat': 0.22637883901359496} | [3.6518004098825383, -2.5270953465680144, -1.1247050633145155] | {'up': 0.5228618558812448, 'down': 0.2620063557383055, 'flat': 0.2151317883804498} |
| 4 | E12/causal | ['us_10y_yield'] | {'up': 0.5228618558812448, 'down': 0.2620063557383055, 'flat': 0.2151317883804498} | [-6.0092729417243085, 6.736035538354673, -0.7267625966303815] | {'up': 0.4627691264640017, 'down': 0.32936671112185223, 'flat': 0.207864162414146} |
| 5 | E12/causal | ['usdkrw'] | {'up': 0.4627691264640017, 'down': 0.32936671112185223, 'flat': 0.207864162414146} | [0.21116464818912717, -0.15930275421912055, -0.051861893969998296] | {'up': 0.464880772945893, 'down': 0.327773683579661, 'flat': 0.207345543474446} |
| 6 | E10/causal | ['2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1w/technical'] | {'up': 0.464880772945893, 'down': 0.327773683579661, 'flat': 0.207345543474446} | [1.1599765549280994, -1.0712031409383593, -0.08877341398973448] | {'up': 0.47648053849517397, 'down': 0.31706165217027743, 'flat': 0.20645780933454866} |
| 7 | E17/scenario | ['3a3a7fa8-bb14-5772-a79c-70f9d478bb6f', '9f6a6b13-d97e-548f-92d7-00dc0ec895f0', '9c0acc46-6350-574b-b19c-faf374000a08', '6ca70099-b681-50a3-92be-eb394f2a442d'] | {'up': 0.47648053849517397, 'down': 0.31706165217027743, 'flat': 0.20645780933454866} | [0.1691082891893958, 2.459391285266693, -2.628499574456095] | {'up': 0.4781716213870679, 'down': 0.34165556502294436, 'flat': 0.1801728135899877} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'up': 0.4781716213870679, 'down': 0.34165556502294436, 'flat': 0.1801728135899877} | [-1.7820796747493983, -0.10239612841259627, 1.8844758031619975] | {'up': 0.46035082463957394, 'down': 0.3406316037388184, 'flat': 0.1990175716216077} |
| 9 | E13/history | [] | {'up': 0.46035082463957394, 'down': 0.3406316037388184, 'flat': 0.1990175716216077} | [0.0, 0.0, 0.0] | {'up': 0.46035082463957394, 'down': 0.3406316037388184, 'flat': 0.1990175716216077} |
| 10 | E18/calibration | ['temperature:1.15'] | {'up': 0.46035082463957394, 'down': 0.3406316037388184, 'flat': 0.1990175716216077} | [-1.6276344333155057, 0.11220918367602639, 1.5154252496394793] | {'up': 0.4440744803064189, 'down': 0.34175369557557866, 'flat': 0.21417182411800248} |
E09 duplicate-root interaction adjustment precedes these causal steps. E10 reflexivity, E17 scenario, E14 challenger, E13 historical and E18 calibration steps are explicit; no additional hidden adjustment.

### What Would Change My Mind
```json
{
  "missing_coverage": [],
  "missing_strong": [
    "foreign_net_buy",
    "institution_net_buy"
  ],
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
      "factor_id": "usdkrw",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd",
      "horizon": "1w",
      "evidence_refs": [
        "usdkrw"
      ]
    },
    {
      "factor_id": "samsung_common_price",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share",
      "horizon": "1w",
      "evidence_refs": [
        "samsung_common_price"
      ]
    },
    {
      "factor_id": "samsung_preferred_price",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share",
      "horizon": "1w",
      "evidence_refs": [
        "samsung_preferred_price"
      ]
    },
    {
      "factor_id": "us_10y_yield",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent",
      "horizon": "1w",
      "evidence_refs": [
        "us_10y_yield"
      ]
    }
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1m
Eligibility: True; reasons: []
Coverage: {'macro': 1.0, 'memory': 0.5833333333333334, 'earnings': 1.0, 'flow': 0.0, 'price_regime': 1.0, 'ai_demand': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.4252500000000001
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision']
Unmapped/conflicting evidence: [{'source_ref': 'raw:574b0ac2d80291b8d4fb28d9c94d2571ab61b8156ff8d15e9c455776a39d71d6', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:9294e05741a3560356d6c7b0466e74ca387b9a67ea6900cc9b542814a1cb3dab', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1m/technical",
  "primary": "1d",
  "higher": "1w",
  "wave": {
    "available": true,
    "bottom_score": 0.45000000000000007,
    "top_score": 0.2,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 54.72382942450808,
    "sma": [
      191245.0,
      191940.0,
      178846.66666666666
    ],
    "atr": 10957.338268841326,
    "volume_ratio": 0.672290280335483,
    "bottom_features": {
      "double": true,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": true,
      "neckline": false,
      "ma": true
    },
    "top_features": {
      "double": true,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "bottom_neckline": 204000.0,
    "top_neckline": 172700.0,
    "bottom_pivots": [
      4920,
      4927
    ],
    "top_pivots": [
      4915,
      4922
    ]
  },
  "higher_wave": {
    "available": true,
    "bottom_score": 0.0,
    "top_score": 0.1,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 56.03519597017332,
    "sma": [
      190905.0,
      124510.83333333333,
      87986.25
    ],
    "atr": 25575.479086468946,
    "volume_ratio": 0.5330666693133895,
    "bottom_features": {
      "double": false,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "top_features": {
      "double": false,
      "divergence": false,
      "extreme": true,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "bottom_neckline": 240500.0,
    "top_neckline": 139600.0,
    "bottom_pivots": [
      1029,
      1036
    ],
    "top_pivots": [
      1031,
      1039
    ]
  },
  "bullish_alignment": 0.4,
  "bearish_alignment": 0.0,
  "buy_liquidity": null,
  "sell_liquidity": null,
  "regime_effect": 0.037500000000000006,
  "flow_effect": 0.0,
  "reflexivity_effect": 0.02500000000000001,
  "evidence_refs": [
    "bars:1d",
    "bars:1w"
  ]
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'regime_effect': 0.037500000000000006, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'batch_id': '2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1m/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-08': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-07': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "aef62d93-51ed-5932-b05c-233fd2eb2943",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "aef62d93-51ed-5932-b05c-233fd2eb2943",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "aef62d93-51ed-5932-b05c-233fd2eb2943",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6530625,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "aef62d93-51ed-5932-b05c-233fd2eb2943",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.14122004584628867,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "aef62d93-51ed-5932-b05c-233fd2eb2943",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

negative_paths (up to five; never padded)
```json
[
  {
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "hypothesis_id": "53ee32c9-820b-57fa-951e-2bf5cf417aa2",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

### Probability contribution reconstruction
Prior: {'up': 0.4, 'down': 0.35, 'flat': 0.25}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'up': 0.4, 'down': 0.35, 'flat': 0.25} | [0.384175547809551, -0.2887629627485566, -0.0954125850609916] | {'up': 0.40384175547809553, 'down': 0.3471123703725144, 'flat': 0.24904587414939008} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'up': 0.40384175547809553, 'down': 0.3471123703725144, 'flat': 0.24904587414939008} | [1.7897404417237306, -1.332705227690112, -0.4570352140336159] | {'up': 0.42173915989533284, 'down': 0.3337853180956133, 'flat': 0.24447552200905392} |
| 2 | E12/causal | ['samsung_common_price'] | {'up': 0.42173915989533284, 'down': 0.3337853180956133, 'flat': 0.24447552200905392} | [2.8898772221679137, -2.110206302911627, -0.7796709192562867] | {'up': 0.450637932117012, 'down': 0.312683255066497, 'flat': 0.23667881281649106} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'up': 0.450637932117012, 'down': 0.312683255066497, 'flat': 0.23667881281649106} | [2.9169465055647548, -2.0807920352345857, -0.8361544703301749] | {'up': 0.4798073971726595, 'down': 0.29187533471415117, 'flat': 0.2283172681131893} |
| 4 | E12/causal | ['us_10y_yield'] | {'up': 0.4798073971726595, 'down': 0.29187533471415117, 'flat': 0.2283172681131893} | [-4.496084779643416, 5.228382243489177, -0.7322974638457547] | {'up': 0.43484654937622536, 'down': 0.34415915714904294, 'flat': 0.22099429347473176} |
| 5 | E12/causal | ['usdkrw'] | {'up': 0.43484654937622536, 'down': 0.34415915714904294, 'flat': 0.22099429347473176} | [0.15639274045043394, -0.11889877691086959, -0.03749396353957268] | {'up': 0.4364104767807297, 'down': 0.34297016937993424, 'flat': 0.22061935383933604} |
| 6 | E10/causal | ['2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1m/technical'] | {'up': 0.4364104767807297, 'down': 0.34297016937993424, 'flat': 0.22061935383933604} | [2.2842719707122985, -2.137650141354086, -0.14662182935821222] | {'up': 0.4592531964878527, 'down': 0.3215936679663934, 'flat': 0.2191531355457539} |
| 7 | E17/scenario | ['59ebb795-ebd1-5957-8d83-75360a3f7e8e', 'a941d6a9-aa2c-5514-8c1e-935685b88077', '051a34ff-01e4-5455-bf7b-a24f0b1c83e4', 'c98fc6a5-9e63-5a84-b8ea-2647f8dfd747'] | {'up': 0.4592531964878527, 'down': 0.3215936679663934, 'flat': 0.2191531355457539} | [0.28192976379148305, 2.967434575113681, -3.2493643389051527] | {'up': 0.4620724941257675, 'down': 0.3512680137175302, 'flat': 0.18665949215670238} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'up': 0.4620724941257675, 'down': 0.3512680137175302, 'flat': 0.18665949215670238} | [-1.5910570703810134, -0.2216505052126838, 1.8127075755936999] | {'up': 0.4461619234219574, 'down': 0.34905150866540335, 'flat': 0.20478656791263938} |
| 9 | E13/history | [] | {'up': 0.4461619234219574, 'down': 0.34905150866540335, 'flat': 0.20478656791263938} | [0.0, 0.0, 0.0] | {'up': 0.4461619234219574, 'down': 0.34905150866540335, 'flat': 0.20478656791263938} |
| 10 | E18/calibration | ['temperature:1.15'] | {'up': 0.4461619234219574, 'down': 0.34905150866540335, 'flat': 0.20478656791263938} | [-1.4357437695335817, -0.024152857434045494, 1.4598966269676188] | {'up': 0.43180448572662156, 'down': 0.3488099800910629, 'flat': 0.21938553418231557} |
E09 duplicate-root interaction adjustment precedes these causal steps. E10 reflexivity, E17 scenario, E14 challenger, E13 historical and E18 calibration steps are explicit; no additional hidden adjustment.

### What Would Change My Mind
```json
{
  "missing_coverage": [],
  "missing_strong": [
    "dram_contract_asp",
    "foreign_net_buy",
    "hbm_demand",
    "hbm_price",
    "institution_net_buy",
    "samsung_eps",
    "samsung_eps_revision"
  ],
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
      "factor_id": "usdkrw",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd",
      "horizon": "1m",
      "evidence_refs": [
        "usdkrw"
      ]
    },
    {
      "factor_id": "samsung_common_price",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share",
      "horizon": "1m",
      "evidence_refs": [
        "samsung_common_price"
      ]
    },
    {
      "factor_id": "samsung_preferred_price",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share",
      "horizon": "1m",
      "evidence_refs": [
        "samsung_preferred_price"
      ]
    },
    {
      "factor_id": "us_10y_yield",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent",
      "horizon": "1m",
      "evidence_refs": [
        "us_10y_yield"
      ]
    }
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1y
Eligibility: False; reasons: ['coverage:memory', 'memory_family_quorum']
Coverage: {'macro': 1.0, 'memory': 0.26666666666666666, 'earnings': 1.0, 'flow': 0.0, 'price_regime': 1.0, 'ai_demand': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.15746400000000002
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'yield_rate']
Unmapped/conflicting evidence: [{'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'reason': 'horizon_excluded'}, {'source_ref': '5edf8fe7457e50137e8202dea55c3538a1a7b2bc3899008e99e307132293ad1c', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': 'raw:574b0ac2d80291b8d4fb28d9c94d2571ab61b8156ff8d15e9c455776a39d71d6', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:9294e05741a3560356d6c7b0466e74ca387b9a67ea6900cc9b542814a1cb3dab', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:e73ddccf2c6ca68b4288f0e9b1d552f63e7a58d98f8f893e5ce7f23496291748#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f86eb9a96b9a6d29c8ecae943f99b4c13efca940bbab68f94e025c21670a94c4#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:f5da8761767a35df03973e2d4ea5d79fb6aef1cd5f16d2976bd73747e48dd8fb#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:b745e31dcef35e8e0e52b8b1f37c33e56647521f99c17ef3dc56db8036525642#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1y/technical",
  "primary": "1w",
  "higher": "1mo",
  "wave": {
    "available": true,
    "bottom_score": 0.0,
    "top_score": 0.1,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 56.03519597017332,
    "sma": [
      190905.0,
      124510.83333333333,
      87986.25
    ],
    "atr": 25575.479086468946,
    "volume_ratio": 0.5330666693133895,
    "bottom_features": {
      "double": false,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "top_features": {
      "double": false,
      "divergence": false,
      "extreme": true,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "bottom_neckline": 240500.0,
    "top_neckline": 139600.0,
    "bottom_pivots": [
      1029,
      1036
    ],
    "top_pivots": [
      1031,
      1039
    ]
  },
  "higher_wave": {
    "available": true,
    "bottom_score": 0.35,
    "top_score": 0.1,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 70.98329445029191,
    "sma": [
      101602.5,
      72593.33333333333,
      58419.666666666664
    ],
    "atr": 27674.688508125186,
    "volume_ratio": 1.4227117714965445,
    "bottom_features": {
      "double": false,
      "divergence": false,
      "extreme": false,
      "volume": false,
      "atr": false,
      "neckline": true,
      "ma": true
    },
    "top_features": {
      "double": false,
      "divergence": false,
      "extreme": true,
      "volume": false,
      "atr": false,
      "neckline": false,
      "ma": false
    },
    "bottom_neckline": 70300.0,
    "top_neckline": 44000.0,
    "bottom_pivots": [
      211,
      220
    ],
    "top_pivots": [
      221,
      236
    ]
  },
  "bullish_alignment": 0.4,
  "bearish_alignment": 0.0,
  "buy_liquidity": null,
  "sell_liquidity": null,
  "regime_effect": -0.015,
  "flow_effect": 0.0,
  "reflexivity_effect": -0.010000000000000002,
  "evidence_refs": [
    "bars:1w",
    "bars:1mo"
  ]
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'regime_effect': -0.015, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'batch_id': '2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/1y/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "056e31c0-727d-507f-9298-ccad42b6ff7b",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "056e31c0-727d-507f-9298-ccad42b6ff7b",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "056e31c0-727d-507f-9298-ccad42b6ff7b",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.5892750000000001,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "056e31c0-727d-507f-9298-ccad42b6ff7b",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.07743254584628867,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "056e31c0-727d-507f-9298-ccad42b6ff7b",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

negative_paths (up to five; never padded)
```json
[
  {
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "hypothesis_id": "c1579709-ea03-5a41-99b3-be756525ca0f",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "edge_ids": [
      "us_10y_yield_to_macro",
      "macro_to_price"
    ],
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  }
]
```

### Probability contribution reconstruction
Probability withheld. No prior is relabeled as a forecast; no numeric feedback delta exists.

### What Would Change My Mind
```json
{
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
    "yield_rate"
  ],
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
      "factor_id": "usdkrw",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd",
      "horizon": "1y",
      "evidence_refs": [
        "usdkrw"
      ]
    },
    {
      "factor_id": "samsung_common_price",
      "operator": "lt",
      "threshold": 65000.0,
      "unit": "krw_per_share",
      "horizon": "1y",
      "evidence_refs": [
        "samsung_common_price"
      ]
    },
    {
      "factor_id": "samsung_preferred_price",
      "operator": "lt",
      "threshold": 52000.0,
      "unit": "krw_per_share",
      "horizon": "1y",
      "evidence_refs": [
        "samsung_preferred_price"
      ]
    },
    {
      "factor_id": "us_10y_yield",
      "operator": "lt",
      "threshold": 4.0,
      "unit": "percent",
      "horizon": "1y",
      "evidence_refs": [
        "us_10y_yield"
      ]
    }
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## Findings for the next PDCA
- Mapped new families with no frozen graph route do not contribute direction.
- Original level normalization is unchanged; semantic change is an eligibility gate, not its sign.
- Coverage can include value-only evidence; confidence and probability are distinct.
- Calibration is unvalidated; reversal scores are not calibrated probabilities.
- OP-F01: conservative US/FX date-end timestamps retained; latest cash-session data may be excluded.
- OP-F02: prior-close intraday bars remain subject to frozen freshness, including midday exceptions.
