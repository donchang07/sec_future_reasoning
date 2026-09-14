# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: d2d7d4b7-78c3-5927-87b4-2ebedb62614a
Cutoff / prediction: 2026-09-14T22:00:11.108958+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-14T06:30:00+00:00', 'source_refs': ['raw:7c0920c75020c2fcae3a37ebffc895172a61fa904ad34b0076db6eba292cb886'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 183400.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 35.8765% | 42.0499% | 22.0736% | 5.0824% | 10.0000% | 20.0000% | 0.13333333333333333/0.2666666666666667 | None/None | WAIT |
| 1m | 37.1998% | 40.3892% | 22.4110% | 4.0478% | 30.0000% | 45.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 36.3437% / 41.5743% / 22.0820% | 35.8765% / 42.0499% / 22.0736% | [-0.46715492028214234, 0.4755603419140553, -0.008405421631918486] |
| 1m | 37.7087% / 39.8758% / 22.4156% | 37.1998% / 40.3892% / 22.4110% | [-0.5088397576639869, 0.5134233234215191, -0.004583565757526609] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503085821666666,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T22:00:10.225373Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7c0920c75020c2fcae3a37ebffc895172a61fa904ad34b0076db6eba292cb886",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503085821666666,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T22:00:10.582584Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503085821666666,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T22:00:10.687523Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5030858216666667,
    "authority": "official_original",
    "collected_at": "2026-09-14T22:00:10.077091Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-14T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077",
    "reason": null,
    "released_at": null,
    "rows": 176,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T22:00:10.640587Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "9b3f2add08eb5014947599985798524a5a0ce6789135c169f626a3125943206c",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50308582166667,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T22:00:10.660585Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "985d1521b871ff40eb2ba968a000b1e24d5347128e5e12645c73cb48435e440b",
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
    "collected_at": "2026-09-14T22:00:11.107959Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f058245a9b1e46e919465e10d4eba387fb8c7a4c865991859118967fb3bb274e",
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
    "collected_at": "2026-09-14T22:00:10.640587Z",
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
    "collected_at": "2026-09-14T22:00:10.640587Z",
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
    "collected_at": "2026-09-14T22:00:10.640587Z",
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
    "collected_at": "2026-09-14T22:00:10.640587Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-14T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-09-14T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:985d1521b871ff40eb2ba968a000b1e24d5347128e5e12645c73cb48435e440b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "d2d7d4b7-78c3-5927-87b4-2ebedb62614a/1w/technical",
  "bearish_alignment": 0.2666666666666667,
  "bullish_alignment": 0.13333333333333333,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 10799.625428806265,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4924
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 46.234575210090355,
    "sma": [
      191755.0,
      190285.0,
      180073.33333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4919,
      4929
    ],
    "top_score": 0.45000000000000007,
    "volume_ratio": 0.7958506833393116
  },
  "primary": "30m",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1293.5021478849249,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": true,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 194300.0,
    "bottom_pivots": [
      223,
      230
    ],
    "bottom_score": 0.1,
    "rsi": 24.016727932218686,
    "sma": [
      188050.0,
      194829.16666666666,
      192080.41666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 185000.0,
    "top_pivots": [
      225,
      233
    ],
    "top_score": 0.2,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'd2d7d4b7-78c3-5927-87b4-2ebedb62614a/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "9239491e-d806-5a1b-bfc1-d060dcfd9684",
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
    "hypothesis_id": "9239491e-d806-5a1b-bfc1-d060dcfd9684",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
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
    "hypothesis_id": "e7bf7ad6-daa8-5123-9e23-4016bc95f086",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7856999999999998
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e7bf7ad6-daa8-5123-9e23-4016bc95f086",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": -1,
    "strength": 0.15322500000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e7bf7ad6-daa8-5123-9e23-4016bc95f086",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.06905823466378021
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.37045588249725037, 0.4626677858758588, -0.09221190337861673] | {'down': 0.35462667785875857, 'flat': 0.24907788096621383, 'up': 0.3962954411750275} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35462667785875857, 'flat': 0.24907788096621383, 'up': 0.3962954411750275} | [-0.8234822420298549, 1.0356035442224465, -0.21212130219258885] | {'down': 0.36498271330098303, 'flat': 0.24695666794428794, 'up': 0.38806061875472897} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36498271330098303, 'flat': 0.24695666794428794, 'up': 0.38806061875472897} | [2.3632236924754304, -1.7987059179304932, -0.5645177745449287] | {'down': 0.3469956541216781, 'flat': 0.24131149019883866, 'up': 0.41169285567948327} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3469956541216781, 'flat': 0.24131149019883866, 'up': 0.41169285567948327} | [2.4001924838574884, -1.7908413776234144, -0.6093511062340767] | {'down': 0.32908724034544395, 'flat': 0.2352179791364979, 'up': 0.43569478051805816} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.32908724034544395, 'flat': 0.2352179791364979, 'up': 0.43569478051805816} | [-7.28906443895318, 9.02605394697637, -1.7369895080231927] | {'down': 0.41934777981520766, 'flat': 0.21784808405626596, 'up': 0.36280413612852636} |
| 5 | E10/causal | ['d2d7d4b7-78c3-5927-87b4-2ebedb62614a/1w/technical'] | {'down': 0.41934777981520766, 'flat': 0.21784808405626596, 'up': 0.36280413612852636} | [-0.7316561887466821, 0.7583341778897412, -0.0266779891430452] | {'down': 0.42693112159410507, 'flat': 0.2175813041648355, 'up': 0.35548757424105953} |
| 6 | E17/scenario | ['5d53c32b-32a5-5a05-85b1-6c275024aa45', '18a2e44d-cc86-5042-8b30-c528ce883a02', '5e936c20-36c1-5f06-ac35-cfe34ee51505', 'ea94bc0d-08f5-5b1b-b8e3-66bec039338b'] | {'down': 0.42693112159410507, 'flat': 0.2175813041648355, 'up': 0.35548757424105953} | [0.9349264057979589, 2.1071496414517945, -3.04207604724977] | {'down': 0.448002618008623, 'flat': 0.1871605436923378, 'up': 0.3648368382990391} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.448002618008623, 'flat': 0.1871605436923378, 'up': 0.3648368382990391} | [-0.41325160469941613, -1.5041902783002326, 1.917441882999646] | {'down': 0.4329607152256207, 'flat': 0.20633496252233427, 'up': 0.36070432225204496} |
| 8 | E13/history | [] | {'down': 0.4329607152256207, 'flat': 0.20633496252233427, 'up': 0.36070432225204496} | [0.0, 0.0, 0.0] | {'down': 0.4329607152256207, 'flat': 0.20633496252233427, 'up': 0.36070432225204496} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4329607152256207, 'flat': 0.20633496252233427, 'up': 0.36070432225204496} | [-0.19388511580448742, -1.2461995144071258, 1.4400846302116244] | {'down': 0.4204987200815494, 'flat': 0.2207358088244505, 'up': 0.3587654710940001} |
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "score"
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.32805
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:985d1521b871ff40eb2ba968a000b1e24d5347128e5e12645c73cb48435e440b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "d2d7d4b7-78c3-5927-87b4-2ebedb62614a/1m/technical",
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
    "atr": 24677.23058029259,
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
      1028,
      1035
    ],
    "bottom_score": 0.0,
    "rsi": 56.527044746782224,
    "sma": [
      192885.0,
      126817.5,
      89079.58333333333
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  },
  "primary": "1d",
  "reflexivity_effect": -0.015000000000000003,
  "regime_effect": -0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 10799.625428806265,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4924
    ],
    "bottom_score": 0.30000000000000004,
    "rsi": 46.234575210090355,
    "sma": [
      191755.0,
      190285.0,
      180073.33333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4919,
      4929
    ],
    "top_score": 0.45000000000000007,
    "volume_ratio": 0.7958506833393116
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'd2d7d4b7-78c3-5927-87b4-2ebedb62614a/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.015000000000000003, 'regime_effect': -0.022500000000000003}
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
    "hypothesis_id": "fe925927-9793-5f5e-b4c5-be4f0e9830a5",
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
    "hypothesis_id": "fe925927-9793-5f5e-b4c5-be4f0e9830a5",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
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
    "hypothesis_id": "2be442da-e968-5591-b189-6e03e0d6e3e4",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7856999999999998
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2be442da-e968-5591-b189-6e03e0d6e3e4",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": -1,
    "strength": 0.16233750000000002
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "2be442da-e968-5591-b189-6e03e0d6e3e4",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.0781707346637802
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.1630169439260809, 0.2033476947052415, -0.04033075077916337] | {'down': 0.3520334769470524, 'flat': 0.24959669249220837, 'up': 0.3983698305607392} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3520334769470524, 'flat': 0.24959669249220837, 'up': 0.3983698305607392} | [-0.33883170274132124, 0.4238986701213532, -0.08506696738002917] | {'down': 0.3562724636482659, 'flat': 0.24874602281840807, 'up': 0.394981513533326} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3562724636482659, 'flat': 0.24874602281840807, 'up': 0.394981513533326} | [1.894131795827475, -1.4271559108190446, -0.4669758850084249] | {'down': 0.3420009045400755, 'flat': 0.24407626396832383, 'up': 0.41392283149160075} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3420009045400755, 'flat': 0.24407626396832383, 'up': 0.41392283149160075} | [1.9170693126017713, -1.4213736549782197, -0.4956956576235655] | {'down': 0.3277871679902933, 'flat': 0.23911930739208817, 'up': 0.43309352461761846} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3277871679902933, 'flat': 0.23911930739208817, 'up': 0.43309352461761846} | [-5.420557322153696, 6.676199516029535, -1.2556421938758278] | {'down': 0.39454916315058863, 'flat': 0.2265628854533299, 'up': 0.3788879513960815} |
| 5 | E10/causal | ['d2d7d4b7-78c3-5927-87b4-2ebedb62614a/1m/technical'] | {'down': 0.39454916315058863, 'flat': 0.2265628854533299, 'up': 0.3788879513960815} | [-0.954945383108674, 0.9692030124354545, -0.014257629326783205] | {'down': 0.4042411932749432, 'flat': 0.22642030916006206, 'up': 0.36933849756499476} |
| 6 | E17/scenario | ['aa15b798-5e8f-56d9-b4dc-6e5fc7adc6e3', 'ba82517c-2626-5016-91ae-216aabfac820', '26a9cab3-7eff-5e16-b9f1-cd87ad8cbda5', '2d12a4e7-db91-5305-9930-a674f7a28b7f'] | {'down': 0.4042411932749432, 'flat': 0.22642030916006206, 'up': 0.36933849756499476} | [1.3448214451281415, 2.153099206851339, -3.4979206519794777] | {'down': 0.42577218534345657, 'flat': 0.19144110264026729, 'up': 0.3827867120162762} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42577218534345657, 'flat': 0.19144110264026729, 'up': 0.3827867120162762} | [-0.650269595820635, -1.2154917729712056, 1.8657613687918544] | {'down': 0.4136172676137445, 'flat': 0.21009871632818583, 'up': 0.3762840160580698} |
| 8 | E13/history | [] | {'down': 0.4136172676137445, 'flat': 0.21009871632818583, 'up': 0.3762840160580698} | [0.0, 0.0, 0.0] | {'down': 0.4136172676137445, 'flat': 0.21009871632818583, 'up': 0.3762840160580698} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4136172676137445, 'flat': 0.21009871632818583, 'up': 0.3762840160580698} | [-0.42856968990443445, -0.9725286857101889, 1.4010983756146094] | {'down': 0.4038919807566426, 'flat': 0.22410970008433193, 'up': 0.3719983191590255} |
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "score"
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.26666666666666666, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.1417176
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '0460688543846033ba70c0aed5bea7dd65414ba0279934c3e4a1554bda56222d'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:985d1521b871ff40eb2ba968a000b1e24d5347128e5e12645c73cb48435e440b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_rsi_14@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_trend_alignment@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#preferred_volume_z@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:065d3372028e3d78937d5157d7378359bca66cd7eead4d0f508d2429e4f78267#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:8c59db273b94b82b731483c49f906b4b39ec0536e556ce7dc1c52c6c814d6217#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:4521e91c6e8a52e3fcc6f632ad5eaf6f68643a08f12cfea99d6e7da61002f077#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "d2d7d4b7-78c3-5927-87b4-2ebedb62614a/1y/technical",
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
    "atr": 24677.23058029259,
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
      1028,
      1035
    ],
    "bottom_score": 0.0,
    "rsi": 56.527044746782224,
    "sma": [
      192885.0,
      126817.5,
      89079.58333333333
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.7543582011652433
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'd2d7d4b7-78c3-5927-87b4-2ebedb62614a/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "ea890eed-5fef-5709-82c0-47e8423b35b6",
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
    "hypothesis_id": "ea890eed-5fef-5709-82c0-47e8423b35b6",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.405
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
    "hypothesis_id": "8008a5df-3d40-51f2-a9d2-064f162bc5b6",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7856999999999998
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8008a5df-3d40-51f2-a9d2-064f162bc5b6",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": -1,
    "strength": 0.15322500000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8008a5df-3d40-51f2-a9d2-064f162bc5b6",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.06905823466378021
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
        "preferred_trend_alignment"
      ],
      "factor_id": "preferred_trend_alignment",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "score"
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
