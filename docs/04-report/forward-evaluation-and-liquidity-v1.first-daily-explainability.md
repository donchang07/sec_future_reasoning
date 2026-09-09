# live-forward-v2 — sealed forward evidence

Run: e5b62fea-3b19-5fc2-8a7a-b1e1788408f2
Cutoff / prediction: 2026-09-09T07:16:28.273912+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-09T06:30:00+00:00', 'source_refs': ['raw:f109033f3b8cc120844ffa00f92627a73a527018b644604cdd8803e20cdc76cf'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 197500.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 44.4074% | 34.1754% | 21.4172% | 16.1764% | 10.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
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
    "age_hours": 0.7745205311111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:27.359009Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f109033f3b8cc120844ffa00f92627a73a527018b644604cdd8803e20cdc76cf",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 0.7745205311111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:27.760612Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 0.7745205311111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:27.673036Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 3.2747983088888892,
    "authority": "official_original",
    "collected_at": "2026-09-09T07:16:27.573425Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "provider": "US Treasury",
    "raw_sha256": "75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e",
    "reason": null,
    "released_at": null,
    "rows": 172,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 8.274798308888888,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:27.928391Z",
    "excluded": {
      "incomplete": 2,
      "invalid": 43,
      "off_grid": 0
    },
    "instrument": "KRW=X",
    "latest_effective_at": "2026-09-08T22:59:59Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563",
    "reason": null,
    "released_at": null,
    "rows": 218,
    "source_id": "usdkrw",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 0.7745205311111112,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:28.272912Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-09T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c7233325897d4857661474676bd8eab02ebae4f85584e6e17e504c29f2a548f5",
    "reason": null,
    "released_at": null,
    "rows": 244,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": 3.2747983088888892,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-09T07:16:28.253918Z",
    "excluded": {
      "incomplete": 1,
      "invalid": 52,
      "off_grid": 0
    },
    "instrument": "DX-Y.NYB",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b1a3ea1cd5a5d335f56e82214e6553378fdc662db4e03d3eb007f5e0846843a7",
    "reason": null,
    "released_at": null,
    "rows": 251,
    "source_id": "dxy",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "unavailable",
    "collected_at": "2026-09-09T07:16:27.760612Z",
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
    "collected_at": "2026-09-09T07:16:27.760612Z",
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
    "collected_at": "2026-09-09T07:16:27.760612Z",
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
    "collected_at": "2026-09-09T07:16:27.760612Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-09T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-04T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-09-09T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 1.0, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.9
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'dxy', 'source_ref': 'raw:b1a3ea1cd5a5d335f56e82214e6553378fdc662db4e03d3eb007f5e0846843a7'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c7233325897d4857661474676bd8eab02ebae4f85584e6e17e504c29f2a548f5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_rsi_14@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_trend_alignment@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_volume_z@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-19T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-08T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-09T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-21T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-30T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-04T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-05T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-31T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-01T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-04T22:59:59+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1w/technical",
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
    "atr": 10957.338268841326,
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
    "rsi": 54.72382942450808,
    "sma": [
      191245.0,
      191940.0,
      178846.66666666666
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
    "volume_ratio": 0.6310531784313187
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 1344.3693849146864,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 200000.0,
    "bottom_pivots": [
      253,
      262
    ],
    "bottom_score": 0.1,
    "rsi": 48.38655878420767,
    "sma": [
      199120.0,
      194151.66666666666,
      191211.66666666666
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
    "top_neckline": 197200.0,
    "top_pivots": [
      249,
      257
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "d113bdf7-7c48-57fe-b755-3fdb01a9bd5d",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6075
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d113bdf7-7c48-57fe-b755-3fdb01a9bd5d",
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
    "hypothesis_id": "d113bdf7-7c48-57fe-b755-3fdb01a9bd5d",
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
    "hypothesis_id": "d113bdf7-7c48-57fe-b755-3fdb01a9bd5d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.09565754584628867
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "d113bdf7-7c48-57fe-b755-3fdb01a9bd5d",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "usdkrw_to_macro/macro_to_price",
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253
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
    "hypothesis_id": "7beb1ae8-6037-58bf-8af5-5371d4a818c0",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.6698465145587307, -0.502860183908016, -0.166986330650723] | {'down': 0.3449713981609198, 'flat': 0.24833013669349277, 'up': 0.40669846514558733} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3449713981609198, 'flat': 0.24833013669349277, 'up': 0.40669846514558733} | [4.316946085228867, -3.1732308826509237, -1.1437152025779385] | {'down': 0.3132390893344106, 'flat': 0.23689298466771339, 'up': 0.449867925997876} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3132390893344106, 'flat': 0.23689298466771339, 'up': 0.449867925997876} | [3.6475925784543395, -2.596178013042494, -1.051414565411843] | {'down': 0.28727730920398564, 'flat': 0.22637883901359496, 'up': 0.4863438517824194} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.28727730920398564, 'flat': 0.22637883901359496, 'up': 0.4863438517824194} | [3.6518004098825383, -2.5270953465680144, -1.1247050633145155] | {'down': 0.2620063557383055, 'flat': 0.2151317883804498, 'up': 0.5228618558812448} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2620063557383055, 'flat': 0.2151317883804498, 'up': 0.5228618558812448} | [-6.0092729417243085, 6.736035538354673, -0.7267625966303815] | {'down': 0.32936671112185223, 'flat': 0.207864162414146, 'up': 0.4627691264640017} |
