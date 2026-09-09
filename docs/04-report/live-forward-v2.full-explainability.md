# live-forward-v2 — sealed forward evidence

Run: e51235a7-9c47-575b-b152-dab8cee04c17
Cutoff / prediction: 2026-09-09T06:42:34.193123+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'value': 197500.0, 'unit': 'krw_per_share', 'timeframe': '30m', 'effective_at': '2026-09-09T06:00:00+00:00', 'definition': 'last eligible completed close, not execution quote', 'source_refs': ['raw:df657b89531876137b00f429aa3ec818f6b77fbd869406cc21dffcbfb759cd9a']}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 40.8039% | 37.1848% | 22.0113% | 11.9883% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 41.1889% | 36.4456% | 22.3655% | 5.6435% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 41.3002% / 36.7398% / 21.9599% | 40.8039% / 37.1848% / 22.0113% | [-0.49637631840980245, 0.44499264946216144, 0.05138366894763824] |
| 1m | 40.2916% / 37.2812% / 22.4271% | 41.1889% / 36.4456% / 22.3655% | [0.8973117346629256, -0.83564894390456, -0.06166279075835723] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "source_id": "preferred_30m",
    "instrument": "005935.KS",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "df657b89531876137b00f429aa3ec818f6b77fbd869406cc21dffcbfb759cd9a",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T06:00:00Z",
    "collected_at": "2026-09-09T06:42:33.167096Z",
    "released_at": null,
    "age_hours": 0.7094980897222223,
    "rows": 264,
    "excluded": {
      "incomplete": 1,
      "off_grid": 0,
      "invalid": 0
    },
    "used_by_model": true,
    "reason": null
  },
  {
    "source_id": "preferred_daily",
    "instrument": "005935.KS",
    "provider": "Yahoo Finance",
    "authority": "public_vendor_fallback",
    "raw_sha256": "4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a",
    "status": "fresh",
    "latest_effective_at": "2026-09-08T06:30:00Z",
    "collected_at": "2026-09-09T06:42:33.658215Z",
    "released_at": null,
    "age_hours": 24.209498089722224,
    "rows": 4931,
    "excluded": {
      "incomplete": 1,
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
    "raw_sha256": "c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4",
    "status": "fresh",
    "latest_effective_at": "2026-09-08T06:30:00Z",
    "collected_at": "2026-09-09T06:42:33.719110Z",
    "released_at": null,
    "age_hours": 24.209498089722224,
    "rows": 4933,
    "excluded": {
      "incomplete": 1,
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
    "raw_sha256": "75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "collected_at": "2026-09-09T06:42:33.422384Z",
    "released_at": null,
    "age_hours": 2.7097758675,
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
    "raw_sha256": "2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85",
    "status": "fresh",
    "latest_effective_at": "2026-09-08T22:59:59Z",
    "collected_at": "2026-09-09T06:42:33.795211Z",
    "released_at": null,
    "age_hours": 7.7097758675,
    "rows": 218,
    "excluded": {
      "incomplete": 2,
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
    "raw_sha256": "6eaea0539719c1f83ec17ed7c80d45d085e25270170726f96a18fee822dd9866",
    "status": "fresh",
    "latest_effective_at": "2026-09-08T06:30:00Z",
    "collected_at": "2026-09-09T06:42:33.996055Z",
    "released_at": null,
    "age_hours": 24.209498089722224,
    "rows": 243,
    "excluded": {
      "incomplete": 1,
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
    "raw_sha256": "937bfbcd5185881c40f8ebe22a933962a428634aec8cf9d14e02086f7bd749d4",
    "status": "fresh",
    "latest_effective_at": "2026-09-09T03:59:59Z",
    "collected_at": "2026-09-09T06:42:34.192122Z",
    "released_at": null,
    "age_hours": 2.7097758675,
    "rows": 251,
    "excluded": {
      "incomplete": 1,
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
    "collected_at": "2026-09-09T06:42:33.719110Z",
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
    "collected_at": "2026-09-09T06:42:33.720106Z",
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
    "collected_at": "2026-09-09T06:42:33.720106Z",
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
    "collected_at": "2026-09-09T06:42:33.720106Z",
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
Bar boundaries: {'30m': {'count': 264, 'last': '2026-09-09T06:00:00+00:00'}, '1d': {'count': 4931, 'last': '2026-09-08T06:30:00+00:00'}, '1w': {'count': 1042, 'last': '2026-09-04T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'macro': 1.0, 'memory': 0.5833333333333334, 'earnings': 0.5, 'flow': 0.0, 'price_regime': 1.0, 'ai_demand': 0.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.9
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy']
Unmapped/conflicting evidence: [{'source_ref': 'raw:937bfbcd5185881c40f8ebe22a933962a428634aec8cf9d14e02086f7bd749d4', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:6eaea0539719c1f83ec17ed7c80d45d085e25270170726f96a18fee822dd9866', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "e51235a7-9c47-575b-b152-dab8cee04c17/1w/technical",
  "primary": "30m",
  "higher": "1d",
  "wave": {
    "available": true,
    "bottom_score": 0.0,
    "top_score": 0.1,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 48.38655878420767,
    "sma": [
      199270.0,
      193956.66666666666,
      191219.16666666666
    ],
    "atr": 1447.7824145235086,
    "volume_ratio": 0.8941167552133016,
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
    "bottom_neckline": 203000.0,
    "top_neckline": 197200.0,
    "bottom_pivots": [
      246,
      253
    ],
    "top_pivots": [
      249,
      257
    ]
  },
  "higher_wave": {
    "available": true,
    "bottom_score": 0.45000000000000007,
    "top_score": 0.2,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 55.26986745784625,
    "sma": [
      190380.0,
      192248.33333333334,
      178375.83333333334
    ],
    "atr": 11461.748904906044,
    "volume_ratio": 0.8887888518056414,
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
  "bullish_alignment": 0.4,
  "bearish_alignment": 0.0,
  "buy_liquidity": null,
  "sell_liquidity": null,
  "regime_effect": -0.015,
  "flow_effect": 0.0,
  "reflexivity_effect": -0.010000000000000002,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ]
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'regime_effect': -0.015, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'batch_id': 'e51235a7-9c47-575b-b152-dab8cee04c17/1w/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-08': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-07': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "8c741f17-bae7-560b-9b49-ca358bf97315",
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
    "strength": 0.386775,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "8c741f17-bae7-560b-9b49-ca358bf97315",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "8c741f17-bae7-560b-9b49-ca358bf97315",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "8c741f17-bae7-560b-9b49-ca358bf97315",
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
    "strength": 0.05291821068092441,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "8c741f17-bae7-560b-9b49-ca358bf97315",
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
    "hypothesis_id": "2157622f-b5df-524d-8111-9fbaa142bab7",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'up': 0.4, 'down': 0.35, 'flat': 0.25} | [0.37016105399403365, -0.2782460666559683, -0.09191498733805703] | {'up': 0.40370161053994036, 'down': 0.3472175393334403, 'flat': 0.24908085012661943} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'up': 0.40370161053994036, 'down': 0.3472175393334403, 'flat': 0.24908085012661943} | [2.7329629469351913, -2.027224760345503, -0.7057381865896994] | {'up': 0.43103124000929227, 'down': 0.32694529172998527, 'flat': 0.24202346826072244} |
| 2 | E12/causal | ['samsung_common_price'] | {'up': 0.43103124000929227, 'down': 0.32694529172998527, 'flat': 0.24202346826072244} | [2.4153330620462876, -1.7537067298591724, -0.6616263321871069] | {'up': 0.45518457062975515, 'down': 0.30940822443139354, 'flat': 0.23540720493885137} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'up': 0.45518457062975515, 'down': 0.30940822443139354, 'flat': 0.23540720493885137} | [2.4320014651841637, -1.7319315041573802, -0.7000699610267891] | {'up': 0.4795045852815968, 'down': 0.29208890938981974, 'flat': 0.22840650532858348} |
| 4 | E12/causal | ['us_10y_yield'] | {'up': 0.4795045852815968, 'down': 0.29208890938981974, 'flat': 0.22840650532858348} | [-6.025331775440473, 7.064415619597431, -1.03908384415696] | {'up': 0.41925126752719205, 'down': 0.36273306558579405, 'flat': 0.21801566688701388} |
| 5 | E12/causal | ['usdkrw'] | {'up': 0.41925126752719205, 'down': 0.36273306558579405, 'flat': 0.21801566688701388} | [0.20754019110941768, -0.16152756930304935, -0.046012621806362786] | {'up': 0.4213266694382862, 'down': 0.36111778989276355, 'flat': 0.21755554066895025} |
| 6 | E10/causal | ['e51235a7-9c47-575b-b152-dab8cee04c17/1w/technical'] | {'up': 0.4213266694382862, 'down': 0.36111778989276355, 'flat': 0.21755554066895025} | [0.32064324160605007, -0.30948856291871385, -0.011154678687330666] | {'up': 0.42453310185434673, 'down': 0.3580229042635764, 'flat': 0.21744399388207694} |
| 7 | E17/scenario | ['ccd500b2-df91-524a-aed3-0df7c4c1568f', '65d7df9a-830a-5d3a-923c-2a469f8b8fec', '13aca76c-a0c3-5a1e-a80f-441967e5c0de', 'fba68ed9-40a0-5340-b0fb-35d3a0bb7136'] | {'up': 0.42453310185434673, 'down': 0.3580229042635764, 'flat': 0.21744399388207694} | [0.6503428959852231, 2.430205138080038, -3.0805480340652807] | {'up': 0.43103653081419896, 'down': 0.3823249556443768, 'flat': 0.18663851354142413} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'up': 0.43103653081419896, 'down': 0.3823249556443768, 'flat': 0.18663851354142413} | [-1.2703326339086884, -0.6369868971999204, 1.9073195311086144] | {'up': 0.4183332044751121, 'down': 0.3759550866723776, 'flat': 0.20571170885251028} |
| 9 | E13/history | [] | {'up': 0.4183332044751121, 'down': 0.3759550866723776, 'flat': 0.20571170885251028} | [0.0, 0.0, 0.0] | {'up': 0.4183332044751121, 'down': 0.3759550866723776, 'flat': 0.20571170885251028} |
| 10 | E18/calibration | ['temperature:1.15'] | {'up': 0.4183332044751121, 'down': 0.3759550866723776, 'flat': 0.20571170885251028} | [-1.0294480838282882, -0.4107125466940531, 1.4401606305223469] | {'up': 0.4080387236368292, 'down': 0.37184796120543706, 'flat': 0.22011331515773375} |
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
Unmapped/conflicting evidence: [{'source_ref': 'raw:937bfbcd5185881c40f8ebe22a933962a428634aec8cf9d14e02086f7bd749d4', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:6eaea0539719c1f83ec17ed7c80d45d085e25270170726f96a18fee822dd9866', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "e51235a7-9c47-575b-b152-dab8cee04c17/1m/technical",
  "primary": "1d",
  "higher": "1w",
  "wave": {
    "available": true,
    "bottom_score": 0.45000000000000007,
    "top_score": 0.2,
    "bottom_confirmed": false,
    "top_confirmed": false,
    "rsi": 55.26986745784625,
    "sma": [
      190380.0,
      192248.33333333334,
      178375.83333333334
    ],
    "atr": 11461.748904906044,
    "volume_ratio": 0.8887888518056414,
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
Feedback applied once: {'regime_effect': 0.037500000000000006, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'batch_id': 'e51235a7-9c47-575b-b152-dab8cee04c17/1m/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "557a59fd-77e6-5c42-9391-3c0b813cf686",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "557a59fd-77e6-5c42-9391-3c0b813cf686",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "557a59fd-77e6-5c42-9391-3c0b813cf686",
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
    "strength": 0.45056250000000003,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "557a59fd-77e6-5c42-9391-3c0b813cf686",
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
    "strength": 0.11670571068092442,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "557a59fd-77e6-5c42-9391-3c0b813cf686",
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
    "hypothesis_id": "e3222f19-f9f6-5a3b-9793-992bcca6ea86",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'up': 0.4, 'down': 0.35, 'flat': 0.25} | [0.317408957961951, -0.23864780355886683, -0.0787611544030925] | {'up': 0.40317408957961953, 'down': 0.3476135219644113, 'flat': 0.24921238845596907} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'up': 0.40317408957961953, 'down': 0.3476135219644113, 'flat': 0.24921238845596907} | [1.2320631152767048, -0.920149175913848, -0.3119139393628484] | {'up': 0.4154947207323866, 'down': 0.33841203020527283, 'flat': 0.2460932490623406} |
| 2 | E12/causal | ['samsung_common_price'] | {'up': 0.4154947207323866, 'down': 0.33841203020527283, 'flat': 0.2460932490623406} | [1.9164823883406346, -1.4123275359092413, -0.5041548524313877] | {'up': 0.4346595446157929, 'down': 0.3242887548461804, 'flat': 0.24105170053802671} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'up': 0.4346595446157929, 'down': 0.3242887548461804, 'flat': 0.24105170053802671} | [1.9333003409043203, -1.4023046883311074, -0.5309956525732074] | {'up': 0.45399254802483613, 'down': 0.31026570796286934, 'flat': 0.23574174401229464} |
| 4 | E12/causal | ['us_10y_yield'] | {'up': 0.45399254802483613, 'down': 0.31026570796286934, 'flat': 0.23574174401229464} | [-4.47823307204226, 5.358595734717681, -0.8803626626754296] | {'up': 0.40921021730441354, 'down': 0.36385166531004615, 'flat': 0.22693811738554034} |
| 5 | E12/causal | ['usdkrw'] | {'up': 0.40921021730441354, 'down': 0.36385166531004615, 'flat': 0.22693811738554034} | [0.15416848381509252, -0.11952536256406021, -0.03464312125104063] | {'up': 0.41075190214256446, 'down': 0.36265641168440554, 'flat': 0.22659168617302994} |
| 6 | E10/causal | ['e51235a7-9c47-575b-b152-dab8cee04c17/1m/technical'] | {'up': 0.41075190214256446, 'down': 0.36265641168440554, 'flat': 0.22659168617302994} | [1.895740034143245, -1.8227860052439093, -0.07295402889933023] | {'up': 0.4297093024839969, 'down': 0.34442855163196645, 'flat': 0.22586214588403664} |
| 7 | E17/scenario | ['5569c2f9-123c-5791-9d06-ae05b10272e6', '158fee6a-24b0-5b73-848d-7302db6e5efc', 'aafa6e32-8a50-5ba1-bbef-fcabe832cded', 'da488f45-c470-58a4-b261-f6ef83ea4b62'] | {'up': 0.4297093024839969, 'down': 0.34442855163196645, 'flat': 0.22586214588403664} | [0.6668813160130127, 2.813170389865516, -3.480051705878534] | {'up': 0.43637811564412704, 'down': 0.3725602555306216, 'flat': 0.1910616288252513} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'up': 0.43637811564412704, 'down': 0.3725602555306216, 'flat': 0.1910616288252513} | [-1.3405465742479306, -0.5103171164092646, 1.8508636906572007] | {'up': 0.42297264990164773, 'down': 0.36745708436652896, 'flat': 0.2095702657318233} |
| 9 | E13/history | [] | {'up': 0.42297264990164773, 'down': 0.36745708436652896, 'flat': 0.2095702657318233} | [0.0, 0.0, 0.0] | {'up': 0.42297264990164773, 'down': 0.36745708436652896, 'flat': 0.2095702657318233} |
| 10 | E18/calibration | ['temperature:1.15'] | {'up': 0.42297264990164773, 'down': 0.36745708436652896, 'flat': 0.2095702657318233} | [-1.10834091177352, -0.30010964776738813, 1.4084505595409107] | {'up': 0.41188924078391254, 'down': 0.3644559878888551, 'flat': 0.2236547713272324} |
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
Unmapped/conflicting evidence: [{'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'reason': 'horizon_excluded'}, {'source_ref': '6f31fb709f01491305949f828b1112cadff9c42399a4a12bcc03763308ab2922', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'reason': 'horizon_excluded'}, {'source_ref': 'raw:937bfbcd5185881c40f8ebe22a933962a428634aec8cf9d14e02086f7bd749d4', 'source_field': 'dxy', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:6eaea0539719c1f83ec17ed7c80d45d085e25270170726f96a18fee822dd9866', 'source_field': 'kospi', 'reason': 'no_mapping_rule'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_rsi_14@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_rsi_14', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_trend_alignment@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_trend_alignment', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-03T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#preferred_volume_z@2026-09-04T06:30:00+00:00', 'source_field': 'preferred_volume_z', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:c67492106ab47fa46b91e8c11235527bb0fa728b2f334e5de9360dc68db9a4f4#samsung_common_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_common_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-17T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-06-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-08T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-09T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-15T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-16T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-22T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-23T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-29T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-30T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-07-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-05T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-06T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-07T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-10T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-11T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-12T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-13T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-14T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-18T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-19T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-20T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-21T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-24T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-25T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-26T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-27T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-28T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-08-31T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-01T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-02T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-03T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:4618b37a64abf3d9a1981eba6c775b797a871bb50fa9d19bc15a2f2bb5aa7a5a#samsung_preferred_price@2026-09-04T06:30:00+00:00', 'source_field': 'samsung_preferred_price', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-08T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-09T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-15T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-16T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-17T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-22T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-23T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-29T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-30T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-01-31T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-10T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-11T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-12T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-13T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-14T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-18T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-19T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-20T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-21T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-24T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-25T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-26T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-27T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-02-28T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-03T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-04T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-05T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-06T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-07T04:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-03-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-04-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-05-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-06-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-03T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-09T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-10T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-16T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-17T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-23T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-24T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-30T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-07-31T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-04T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-05T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-06T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-07T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-08T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-11T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-12T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-13T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-14T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-15T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-18T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-19T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-20T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-21T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-22T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-25T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-26T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-27T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-28T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-08-29T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-01T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:75e737940eaae321598198dbe5f794f7750947d69bcb091a788f90de499fb35e#us_10y_yield@2026-09-02T03:59:59+00:00', 'source_field': 'us_10y_yield', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-19T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-06-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-08T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-09T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-15T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-16T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-21T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-22T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-23T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-29T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-07-30T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-05T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-06T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-07T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-10T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-11T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-12T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-13T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-14T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-17T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-18T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-20T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-24T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-25T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-26T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-27T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-28T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-08-31T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-01T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-02T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-03T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}, {'source_ref': 'raw:2e01784dabb2582a893475e109981aa1038550f408d4bf819e785ba03aa59c85#usdkrw@2026-09-04T22:59:59+00:00', 'source_field': 'usdkrw', 'reason': 'stale'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "e51235a7-9c47-575b-b152-dab8cee04c17/1y/technical",
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
Feedback applied once: {'regime_effect': -0.015, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'batch_id': 'e51235a7-9c47-575b-b152-dab8cee04c17/1y/technical', 'flow_applied': False}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'score': 1.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_inventory': None, 'memory_bit_shipment': None, 'semiconductor_export_momentum': 1.0}, 'positive_families': ['semiconductor_export_momentum'], 'negative_families': [], 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment'], 'conflict': 0.0, 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}}

positive_paths (up to five; never padded)
```json
[
  {
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "hypothesis_id": "51854548-757a-5822-af33-0a0dcd90d524",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "hypothesis_id": "51854548-757a-5822-af33-0a0dcd90d524",
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
    "strength": 0.405,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "hypothesis_id": "51854548-757a-5822-af33-0a0dcd90d524",
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
    "strength": 0.386775,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "hypothesis_id": "51854548-757a-5822-af33-0a0dcd90d524",
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
    "strength": 0.05291821068092441,
    "confidence": 0.9025,
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6"
  },
  {
    "path_id": "usdkrw_to_macro/macro_to_price",
    "hypothesis_id": "51854548-757a-5822-af33-0a0dcd90d524",
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
    "hypothesis_id": "1f4ec501-2ba6-520f-957d-332ded9b54a2",
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