| 5 | E12/causal | ['usdkrw'] | {'down': 0.32936671112185223, 'flat': 0.207864162414146, 'up': 0.4627691264640017} | [0.21116464818912717, -0.15930275421912055, -0.051861893969998296] | {'down': 0.327773683579661, 'flat': 0.207345543474446, 'up': 0.464880772945893} |
| 6 | E10/causal | ['e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1w/technical'] | {'down': 0.327773683579661, 'flat': 0.207345543474446, 'up': 0.464880772945893} | [1.1599765549280994, -1.0712031409383593, -0.08877341398973448] | {'down': 0.31706165217027743, 'flat': 0.20645780933454866, 'up': 0.47648053849517397} |
| 7 | E17/scenario | ['b161ca82-ffb8-58b4-bcd3-da1544885234', '7ebd34da-d9eb-5f2a-97c9-fd63e89bebc5', '24ade68e-0c22-5e01-a34b-ebaa252622af', '499331c8-8072-5b05-9c54-6e99d9feac57'] | {'down': 0.31706165217027743, 'flat': 0.20645780933454866, 'up': 0.47648053849517397} | [0.1691082891893958, 2.459391285266693, -2.628499574456095] | {'down': 0.34165556502294436, 'flat': 0.1801728135899877, 'up': 0.4781716213870679} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.34165556502294436, 'flat': 0.1801728135899877, 'up': 0.4781716213870679} | [-1.7820796747493983, -0.10239612841259627, 1.8844758031619975] | {'down': 0.3406316037388184, 'flat': 0.1990175716216077, 'up': 0.46035082463957394} |
| 9 | E13/history | [] | {'down': 0.3406316037388184, 'flat': 0.1990175716216077, 'up': 0.46035082463957394} | [0.0, 0.0, 0.0] | {'down': 0.3406316037388184, 'flat': 0.1990175716216077, 'up': 0.46035082463957394} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.3406316037388184, 'flat': 0.1990175716216077, 'up': 0.46035082463957394} | [-1.6276344333155057, 0.11220918367602639, 1.5154252496394793] | {'down': 0.34175369557557866, 'flat': 0.21417182411800248, 'up': 0.4440744803064189} |
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
        "usdkrw"
      ],
      "factor_id": "usdkrw",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd"
    },
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
    }
  ],
  "missing_coverage": [],
  "missing_strong": [
    "foreign_net_buy",
    "institution_net_buy"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1m
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 1.0, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.4252500000000001
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'dxy', 'source_ref': 'raw:b1a3ea1cd5a5d335f56e82214e6553378fdc662db4e03d3eb007f5e0846843a7'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c7233325897d4857661474676bd8eab02ebae4f85584e6e17e504c29f2a548f5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_rsi_14@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_trend_alignment@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_volume_z@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-19T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-08T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-09T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-21T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-30T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-04T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-05T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-31T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-01T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-04T22:59:59+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1m/technical",
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
    "atr": 10957.338268841326,
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
    "rsi": 54.72382942450808,
    "sma": [
      191245.0,
      191940.0,
      178846.66666666666
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
    "volume_ratio": 0.6310531784313187
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'regime_effect': 0.037500000000000006}
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
    "hypothesis_id": "29c7cd5d-0a33-593f-ae47-1afa0f14e283",
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
    "hypothesis_id": "29c7cd5d-0a33-593f-ae47-1afa0f14e283",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "29c7cd5d-0a33-593f-ae47-1afa0f14e283",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6530625
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "29c7cd5d-0a33-593f-ae47-1afa0f14e283",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.14122004584628867
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "29c7cd5d-0a33-593f-ae47-1afa0f14e283",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "usdkrw_to_macro/macro_to_price",
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253
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
    "hypothesis_id": "8e6d1f18-aecf-500c-b589-e679a3156771",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.384175547809551, -0.2887629627485566, -0.0954125850609916] | {'down': 0.3471123703725144, 'flat': 0.24904587414939008, 'up': 0.40384175547809553} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3471123703725144, 'flat': 0.24904587414939008, 'up': 0.40384175547809553} | [1.7897404417237306, -1.332705227690112, -0.4570352140336159] | {'down': 0.3337853180956133, 'flat': 0.24447552200905392, 'up': 0.42173915989533284} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3337853180956133, 'flat': 0.24447552200905392, 'up': 0.42173915989533284} | [2.8898772221679137, -2.110206302911627, -0.7796709192562867] | {'down': 0.312683255066497, 'flat': 0.23667881281649106, 'up': 0.450637932117012} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.312683255066497, 'flat': 0.23667881281649106, 'up': 0.450637932117012} | [2.9169465055647548, -2.0807920352345857, -0.8361544703301749] | {'down': 0.29187533471415117, 'flat': 0.2283172681131893, 'up': 0.4798073971726595} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.29187533471415117, 'flat': 0.2283172681131893, 'up': 0.4798073971726595} | [-4.496084779643416, 5.228382243489177, -0.7322974638457547] | {'down': 0.34415915714904294, 'flat': 0.22099429347473176, 'up': 0.43484654937622536} |
| 5 | E12/causal | ['usdkrw'] | {'down': 0.34415915714904294, 'flat': 0.22099429347473176, 'up': 0.43484654937622536} | [0.15639274045043394, -0.11889877691086959, -0.03749396353957268] | {'down': 0.34297016937993424, 'flat': 0.22061935383933604, 'up': 0.4364104767807297} |
| 6 | E10/causal | ['e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1m/technical'] | {'down': 0.34297016937993424, 'flat': 0.22061935383933604, 'up': 0.4364104767807297} | [2.2842719707122985, -2.137650141354086, -0.14662182935821222] | {'down': 0.3215936679663934, 'flat': 0.2191531355457539, 'up': 0.4592531964878527} |
| 7 | E17/scenario | ['d87d2c43-3bac-5b5d-bec7-a4d44a8c1f17', 'b67bce0d-a073-5356-bd06-74d84652f6ca', '3f1a8026-1914-54cf-9bc0-157f2fcde74a', '5e48fbdd-ac8a-50d2-876c-af824d09dbe8'] | {'down': 0.3215936679663934, 'flat': 0.2191531355457539, 'up': 0.4592531964878527} | [0.28192976379148305, 2.967434575113681, -3.2493643389051527] | {'down': 0.3512680137175302, 'flat': 0.18665949215670238, 'up': 0.4620724941257675} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3512680137175302, 'flat': 0.18665949215670238, 'up': 0.4620724941257675} | [-1.5910570703810134, -0.2216505052126838, 1.8127075755936999] | {'down': 0.34905150866540335, 'flat': 0.20478656791263938, 'up': 0.4461619234219574} |
| 9 | E13/history | [] | {'down': 0.34905150866540335, 'flat': 0.20478656791263938, 'up': 0.4461619234219574} | [0.0, 0.0, 0.0] | {'down': 0.34905150866540335, 'flat': 0.20478656791263938, 'up': 0.4461619234219574} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.34905150866540335, 'flat': 0.20478656791263938, 'up': 0.4461619234219574} | [-1.4357437695335817, -0.024152857434045494, 1.4598966269676188] | {'down': 0.3488099800910629, 'flat': 0.21938553418231557, 'up': 0.43180448572662156} |
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
        "usdkrw"
      ],
      "factor_id": "usdkrw",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd"
    },
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
    "samsung_eps_revision"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## 1y
Eligibility: False; reasons: ['coverage:memory', 'memory_family_quorum']
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 1.0, 'memory': 0.26666666666666666, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.15746400000000002
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '97e4708288a143695e7269f71646f14dedcdbfe8d2d23cf90a13b9fbd98a6c79'}, {'reason': 'no_mapping_rule', 'source_field': 'dxy', 'source_ref': 'raw:b1a3ea1cd5a5d335f56e82214e6553378fdc662db4e03d3eb007f5e0846843a7'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c7233325897d4857661474676bd8eab02ebae4f85584e6e17e504c29f2a548f5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_rsi_14@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_trend_alignment@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#preferred_volume_z@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:e9854160a4187c72c186c60175c1128b38aa96fe7b84676844c6505bb824e484#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:e300254dccf4e1cc1bad7d1e4add7ea59ea3a626d493bd96453047e7ab3e5345#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-19T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-06-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-08T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-09T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-15T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-16T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-21T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-22T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-23T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-29T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-07-30T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-04T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-05T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-06T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-07T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-10T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-11T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-12T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-13T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-14T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-17T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-18T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-20T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-24T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-25T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-26T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-27T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-28T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-08-31T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-01T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-02T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-03T22:59:59+00:00'}, {'reason': 'stale', 'source_field': 'usdkrw', 'source_ref': 'raw:5c3cc30e3461fb02a17aef3e11aefc03543ce5c2aee06b81c090211398f3c563#usdkrw@2026-09-04T22:59:59+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1y/technical",
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
Feedback applied once: {'batch_id': 'e5b62fea-3b19-5fc2-8a7a-b1e1788408f2/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "c764dc59-57f6-50a7-ba43-a4d313998437",
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
    "hypothesis_id": "c764dc59-57f6-50a7-ba43-a4d313998437",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c764dc59-57f6-50a7-ba43-a4d313998437",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.5892750000000001
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c764dc59-57f6-50a7-ba43-a4d313998437",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.07743254584628867
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "usdkrw_to_macro",
      "macro_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c764dc59-57f6-50a7-ba43-a4d313998437",
    "node_ids": [
      "usdkrw",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "usdkrw_to_macro/macro_to_price",
    "root_evidence_group": "usdkrw",
    "sign": 1,
    "strength": 0.017361145019531253
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
    "hypothesis_id": "38e8434c-bbef-50ad-9a3b-f5a00e2109e2",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.6479999999999999
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
        "usdkrw"
      ],
      "factor_id": "usdkrw",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 1350.0,
      "unit": "krw_per_usd"
    },
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
    "yield_rate"
  ]
}
```
Resolve these evidence/gate conditions in a NEW run. This prediction will not be rewritten.

## Findings for the next PDCA
- Mapped new families with no frozen graph route do not contribute direction.
- Original level normalization is unchanged; semantic change is an eligibility gate, not its sign.
- Coverage can include value-only evidence; confidence and probability are distinct.
- Calibration is unvalidated; reversal scores are not calibrated probabilities.
